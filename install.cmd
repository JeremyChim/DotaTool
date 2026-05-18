cd /d "%~dp0"
rd /s /q "build"
rd /s /q "dist"
del /f /q "DotaTool.spec"
pyinstaller.exe -F -i main.ico main.py -n DotaTool
robocopy _install dist\_install /E
robocopy bot_script dist\bot_script /E
robocopy gi dist\gi /E
robocopy npc dist\npc /E
robocopy vpk dist\vpk /E
copy config.json dist\config.json /Y
rd /s /q "build"
del /f /q "DotaTool.spec"
cmd
