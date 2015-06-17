import sys
from Frame import Frame
from Video import Video
from FireMask import FireMask
from SimpleTransformationProcessor import SimpleTransformationProcessor
from MaskApplication import MaskApplication

# check for command-line file, use default if none given
if len(sys.argv) < 2:
	VIDEO_FILE = 'aigfire.mp4'
else:
	VIDEO_FILE = sys.argv[1]

processor = SimpleTransformationProcessor(MaskApplication(FireMask()))
frame = Frame(processor)
frame.addStream("rgb", VIDEO_FILE)
frame.run()