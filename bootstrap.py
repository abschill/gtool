import urllib, os
# probably set this properly later
p_path = os.getcwd()
b_path = 'https://raw.githubusercontent.com/abschill/gtool/main/bootstrap/'
# global dotfiles regardless of proj type
b_files = [
	'.editorconfig',
	'.gitkeep',
	'MakeFile',
	'authors',
	'license',
	'readme.md'
]

for file in b_files:
	f = urllib.URLopener()
	f.retrieve(b_path+file, file)
