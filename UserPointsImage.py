#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import sys

img_file = sys.argv[1]
annotation_file = sys.argv[2]

img = cv2.imread(img_file)

USERPOINTS = [[(236,155), 10], [(223,94),20]]

# define range of fire color
FIRE_MIN = np.array([0,60,150])
FIRE_MAX = np.array([80,220,255])

def drawClassifiedPoints(img) :
	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)

	# HSV version of img
	hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	# Threshold the HSV image to get only fire colors
	mask = cv2.inRange(img, FIRE_MIN, FIRE_MAX)

	blur = cv2.GaussianBlur(mask,(5,5),0)
	ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	kernel = np.ones((7,7), np.uint8)
	erosion = cv2.erode(th3,kernel,iterations=1)
	dilation = cv2.dilate(erosion,kernel,iterations=1)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(img,img, mask= dilation)

	keypoints = detector.detect(res)
	
	cv2.imshow('result', res)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob
	return cv2.drawKeypoints(img, keypoints, np.array([]), (255,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# This function draws the trainingset points onto an image
def drawUserPoints(img, points) :
	for point in points:
		center = point[0]
		radius = point[1]
		img = cv2.circle(img, center, radius, (255,0,0), 0)
	return img

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 255

# Filter by Area.
params.filterByArea = True
params.minArea = 100
params.maxArea = 1000000

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87
    
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

img_test = drawClassifiedPoints(img)
img_overlay = drawUserPoints(img_test, USERPOINTS)

cv2.imshow('img_overlay',img_overlay)

cv2.waitKey(0)
cv2.destroyAllWindows()