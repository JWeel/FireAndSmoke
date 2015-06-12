from Transformation import Transformation
import numpy as np
import cv2

class FireMask(Transformation):
	def transform(self, img):
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		# get dimensions
		height, width, depth = img.shape
		redThres = 200
		satThres = 150

		mask = np.zeros((height, width), dtype=np.uint8)

		for i in range(0, height):
			for j in range(0, width):
				if img.item(i,j,2) > redThres and img.item(i,j,2) > img.item(i,j,1) and img.item(i,j,1) > img.item(i,j,0): 
					if hsv.item(i,j,1) > 200: 
						mask[i,j] = 255

		kernel = np.ones((1,1), np.uint8)
		erosion = cv2.erode(mask,kernel,iterations=1)
		dilation = cv2.dilate(erosion,kernel,iterations=1)

		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(img,img, mask= dilation)
		return res