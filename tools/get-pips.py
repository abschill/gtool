import util

status = 0
pips = [
	'pyyaml'
]

status = util.iprefix('pip install', pips)

print('Exit Code: ', status)
