@echo off
echo ========================================
echo Starting TOON-Maker Application
echo ========================================
echo.

REM Check if in correct directory
if not exist "backend\app.py" (
    echo ERROR: Please run this script from the TOON-Maker root directory
    pause
    exit /b 1
)

echo [1/2] Starting Backend Server...
start "TOON-Maker Backend" cmd /k "cd /d %~dp0backend && python app.py"

echo [2/2] Starting Frontend Development Server...
timeout /t 2 /nobreak >nul
start "TOON-Maker Frontend" cmd /k "cd /d %~dp0frontend && npm start"

echo.
echo ========================================
echo TOON-Maker is starting up!
echo ========================================
echo.
echo Backend: http://localhost:5000
echo Frontend: Will open automatically in browser
echo.
echo Two new terminal windows have been opened.
echo Close those windows to stop the servers.
echo.
pause
