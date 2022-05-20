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
	file_url = b_path+file
	print('Downloading:')
	print(file_url)
	with urllib.request.urlopen(file_url) as response:
		c = response.read()
		f = open(file, 'wb')
		f.write(c)
		f.close()

