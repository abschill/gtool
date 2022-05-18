#!/usr/bin/env python3
import requests, os
# probably set this properly later
p_path = os.getcwd()
b_files = 'bootstrap'
# global dotfiles regardless of proj type
dotfiles = [
    ['.editorconfig', 'https://raw.githubusercontent.com/abschill/html-chunk-loader/master/.editorconfig']
]

def ctxpath(rel, f):
	if(f == None): return os.path.join(p_path, rel)
	return os.path.join(p_path, rel, f)

bs_path = os.listdir(ctxpath(b_files, ''))

for file in bs_path:
	f = open(ctxpath('bootstrap', file), 'r')
	open(file, 'wb').write(f.read())
for url in dotfiles:
    r = requests.get(url[1], allow_redirects=True)
    open(url[0], 'wb').write(r.content)
