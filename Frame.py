import cv2
import time
import numpy as np
from VideoManager import VideoManager
from Video import Video

'''
@class Frame

Handles the windows and the video loop.
'''
class Frame:
	def __init__(self, processor, fps):
		cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
		cv2.resizeWindow('Frame', 2133, 600)
		self.processor = processor
		self.videoManager = VideoManager(2)
		self.previousImg = None
		self.interval = int(1000 / fps)

	'''
	Add a video stream.

	@param string name
	@param string filename
	'''
	def addStream(self, name, filename):
		self.videoManager.addStream(name, filename)

	'''
	Close the application, including the windows.
	'''
	def close(self):
		self.videoManager.close()
		cv2.destroyAllWindows()

	'''
	Enter the video loop.
	'''
	def run(self):
		ticks = int(time.time() * 1000)
		self.videoManager.initialize()
		while True:
			newTicks = int(time.time() * 1000)
			if newTicks > (ticks + self.interval):
				ticks = newTicks
				if not self.step():
					break

	'''
	Execute a single step. This involves reading a new image, as well as
	checking for an exit event.
	'''
	def step(self):
		if cv2.waitKey(1) & 0xFF == ord('q'):
			self.close()
			return False
		if not self.videoManager.read():
			return False
		img = self.videoManager.get("rgb", 0)
		res = self.processor.process(self.videoManager)
		double = np.hstack((img, res))
		cv2.imshow('Frame',double)
		self.previousImg = img
		return True
