@echo off
title IP Tool Homepage
cls
chcp 65001 >nul
echo.
echo.
echo.
echo.
echo.  ██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
echo.  ██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
echo.  ██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
echo.  ██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
echo.  ██║██║         ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
echo.  ╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═                                           
echo.                     
echo ==============================================================================
echo              WELCOME TO YOUR IP TOOL HUB - Made by: Dante Warhola
echo ==============================================================================
echo.
echo  [1] Run Angry IP Scanner and Auto Save Results
echo  [2] Exit
echo.
set /p choice="Enter your choice: "
if "%choice%"=="1" goto RunScanner
goto End

:RunScanner
echo Launching Angry IP Scanner...
python "%~dp0autostart_ip.py"

echo Starting autosave tracker...
python "%~dp0live_scan_tracker.py"

goto End

:End
echo.
echo Press any key to exit.
pause >nul