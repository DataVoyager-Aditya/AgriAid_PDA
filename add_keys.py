import json

new_keys = {
    "tech_dl_title": "Deep Learning Models",
    "tech_dl_desc": "Our ResNet50-based architecture achieves 98.4% accuracy in disease detection, trained on thousands of crop images from Indian agricultural conditions.",
    "tech_db_title": "Comprehensive Database",
    "tech_db_desc": "Extensive disease database with organic and chemical treatment solutions, prevention methods, and crop-specific recommendations.",
    "tech_cloud_title": "Cloud Infrastructure",
    "tech_cloud_desc": "Scalable cloud-based processing ensures fast response times and reliable service availability for farmers across India.",
    "impact_accuracy": "Detection Accuracy",
    "impact_accuracy_desc": "Achieved through rigorous testing and validation on diverse crop datasets",
    "impact_farmers": "Farmers Supported",
    "impact_farmers_desc": "Helping farmers across different states improve their crop management",
    "impact_yield": "Yield Improvement",
    "impact_yield_desc": "Average increase in crop yields through early disease detection",
    "impact_crops": "Major Crops",
    "impact_crops_desc": "Comprehensive coverage of India's most important agricultural crops",
    "service_features_accuracy": "98.4% accuracy rate",
    "service_features_instant": "Instant results",
    "service_features_crops": "5 major crops supported",
    "service_features_multiple": "Multiple disease detection",
    "service_features_organic": "Organic treatment options",
    "service_features_chemical": "Chemical solutions with dosages",
    "service_features_prevention": "Prevention strategies",
    "service_features_specific": "Crop-specific recommendations",
    "service_features_devices": "Works on all devices",
    "service_features_internet": "Optimized for slow internet",
    "service_features_offline": "Offline-ready features",
    "service_features_ui": "User-friendly interface",
    "service_features_expert": "Expert consultation",
    "service_features_tech": "Technical support",
    "service_features_training": "Training resources",
    "service_features_community": "Community forum",
    "crop_wheat": "Wheat",
    "crop_rice": "Rice",
    "crop_corn": "Corn",
    "crop_sugarcane": "Sugarcane",
    "crop_potato": "Potato",
    "disease_brown_rust": "Brown Rust (Leaf Rust)",
    "disease_yellow_rust": "Yellow Rust (Stripe Rust)",
    "disease_healthy": "Healthy Crop Detection",
    "disease_brown_spot": "Brown Spot",
    "disease_leaf_blast": "Leaf Blast",
    "disease_neck_blast": "Neck Blast",
    "disease_common_rust": "Common Rust",
    "disease_gray_leaf": "Gray Leaf Spot",
    "disease_northern_blight": "Northern Leaf Blight",
    "disease_bacterial_blight": "Bacterial Blight",
    "disease_red_rot": "Red Rot",
    "disease_early_blight": "Early Blight",
    "disease_late_blight": "Late Blight"
}

try:
    with open('translations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for lang in data:
        for key, value in new_keys.items():
            if key not in data[lang]:
                data[lang][key] = value

    with open('translations.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("Successfully added new keys.")

except Exception as e:
    print(f"Error: {e}")
