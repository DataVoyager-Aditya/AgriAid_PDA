@echo off
echo Setting up AgriAid...

REM Create virtual environment
python -m venv agriaid_env

REM Activate virtual environment
call agriaid_env\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Create necessary directories
if not exist "models" mkdir models
if not exist "uploads" mkdir uploads

echo.
echo Setup complete!
echo.
echo To run AgriAid:
echo 1. Make sure your model files are in the models/ directory
echo 2. Run: python app.py
echo 3. Open http://localhost:5000 in your browser
echo.
pause
