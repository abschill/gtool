import util

status = 0
statuc = util.py('-m pip install --upgrade pip')
status = util.py('pip install pyyaml')

print('Exit Code: ', status)
