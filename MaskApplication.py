from Transformation import Transformation
import cv2

class MaskApplication(Transformation):
	def __init__(self, maskTransformation):
		self.maskTransformation = maskTransformation

	def transform(self, img):
		res = cv2.bitwise_and(img,img, mask=self.maskTransformation.transform(img))
		return res