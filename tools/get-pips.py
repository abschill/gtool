#!/usr/bin/env python3
import util

status = 0
pips = [
	'pyyaml',
	'numpy',
	'Cython'
]

status = util.iprefix('pip install', pips)

print('Exit Code: ', status)
