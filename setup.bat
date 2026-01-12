@echo off
REM setup.bat - Create venv, install requirements, run migrations
where python >nul 2>&1 || (
  echo Python not found in PATH. Install Python 3.8+ and try again.
  pause
  exit /b 1
)

if not exist venv (
  python -m venv venv
  echo Created virtual environment at venv\
) else (
  echo Virtual environment already exists at venv\
)

call venv\Scripts\activate.bat
python -m pip install --upgrade pip
if exist requirements.txt (
  python -m pip install -r requirements.txt
) else (
  echo requirements.txt not found - skipping dependency install
)
python manage.py migrate

echo Setup complete. To start the server, run: run_server.bat
pause
