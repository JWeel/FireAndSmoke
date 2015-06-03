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
ORANGE_MIN = np.array([0, 50, 100],np.uint8)
ORANGE_MAX = np.array([34, 250, 250],np.uint8)

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)

# Capture on camera 0
cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	RET, frame = cap.read()

	# Blur to alleviate noise
	frame = cv2.GaussianBlur(frame,(5,5),0)
	frame = cv2.GaussianBlur(frame,(5,5),0)

	# HSV version of frame
	hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	# Filter for colors from red to yellow
	filter_frame = cv2.inRange(hsv_frame, ORANGE_MIN, ORANGE_MAX);

	# Invert frame
	filter_frame = (255 - filter_frame)

	# Blur again to increase blobbiness of features
	filter_frame = cv2.GaussianBlur(filter_frame,(5,5),0)
	filter_frame = cv2.GaussianBlur(filter_frame,(5,5),0)

	# Detect blobs.
	keypoints = detector.detect(filter_frame)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob
	frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	# Display the resulting frame
	cv2.imshow('frame_filter',filter_frame)
	cv2.imshow('frame',frame_with_keypoints)
	cv2.imshow('frame_orig',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
