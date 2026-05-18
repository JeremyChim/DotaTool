cd /d "%~dp0"
::pip freeze > requirements.txt
::pip install pipreqs -i https://pypi.tuna.tsinghua.edu.cn/simple
::pip install pipreqs 
pipreqs ./
cmd