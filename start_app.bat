@echo off
set PYTHON_PATH="C:\Users\user\AppData\Local\Programs\Python\Python314\python.exe"
echo Installing requirements using system Python...
%PYTHON_PATH% -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements.
    pause
    exit /b %errorlevel%
)
echo Requirements installed.
echo Starting application...
%PYTHON_PATH% run.py
pause
