import run

status = 0

status = run.bash('sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl')
status = run.bash('sudo chmod a+rx /usr/local/bin/youtube-dl')
status = run.bash('apt install rig')

print('Exit Code: ', status)
