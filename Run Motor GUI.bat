@echo off
cd /d "%~dp0"
python -m ParaffinN2O_dimensioncalc
if errorlevel 1 pause
