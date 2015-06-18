import sys
import argparse
from Frame import Frame
from FireMask import FireMask
from SimpleTransformationProcessor import SimpleTransformationProcessor
from MaskApplication import MaskApplication

# check for command-line file, use default if none given

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--stream', nargs=1, help='the video file to stream', metavar='S', default='aigfire.mp4', type=str)
parser.add_argument('--fps', nargs=1, help="frames per second", metavar='F', default=2, type=int)

#if len(sys.argv) < 2:
#	VIDEO_FILE = 'aigfire.mp4'
#else:
#	VIDEO_FILE = sys.argv[1]

args = vars(parser.parse_args(sys.argv[1:]))
print args
VIDEO_FILE = args['stream']

processor = SimpleTransformationProcessor(FireMask())
frame = Frame(processor, args['fps'])
frame.addStream('rgb', VIDEO_FILE)
frame.run()
frame.close()