# Amazon Strands Virtual Environment Setup Script
Write-Host "Setting up Amazon Strands virtual environment..." -ForegroundColor Green

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "Setup complete! Your virtual environment is now active." -ForegroundColor Green
Write-Host "To activate it manually in the future, run: venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host "To deactivate, run: deactivate" -ForegroundColor Cyan
