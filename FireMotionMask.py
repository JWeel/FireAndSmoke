import cv2
from Transformation import Transformation
from FireMask import FireMask

class FireMotionMask(Transformation):
	def __init__(self):
		self.previousImg = None

	def transform(self, img):
		transformation = FireMask()
		res = transformation.transform(img)
		if self.previousImg != None:
			mask = cv2.bitwise_xor(res, self.previousImg)
		else:
			mask = res
		self.previousImg = res
		return mask