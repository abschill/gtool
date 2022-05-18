import os, subprocess

def bash(chars):
	return subprocess.run(chars, shell=True).returncode
