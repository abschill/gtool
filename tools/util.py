import subprocess


def to_string(chars):
	return ' '.join(list(chars))

def sh(chars):
	str = to_string(chars)
	return subprocess.run(str, shell=True).returncode

def py(chars):
	cmd = 'python ' + to_string(chars)
	return subprocess.run(cmd, shell=True).returncode

def pip(chars):
	cmd = 'pip ' + to_string(chars)
	return subprocess.run(cmd, shell=True).returncode
