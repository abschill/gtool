import urllib.request, os
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
	with urllib.request(b_path+file, file) as response:
		f = open(file, 'w')
		f.write(response.read())
		f.close()

