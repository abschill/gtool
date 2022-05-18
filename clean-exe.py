import os, subprocess

splitter = filter(lambda fmap: len(fmap) < 2, list(map(lambda x: x.split('.'), os.listdir(os.getcwd()))))


status = 0

for fname in splitter:
    cmd = str("rm " + fname[0])
    status = subprocess.run(cmd, shell=True).returncode


print("Return Code: ", status)
