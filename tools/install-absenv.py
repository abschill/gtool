#!/usr/bin/env python3
import util

status = 0
status = util.pip('install pyyaml')

print('Exit Code: ', status)
