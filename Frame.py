import cv2
import time
import numpy as np
from VideoManager import VideoManager

'''
@class Frame

Handles the windows and the video loop.
'''
class Frame:
	def __init__(self, processor, fps, n=2, fullscreen=False, stack=True):
		cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
		if fullscreen:
			cv2.setWindowProperty('Frame', 
								cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
		
		if stack:
			cv2.resizeWindow('Frame', 2133, 600)
		else:
			cv2.resizeWindow('Frame', 1066, 600)
		
		self.processor = processor
		self.videoManager = VideoManager(n)
		self.previousImg = None
		self.interval = int(1000 / fps)
		self.stack = stack
		self.screenshot = 0

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
		
		key = cv2.waitKey(1) & 255

		if key == ord('q'):
			self.close()
			return False
		elif key == ord('s'):
			print "bla"
			if self.screenshot > 0:
				self.screenshot = 0
			else:
				self.screenshot = 1

		if not self.videoManager.read():
			return False
		(img, res) = self.processor.process(self.videoManager)
		
		if self.screenshot > 0:
			cv2.imwrite("screenshot" + str(self.screenshot) + ".jpg", img)
			if self.screenshot % 4 == 0 or self.screenshot % 4 == 1:
				cv2.circle(img, (20,20), 10, (0,0,255), -1)
			self.screenshot += 1
		
		
		if self.stack:
			double = np.hstack((img, res))
			cv2.imshow('Frame', double)
		else:
			cv2.imshow('Frame', img)
		
		self.previousImg = img
		return True
