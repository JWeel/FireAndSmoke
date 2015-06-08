import cv2
import os
import sys

class Video:
	def __init__(self, filename):
		# halt if file doesn't exist
		if not os.path.isfile(filename):
			print 'Video file not found.'
			sys.exit()
		self.cap = cv2.VideoCapture(filename)
		# calculate frame-rate for updating bit-masking
		self.fps = self.cap.get(5) # 5 is index of the frame rate property of a video
		self.frametime = 1000 / self.fps

	def getInterval(self):
		return self.frametime

	def read(self):
		retval, image = self.cap.read()
		if retval == False:
			return None
		return image

	def close(self):
		self.cap.release()