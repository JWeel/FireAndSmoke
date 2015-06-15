import sys
from Frame import Frame
from Video import Video
from FireMask import FireMask
from FireMotionMask import FireMotionMask
from MaskApplication import MaskApplication

# check for command-line file, use default if none given
if len(sys.argv) < 2:
	VIDEO_FILE = 'aigfire.mp4'
else:
	VIDEO_FILE = sys.argv[1]

video = Video(VIDEO_FILE)
frame = Frame()
frame.addTransformation(MaskApplication(FireMotionMask()))
frame.setVideo(video)
frame.run()