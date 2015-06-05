# Standard imports
import cv2
import numpy as np;
import sys
import time
import os.path

# check for command-line file, use default if none given
if len(sys.argv) < 2:
	VIDEO_FILE = 'aigfire.mp4'
else:
	VIDEO_FILE = sys.argv[1]

# halt if file doesn't exist
if not os.path.isfile(VIDEO_FILE):
	print 'Video file not found.'
	sys.exit()

cap = cv2.VideoCapture(VIDEO_FILE)

# calculate frame-rate for updating bit-masking
fps = cap.get(5) # 5 is index of the frame-rate property of video
frametime = 1000 / fps

# create window that will contain original and altered footage
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', 2133, 600)

while(cap.isOpened()):
	startlooptime = int(round(time.time() * 1000))
	# Read frame from video
	RET, img = cap.read()
	
	# Exit loop on last frame
	if RET == False:
		break

	# define range of fire color
	lower_fire = np.array([0,60,160])
	upper_fire = np.array([80,170,255])

	# Threshold the HSV image to get only fire colors
	mask = cv2.inRange(img, lower_fire, upper_fire)

	# Gaussian blur + Otsu's method to decrease noise (might not be useful)
	blur = cv2.GaussianBlur(mask,(5,5),0)
	ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	# Erode and Dilate filters blobs
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(th3,kernel,iterations=1)
	dilation = cv2.dilate(erosion,kernel,iterations=1)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(img,img, mask= dilation)

	double = np.hstack((img, res))

	cv2.imshow('Frame',double)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	# Run at 25 fps
	while int(round(time.time() * 1000)) < startlooptime + frametime:
		pass

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()