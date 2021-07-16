@echo off
@rem throw this file in jetbrains installation folder, it takes the last created PyCharm folder (the latest ide update) for the script

FOR /F "delims=" %%i IN ('dir /b /ad-h /t:c /od -filter "PyCharm*"') DO SET a=%%i

SET PyCharmPath=D:\ProgramsD\PyCharm Community Edition 2019.2.1\bin\pycharm64.exe

echo %PyCharmPath%

echo Adding file entries
@reg add "HKEY_CLASSES_ROOT\*\shell\Open in PyCharm" /t REG_SZ /v "" /d "Open in &PyCharm"   /f
@reg add "HKEY_CLASSES_ROOT\*\shell\Open in PyCharm" /t REG_EXPAND_SZ /v "Icon" /d "%PyCharmPath%,0" /f
@reg add "HKEY_CLASSES_ROOT\*\shell\Open in PyCharm\command" /t REG_SZ /v "" /d "%PyCharmPath% \"%%1\"" /f

echo Adding folder entries
@reg add "HKEY_CLASSES_ROOT\Directory\shell\Open directory in PyCharm" /t REG_SZ /v "" /d "Open directory in &PyCharm"   /f
@reg add "HKEY_CLASSES_ROOT\Directory\shell\Open directory in PyCharm" /t REG_EXPAND_SZ /v "Icon" /d "%PyCharmPath%,0" /f
@reg add "HKEY_CLASSES_ROOT\Directory\shell\Open directory in PyCharm\command" /t REG_SZ /v "" /d "%PyCharmPath% \"%%1\"" /f

echo Adding folder background entries
@reg add "HKEY_CLASSES_ROOT\Directory\background\shell\Open directory in PyCharm" /t REG_SZ /v "" /d "Open directory in &PyCharm"   /f
@reg add "HKEY_CLASSES_ROOT\Directory\background\shell\Open directory in PyCharm" /t REG_EXPAND_SZ /v "Icon" /d "%PyCharmPath%,0" /f
@reg add "HKEY_CLASSES_ROOT\Directory\background\shell\Open directory in PyCharm\command" /t REG_SZ /v "" /d "%PyCharmPath% \"%%V\"" /f

pause
