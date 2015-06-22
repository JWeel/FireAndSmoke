import sys
import argparse
from Frame import Frame
from FireMask import FireMask
from SimpleTransformationProcessor import SimpleTransformationProcessor
from MaskApplication import MaskApplication

# check for command-line file, use default if none given

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--stream', help='the video file to stream', metavar='S', type=str, required=True)
parser.add_argument('--fps', help="frames per second", metavar='F', default=2, type=int)

args = vars(parser.parse_args(sys.argv[1:]))
VIDEO_FILE = args['stream']

processor = SimpleTransformationProcessor(FireMask())
frame = Frame(processor, args['fps'])
frame.addStream('rgb', VIDEO_FILE)
frame.run()
frame.close()