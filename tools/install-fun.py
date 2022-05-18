import run

status = 0

status = run.bash('sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl')
status = run.bash('sudo chmod a+rx /usr/local/bin/youtube-dl')
status = run.bash('sudo apt install rig')
status = run.bash('sudo apt install 0ad')
status = run.bash('sudo apt install fnt')
print('Exit Code: ', status)
