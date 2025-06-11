#!/bin/bash
echo "Setting up AgriAid..."

# Create virtual environment
python3 -m venv agriaid_env

# Activate virtual environment
source agriaid_env/bin/activate

# Install requirements
pip install -r requirements.txt

# Create necessary directories
mkdir -p models
mkdir -p uploads

echo ""
echo "Setup complete!"
echo ""
echo "To run AgriAid:"
echo "1. Make sure your model files are in the models/ directory"
echo "2. Run: python app.py"
echo "3. Open http://localhost:5000 in your browser"
echo ""
