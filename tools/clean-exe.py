#!/usr/bin/env python3
import os, util

splitter = filter(lambda fmap: len(fmap) < 2, list(map(lambda x: x.split('.'), os.listdir(os.getcwd()))))
status = 0

for fname in splitter:
    cmd = str("rm " + fname[0])
    status = util.sh(cmd)


print("Return Code: ", status)
