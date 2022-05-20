import requests, os
# probably set this properly later
p_path = os.getcwd()
b_files = 'bootstrap'
# global dotfiles regardless of proj type

def ctxpath(rel, f):
	if(f == None): return os.path.join(p_path, rel)
	return os.path.join(p_path, rel, f)

bs_path = os.listdir(ctxpath(b_files, ''))

for file in bs_path:
	f = open(ctxpath('bootstrap', file), 'r')
	open(file, 'wb').write(f.read())
