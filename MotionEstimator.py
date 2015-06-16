import cv2
import numpy

class MotionEstimator:
	def __init__(self, size, paletteSize=32, threshold=5000):
		self.size = size
		self.paletteSize = paletteSize
		self.threshold = threshold

	'''
	Estimate the global motion between two images.
	
	@param numpy.Mat img1
	@param numpy.Mat img2
	@return (int, int) the global motion vector
	'''
	def estimate(self, img1, img2):
		x = 300
		y = 300
		g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
		g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
		
		bestMatch = None
		bestDistance = 99999
		
		for i in range(-self.size, self.size):
			for j in range(-self.size, self.size):
				dist = 0
				for k in range(x, x + self.size):
					for l in range(y, y + self.size):
						dist += abs(g1.item(k + i, l + j) - g2.item(k, l))
				if bestMatch == None or dist < bestDistance:
					bestMatch = (i, j)
					bestDistance = dist
		#if bestDistance < self.threshold:
		return bestMatch
		#else:
		#	return None