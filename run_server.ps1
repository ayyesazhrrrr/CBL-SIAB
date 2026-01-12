# run_server.ps1 - Activate project's venv and start the Django dev server
# Usage: .\run_server.ps1

if (-not (Test-Path .\venv\Scripts\Activate.ps1)) {
    Write-Error "Virtual environment not found. Run .\setup.ps1 first."
    exit 1
}

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
. .\venv\Scripts\Activate.ps1
python manage.py runserver
