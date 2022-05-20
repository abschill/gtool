import util

status = 0
pips = [
	'pyyaml',
	'numpy',
	'Cython'
]
for i in pips:
	status = util.pip(('install', i))

print('Exit Code: ', status)
