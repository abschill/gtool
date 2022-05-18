import os, subprocess

status = 0
node_modules = os.path.join(os.getcwd(), "node_modules")

if os.path.exists(node_modules):
	status = subprocess.run('rm -rf node_modules', shell=True).returncode

status = subprocess.run('yarn', shell=True).returncode

print("Exit Code: ", status)
