@echo off
echo Setting up Amazon Strands virtual environment...

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete! Your virtual environment is now active.
echo To activate it manually in the future, run: venv\Scripts\activate.bat
echo To deactivate, run: deactivate
