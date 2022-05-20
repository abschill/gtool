import os, util

status = 0
node_modules = os.path.join(os.getcwd(), "node_modules")

if os.path.exists(node_modules):
	status = util.sh('rm -rf node_modules')
if os.path.exists('package.json') and os.path.exists('yarn.lock'):
	status = util.sh('yarn', shell=True)

print("Exit Code: ", status)
