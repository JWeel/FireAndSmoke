from Transformation import Transformation
#from FirePixelDetector import FirePixelDetector
import numpy as np
import cv2
import math

class FireMask(Transformation):

	def __init__(self):
		self.kernel = np.ones((5, 5), np.uint8)
		self.sectors = None
		self.sector = np.matrix([0, 0]) # (width, height)
		self.squares = None
		self.fire = 0
		self.attention = {}
		self.frame = 0
		
	def transform(self, img):

		KERNEL    = np.ones((1, 1), np.uint8)
		RED_THRES = 180 # default 180
		SAT_THRES = 140 # default 140
		BUF_SIZE  = 30
		DIM       = np.array([20, 33]) # default 20, 33
		
		# Get HSV color space		
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
		# Compose mask according to different thresholds in RGB and HSV color 
		# space
		mask = np.all([
				img[:,:,2] > RED_THRES,
				img[:,:,2] > (img[:,:,1]*1.3), 
				img[:,:,1] > (img[:,:,0]*1.3),
				hsv[:,:,1] > SAT_THRES
			], axis=0).astype(np.uint8) * 255
		
		# Erode mask and dilate mask to remove noise
		erosion = cv2.erode(mask, KERNEL, iterations=1)
		dilation = cv2.dilate(erosion, KERNEL, iterations=1)
		
		# Compose output image
		#res = cv2.bitwise_and(img, img, mask=dilation)
		res = []
		# Initialize sector space
		if self.sectors == None:
			shape			= np.asarray(img.shape[0:2])
			self.sector 	= shape/DIM
			self.sectors 	= np.zeros(np.hstack((DIM, np.array([BUF_SIZE]))))
			self.squares	= np.zeros(DIM)
				
		# Increment frame		
		if self.frame < (BUF_SIZE - 1):
			self.frame += 1

		self.sectors = np.dstack((self.sectors[:,:,1:BUF_SIZE], np.zeros(DIM)))
			
		# Find contours in image
		contours0, hierarchy = cv2.findContours(
			dilation.copy(),
			cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE
		)
		
		moments  = [cv2.moments(cnt) for cnt in contours0]
		
		parameters = []
		for m in moments:
			  try:
			  	centroid = (int(round(m['m10']/m['m00'])), int(round(m['m01']/m['m00'])))
			  	parameters.append(centroid)
			  except ZeroDivisionError:
			  	pass

		# Set sectors in current frame
		for centroid in parameters:
			(x, y) = (centroid / self.sector)
			
			# For testing purposes only
			cv2.circle(img, (centroid), 10, (0,0,255), 1)
			
			if x < self.sectors.shape[1]:
				self.sectors[y, x - 1, BUF_SIZE-1] += 1
		
		for (y, x) in np.transpose(np.nonzero(np.sum(self.sectors, axis=2))):
			
			var = np.var(self.sectors[y, x, :])
			
			if var > 0.2:

				position = np.multiply([y, x], self.sector)
				
				if self.squares[y, x] < BUF_SIZE:
					self.squares[y, x] +=  BUF_SIZE
										
 		for (y, x) in np.transpose(np.nonzero(self.squares)):

 			position = np.multiply([y, x], self.sector)
 			
			cv2.rectangle(
				img,
				tuple(position[::-1]),
				tuple(position[::-1] + np.array(self.sector[::-1])),
				(0, 255, 0), 
				1,
				4
			)
			
			self.squares[y, x] -= 1

		return res