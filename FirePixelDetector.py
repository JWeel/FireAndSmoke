import numpy
import cv2

class FirePixelDetector:
	def __init__(self, img, rednessThreshold, saturationThreshold):
		self.img = img
		self.hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		self.rednessThreshold = rednessThreshold
		self.saturationThreshold = saturationThreshold

	def detect(self, x, y):
		r = self.img.item((x, y, 2))
		g = self.img.item((x, y, 1))
		b = self.img.item((x, y, 0))
		s = self.hsvImg.item((x, y, 1))

		# Rule 1: R > Rt
		if not r > self.rednessThreshold:
			return False

		# Rule 2: R >= G > B
		if not (r >= g and g > b):
			return False

		# Rule 3: S > ((Rmax - R) * St/Rt)
		if not s > ((255 - r) * self.saturationThreshold / self.rednessThreshold):
			return False

		return True