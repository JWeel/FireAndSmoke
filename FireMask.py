from Transformation import Transformation
from FirePixelDetector import FirePixelDetector
import numpy as np
import cv2
import math


class FireMask(Transformation):

	def __init__(self):
		self.sectors = None
		self.sector = np.matrix([0, 0]) # (width, height)
		self.fire = 0
		self.attention = {}
		
	def transform(self, img):
		
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		# get dimensions
		height, width, depth = img.shape
		redThres = 180
		satThres = 40 # default 140

		#mask = np.zeros((height, width), dtype=np.uint8)

		# Thresholding
		#for i in range(0, height):
		#	for j in range(0, width):
		#		if img.item(i,j,2) > redThres and img.item(i,j,2) > img.item(i,j,1) and img.item(i,j,1) > img.item(i,j,0): 
		#			if hsv.item(i,j,1) > satThres: 
		#				mask[i,j] = 255
		
		mask = np.all([img[:,:,2] > redThres, img[:,:,2] > (img[:,:,1]*1.4), 
			img[:,:,1] > (img[:,:,0] * 1.4), hsv[:,:,1] > satThres], axis=0).astype(np.uint8) * 255
		
		# Creates arrays of x- and y- values within threshold
		#xcoords, ycoords = np.where(mask == 255)

		kernel = np.ones((1,1), np.uint8)
		erosion = cv2.erode(mask,kernel,iterations=1)
		dilation = cv2.dilate(erosion,kernel,iterations=1)
		
		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(img, img, mask= dilation)
		
		#test = cv2.dilate(mask,np.ones((9,9), np.uint8),iterations=1)
		#cv2.imshow("a", test)
		
		blobs = cv2.erode(mask, np.ones((5,5), np.uint8), iterations=1)
		blobs = cv2.dilate(blobs, np.ones((5, 5), np.uint8), iterations=1)
		
		contours0, hierarchy = cv2.findContours( blobs.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		moments  = [cv2.moments(cnt) for cnt in contours0]
		parameters = [(
					(int(round(m['m10']/m['m00'])), int(round(m['m01']/m['m00']))),
					(int(round(m['m10']-m['m00']))+int(round(m['m01']-m['m00'])))/4000
					) for m in moments]


		if self.sectors == None:
			shape  = np.asarray(img.shape[0:2])
			sector = (shape/[20, 30])
			self.sectors = np.zeros(shape/sector)
			self.sector  = sector

		self.sectors -= (self.sectors > 0).astype(int)
		
		if self.fire > 0:
			self.fire -= 1
	
	

		for key in self.attention.keys():
			if self.attention[key] > 0:
				radius = self.attention[key] + 30
				self.attention[key] -= 1
				(u, v) = key
				
				position = np.multiply([u+1, v+1], self.sector)
				
				cv2.circle(img, (position[0] + int(round(self.sector[0]*.5)), position[1] + 
								int(round(self.sector[1]*.5))), radius, (0,0,255), 3)

		for (centroid, radius) in parameters:
			sector = centroid/self.sector
			
			y = sector[0] - 1
			x = sector[1] - 1
			
			if self.fire == 0:
				self.attention[(y, x)] = 60
			
			if len(parameters) > 0 and self.fire < 300:
				self.fire += 10
			
			if y < self.sectors.shape[0] and self.sectors[y][x] < 10:
				self.sectors[y][x] += 5

			
			#position = np.multiply([y, x], self.sector)
			#position = np.matrix([x, y]) * self.sector
		for y in range(0, self.sectors.shape[0]):
			for x in range(0, self.sectors.shape[1]):
				if self.sectors[y][x] > 0:
					position = np.multiply([y+1, x+1], self.sector)
					cv2.rectangle(img, (position[0], position[1]),
								(position[0] + self.sector[0], position[1] + self.sector[1])
								 , (0, 255, 0), 1, 4)
		
		# Draw circle on center of blob. Works for single blob only
		#if len(xcoords) > 0:
		#	blobcenter = (int(round(np.average(ycoords))), int(round(np.average(xcoords))))
			# image, center, radius, color, thickness
		#	cv2.circle(img, blobcenter, 10 + int(round(math.sqrt(len(xcoords)))), (0,255,0),1)

		return res