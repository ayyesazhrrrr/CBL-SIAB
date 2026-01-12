# setup.ps1 - Create virtualenv, install requirements, run migrations and (optionally) start server
# Usage:
#   .\setup.ps1          -> runs setup and starts the dev server
#   .\setup.ps1 -NoRun  -> runs setup only (doesn't start server)
param([switch]$NoRun)

# Ensure Python is available
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python not found in PATH. Install Python 3.8+ and try again."
    exit 1
}

# Create venv if missing
if (-not (Test-Path .\venv)) {
    python -m venv venv
    Write-Host "Created virtual environment at .\venv"
} else {
    Write-Host "Virtual environment already exists at .\venv"
}

# Bypass script policy for this session so activation can run
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Activate venv for the remainder of this script
. .\venv\Scripts\Activate.ps1

# Upgrade pip and install requirements
python -m pip install --upgrade pip
if (Test-Path .\requirements.txt) {
    python -m pip install -r requirements.txt
} else {
    Write-Warning "requirements.txt not found - skipping dependency install"
}

# Apply migrations
python manage.py migrate

if (-not $NoRun) {
    Write-Host "Starting Django development server..."
    python manage.py runserver
} else {
    Write-Host "Setup complete. Activate the venv later with: .\venv\Scripts\Activate.ps1"
}
