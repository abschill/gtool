import util, sys

status = 0

## Downloads mp3 from youtube or whatever to disk

if len(sys.argv) < 2:
	exit('error: no url to download. exit 1')

# download with the merged audio + video
cmd = 'youtube-dl -f \'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4\' ' + sys.argv[1]
status = util.sh(cmd)
