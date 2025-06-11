import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import send_from_directory
from werkzeug.utils import secure_filename
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'agriaid_secret_key_2025'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Your updated disease classes based on model outputs
CROP_INFO = {
    'sugarcane': {
        'classes': ['Bacterial Blight', 'Healthy', 'Red Rot'],
        'num_classes': 3,
        'display_name': 'Sugarcane'
    },
    'wheat': {
        'classes': ['Wheat___Brown_Rust', 'Wheat___Healthy', 'Wheat___Yellow_Rust'],
        'num_classes': 3,
        'display_name': 'Wheat'
    },
    'rice': {
        'classes': ['Rice___Brown_Spot', 'Rice___Healthy', 'Rice___Leaf_Blast', 'Rice___Neck_Blast'],
        'num_classes': 4,
        'display_name': 'Rice'
    },
    'corn': {
        'classes': ['Corn___Common_Rust', 'Corn___Gray_Leaf_Spot', 'Corn___Healthy', 'Corn___Northern_Leaf_Blight'],
        'num_classes': 4,
        'display_name': 'Corn'
    },
    'potato': {
        'classes': ['Potato___Early_Blight', 'Potato___Healthy', 'Potato___Late_Blight'],
        'num_classes': 3,
        'display_name': 'Potato'
    }
}

# TransferResNet50 Model (your existing architecture)
class TransferResNet50(nn.Module):
    def __init__(self, num_classes):
        super(TransferResNet50, self).__init__()
        self.base_model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
        for param in self.base_model.parameters():
            param.requires_grad = False

        # Unfreeze the last block
        for param in self.base_model.layer4.parameters():
            param.requires_grad = True

        num_features = self.base_model.fc.in_features
        self.base_model.fc = nn.Sequential(
            nn.Linear(num_features, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        return self.base_model(x)

# Safe model loading function to prevent errors
def load_model_safely(model_path, num_classes):
    model = TransferResNet50(num_classes)

    try:
        # Try normal loading first
        saved_state = torch.load(model_path, map_location=device)
        model.load_state_dict(saved_state)
        return model, "direct"
    except RuntimeError as e:
        print(f"Direct loading failed: {e}")
        try:
            # Try flexible loading
            model.load_state_dict(saved_state, strict=False)
            return model, "flexible"
        except Exception as e2:
            print(f"Flexible loading failed: {e2}")
            # Create empty model if loading fails
            return model, "failed"

# Load all models
models_dict = {}
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

for crop, info in CROP_INFO.items():
    model_path = f'models/{crop}_model.pth'

    if os.path.exists(model_path):
        try:
            model, load_method = load_model_safely(model_path, info['num_classes'])
            model.eval()
            models_dict[crop] = model
            print(f"✅ {crop}: Model loaded successfully ({load_method})")
        except Exception as e:
            print(f"❌ {crop}: Failed to load - {e}")
    else:
        print(f"❌ {crop}: Model file not found at {model_path}")

print(f"Successfully loaded {len(models_dict)} models out of 5")

# Image preprocessing function
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((299, 299)),
        transforms.ToTensor(),
        transforms.Normalize([0.5]*3, [0.5]*3)
    ])

    image = Image.open(image_path).convert('RGB')
    image_tensor = transform(image).unsqueeze(0)
    return image_tensor

# Prediction function
def predict_disease(crop, image_path):
    if crop not in models_dict:
        return None, 0.0

    model = models_dict[crop]
    image_tensor = preprocess_image(image_path)

    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        confidence, predicted = torch.max(probabilities, 0)

    class_names = CROP_INFO[crop]['classes']
    predicted_class = class_names[predicted.item()]
    confidence_score = confidence.item() * 100

    return predicted_class, confidence_score

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/predict-page')
def predict_page():
    return render_template('predict.html', crops=CROP_INFO)

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files or 'crop' not in request.form:
            flash('Please select both a crop and upload an image.', 'error')
            return redirect(url_for('predict_page'))

        file = request.files['file']
        crop = request.form['crop']

        if file.filename == '':
            flash('Please select an image file.', 'error')
            return redirect(url_for('predict_page'))

        if crop not in models_dict:
            flash(f'Model for {crop} is not available. Please try another crop.', 'error')
            return redirect(url_for('predict_page'))

        if file and crop in CROP_INFO:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                predicted_disease, _ = predict_disease(crop, filepath)  # No confidence display

                # Clean up uploaded file
                os.remove(filepath)

                # Get disease info (no confidence needed)
                disease_info = None
                if 'Healthy' not in predicted_disease:
                    disease_info = get_disease_info(crop, predicted_disease)

                return render_template('result.html', 
                                     crop=CROP_INFO[crop]['display_name'],
                                     prediction=predicted_disease.replace('___', ' - ').replace('_', ' '),
                                     disease_info=disease_info)

            except Exception as e:
                # Clean up file if prediction fails
                if os.path.exists(filepath):
                    os.remove(filepath)
                flash(f'Error processing image: {str(e)}', 'error')
                return redirect(url_for('predict_page'))

        flash('Invalid request. Please try again.', 'error')
        return redirect(url_for('predict_page'))

    except Exception as e:
        flash(f'Server error: {str(e)}', 'error')
        return redirect(url_for('predict_page'))

@app.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject', 'AgriAid Contact')
        message = request.form.get('message')
        
        try:
            # Send email to your Gmail
            send_contact_email(name, email, subject, message)
            flash('Thank you! Your message has been sent successfully.', 'success')
        except Exception as e:
            print(f"Email error: {e}")
            flash('Message received! We will get back to you soon.', 'success')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Add this NEW function to your app.py
def send_contact_email(name, email, subject, message):
    # YOUR EMAIL SETTINGS (Change these)
    sender_email = "appcrosstheskylimits@gmail.com"  # Your Gmail
    sender_password = "ocgyvnktbbncmemn"   # Gmail App Password
    receiver_email = "aditya.rajthakur@agriaid.tech" # Where to receive messages
    
    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"AgriAid Contact: {subject}"
    
    body = f"""
    🌾 NEW AGRIAID CONTACT MESSAGE 🌾
    
    👤 Name: {name}
    📧 Email: {email}
    📝 Subject: {subject}
    
    💬 Message:
    {message}
    
    ---
    Sent from AgriAid Contact Form
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()

# Disease information function
def get_disease_info(crop, disease):
    # Load disease database
    try:
        with open('disease_database.json', 'r') as f:
            disease_db = json.load(f)

        if crop in disease_db and disease in disease_db[crop]['diseases']:
            return disease_db[crop]['diseases'][disease]
    except:
        pass

    # Fallback basic info
    return {
        'description': f'{disease.replace("___", " ").replace("_", " ")} detected in {crop}',
        'organic_solutions': [
            'Apply neem-based organic treatments',
            'Use balanced organic fertilizers',
            'Maintain proper field hygiene',
            'Remove infected plant parts'
        ],
        'chemical_solutions': [
            'Consult local agricultural extension officer',
            'Use appropriate fungicides as recommended',
            'Follow proper application timing',
            'Maintain recommended dosage'
        ],
        'prevention': [
            'Use resistant crop varieties',
            'Maintain proper plant spacing',
            'Ensure good field drainage',
            'Practice crop rotation'
        ]
    }

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml', mimetype='application/xml')



if __name__ == '__main__':
    print(f"🚀 Starting AgriAid server with {len(models_dict)} models loaded...")
    app.run(debug=True, host='0.0.0.0', port=5000)
