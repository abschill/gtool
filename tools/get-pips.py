import util

status = 0
pips = [
	'pyyaml',
	'numpy',
	'cython',
	'opencv',
	'pyqt',
	'pywin32',
	'pytest',
	'pendulum',
	'plotly',
	'requests',
	'keras',
	'bokeh',
	'tkinter',
	'moviepy',
	'pygame',
	'chardet',
	'tqdm',
	'ipython',
	'scikit-learn',
	'pytorch',
	'scipy'
]
for i in pips:
	status = util.pip(('install', i))

print('Exit Code: ', status)
