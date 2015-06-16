import cv2
import time
import numpy as np
from Video import Video
from MotionEstimator import MotionEstimator

'''
@class Frame

Handles the windows and the video loop.
'''
class Frame:
	def __init__(self):
		self.transformations = []
		cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
		cv2.resizeWindow('Frame', 2133, 600)
		self.video = None
		self.previousImg = None

	'''
	Add a transformation.

	@param Transformation transformation
	'''
	def addTransformation(self, transformation):
		self.transformations.append(transformation)

	'''
	Set the video.

	@param Video video
	'''
	def setVideo(self, video):
		self.video = video

	'''
	Close the application, including the windows.
	'''
	def close(self):
		if self.video != None:
			self.video.close()
		cv2.destroyAllWindows()

	'''
	Enter the video loop.
	'''
	def run(self):
		ticks = int(time.time() * 1000)
		while self.video != None:
			newTicks = int(time.time() * 1000)
			if newTicks > (ticks + self.video.getInterval()):
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
		img = self.video.read()
		if self.previousImg != None:
			estimate = MotionEstimator(24).estimate(self.previousImg, img)
			for x in range(10):
				for y in range(10):
					i = x + estimate[0]
					j = y + estimate[1]
					img.itemset((300 + i, 300 + j, 2), 255)
					img.itemset((300 + i, 300 + j, 0), 0)
					img.itemset((300 + i, 300 + j, 1), 0)
		res = self.transform(img)
		double = np.hstack((img, res))
		cv2.imshow('Frame',double)
		self.previousImg = img
		return True

	'''
	Perform all transformations on the given image and return a transformed image.

	@param Image image
	'''
	def transform(self, image):
		transformedImage = image
		for transformation in self.transformations:
			transformedImage = transformation.transform(transformedImage)
		return transformedImage