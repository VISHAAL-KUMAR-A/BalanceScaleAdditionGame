@echo off
echo ====================================
echo Balance Scale Game - Database Setup
echo ====================================
echo.

cd /d "%~dp0"

echo [1/2] Initializing database tables...
python init_game_tables.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================
    echo Setup completed successfully!
    echo ====================================
    echo.
    echo You can now start the backend server with:
    echo   uvicorn main:app --reload
    echo.
) else (
    echo.
    echo ====================================
    echo Setup failed! Check the error above.
    echo ====================================
    echo.
)

pause

