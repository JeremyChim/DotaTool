cd /d "%~dp0"
rd /s /q "build"
rd /s /q "dist"
del /f /q "DotaTool.spec"
del /f /q "DotaTool.exe"
pyinstaller.exe -F -i main.ico main.py -n DotaTool
copy /y "dist\DotaTool.exe" "DotaTool.exe"
cmd
