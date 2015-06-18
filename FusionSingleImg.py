import numpy as np
import cv2

def getImageIntersect(im1, im2, offset):
	(ox, oy) = offset
	(h1, w1) = im1.shape
	(h2, w2) = im2.shape

	x1 = 0
	y1 = 0
	x2 = w1
	y2 = h1

	x3 = ox
	y3 = oy
	x4 = ox + w2
	y4 = oy + h2

	x5 = max(x1,x3)
	y5 = max(y1,y3)
	x6 = max(x2,x4)
	y6 = max(y2,y4)

	im1_overlap = im1[y5:y6,x5:x6]
	im2_overlap = im1[y5-oy:y6-oy,x5-ox:x6-ox]

	return (im1_overlap, im2_overlap)




# Load an color image in grayscale
im1 = cv2.imread('rectA.png',0)
im2 = cv2.imread('rectB.png',0) 

#img_scaled = cv2.resize(img_scaled, (0,0), fx = 0.15, fy = 0.15)

#(scaled_height, scaled_width) = img_scaled.shape

offset = (181,142)

intersects = getImageIntersect(im1, im2, offset)

cv2.imshow('window1', intersects[0])
cv2.imshow('window2', intersects[1])

cv2.waitKey(0)