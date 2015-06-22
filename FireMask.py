from Transformation import Transformation
from FirePixelDetector import FirePixelDetector
import numpy as np
import cv2
import math

class FireMask(Transformation):
	def transform(self, img):
		
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		# get dimensions
		height, width, depth = img.shape
		redThres = 180
		satThres = 140

		mask = np.zeros((height, width), dtype=np.uint8)

		# Thresholding
		#for i in range(0, height):
		#	for j in range(0, width):
		#		if img.item(i,j,2) > redThres and img.item(i,j,2) > img.item(i,j,1) and img.item(i,j,1) > img.item(i,j,0): 
		#			if hsv.item(i,j,1) > satThres: 
		#				mask[i,j] = 255
		
		mask = np.all([img[:,:,2] > redThres, img[:,:,2] > img[:,:,1], 
			img[:,:,1] > img[:,:,0], hsv[:,:,1] > satThres], axis=0).astype(np.uint8) * 255
		
		# Creates arrays of x- and y- values within threshold
		xcoords, ycoords = np.where(mask == 255)

		# Draw circle on center of blob. Works for single blob only
		if len(xcoords) > 0:
			blobcenter = (int(round(np.average(ycoords))), int(round(np.average(xcoords))))
			# image, center, radius, color, thickness
			cv2.circle(img, blobcenter, 10 + int(round(math.sqrt(len(xcoords)))), (0,255,0),1)

		kernel = np.ones((1,1), np.uint8)
		erosion = cv2.erode(mask,kernel,iterations=1)
		dilation = cv2.dilate(erosion,kernel,iterations=1)

		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(img, img, mask= dilation)

		return res