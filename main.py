import sys
import argparse
from Frame import Frame
from FireMask import FireMask
from SimpleTransformationProcessor import SimpleTransformationProcessor
from MaskApplication import MaskApplication
from _dbus_bindings import Boolean
from JLVideo import JLVideo
from extractor.Int16ImageExtractor import Int16ImageExtractor

# check for command-line file, use default if none given

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--stream', help='the video file to stream', metavar='S', type=str, required=True)
parser.add_argument('--fps', help="frames per second", metavar='F', default=30, type=int)
parser.add_argument('--processor', help="processor to use", metavar='P', default='firemask', type=str)
parser.add_argument('--fullscreen', help="set output to fullsceen", action='store_true')

args = vars(parser.parse_args(sys.argv[1:]))
VIDEO_FILE = args['stream']

stack = True

if args['processor'] == 'firemask':
    processor = SimpleTransformationProcessor(FireMask())
    stack = False

#processor = MotionProcessor()
frame = Frame(processor, args['fps'], n=2, fullscreen=args['fullscreen'], stack=stack)
frame.addStream('rgb', VIDEO_FILE)

#video = JLVideo('SWIRCamera', '%05d_snap_SWIR.jl', Int16ImageExtractor(), n=2)
#frame.videoManager.videos['swir'] = video
#video.open('SWIRCamera')

frame.run()
frame.close()