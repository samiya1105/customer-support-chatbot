@echo off
echo Installing dependencies (if needed)...
py -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies.
    pause
    exit /b
)
cls
echo Starting Web Chatbot...
echo Open your browser to: http://localhost:5000
py app.py
pause
