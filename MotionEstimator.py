import cv2
import numpy

class MotionEstimator:
	def __init__(self, size, paletteSize=32):
		self.size = size
		self.paletteSize = paletteSize

	def estimate(self, img1, img2):
		