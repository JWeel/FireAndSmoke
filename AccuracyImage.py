#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

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

# These two variables desrcibe the lower and upper
# bounds of HSV color space we want to classify
ORANGE_MIN = np.array([0, 10, 100],np.uint8)
ORANGE_MAX = np.array([34, 250, 250],np.uint8)

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)

img = cv2.imread('Fireimages\3.jpg')

# HSV version of img
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Filter for colors from red to yel*low
filter_img = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX);

# Invert img
filter_img = (255 - filter_img)

# Detect blobs.
keypoints = detector.detect(filter_img)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the resulting img
cv2.imshow('img_filter',filter_img)
cv2.imshow('img',img_with_keypoints)
cv2.imshow('img_orig',img)

cv2.waitKey(0)
cv2.destroyAllWindows()