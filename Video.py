import cv2
import os
import sys

'''
@class Video

Encapsulates a single video and maintains an image stream.
'''
class Video:
	'''
	Constructor.

	@param string the filename of the video
	'''
	def __init__(self, filename):
		# halt if file doesn't exist
		if not os.path.isfile(filename):
			print 'Video file not found.'
			sys.exit()
		self.cap = cv2.VideoCapture(filename)
		# calculate frame-rate for updating bit-masking
		self.fps = self.cap.get(5) # 5 is index of the frame rate property of a video
		self.frametime = 1000 / self.fps

	'''
	Get the frame interval in ms.

	@return int 
	'''
	def getInterval(self):
		return self.frametime

	'''
	Read a single image from the video. Returns None if the video has ended.

	@return Image
	'''
	def read(self):
		if not self.cap.isOpened():
			return None
		retval, image = self.cap.read()
		if retval == False:
			return None
		return image

	'''
	Close the video stream.
	'''
	def close(self):
		self.cap.release()