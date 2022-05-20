import util

status = 0

status = util.sh('sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl')
status = util.sh('sudo chmod a+rx /usr/local/bin/youtube-dl')
status = util.sh('sudo apt install rig')
status = util.sh('sudo apt install 0ad')
status = util.sh('sudo apt install fnt')
status = util.sh('sudo apt install mpv')
status = util.sh('sudo apt install ffmpeg')
print('Exit Code: ', status)
