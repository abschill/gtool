from platform import python_compiler
import subprocess

def sh(*chars):
	sep = ' '
	str = sep.join(chars)
	return subprocess.run(str, shell=True).returncode


def iprefix(prefix, iterators):
	for i in iterators:
		return sh(prefix, i)

def py(*chars):
	sep = ' '
	str = sep.join(chars)
	return subprocess.run(str, python_compiler=True).returncode
