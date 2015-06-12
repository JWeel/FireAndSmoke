#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;
import sys
import time 
#import os
#for file in os.listdir("."):
#    print(file)

if len(sys.argv) < 2:
	VIDEO_FILE = 'aigfire.mp4'
else:
	VIDEO_FILE = sys.argv[1]
	
#VIDEO_FILE = 'kelder_LWIR.mp4'

cap = cv2.VideoCapture(VIDEO_FILE);
#print cap

if not cap.isOpened():
	print 'error'

# calculate frame-rate for updating bit-masking
fps = cap.get(5) # 5 is index of the frame rate property of a video
frametime = 1000 / fps

while(cap.isOpened()):
	startlooptime = int(round(time.time() * 1000))
	#print 'Open'
	# Capture frame-by-frame
	RET, frame = cap.read()
	#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#frameg = cv2.GaussianBlur(frame, (5,5), 0)
	#frameh = cv2.equalizeHist(frameg)
	#frame = cv2.applyColorMap(frame, 2);

	#kernel = np.ones((20,20), np.uint8)
	#mask = cv2.inRange(frameh, 230, 255)
	#mask = cv2.bitwise_not(mask)
	#frame2 = cv2.bitwise_and(mask, frameh)
	#cv2.imshow('2',frame2)
	#cv2.imshow('1',frame)
	#cv2.imshow('3',frameh)

	frame = cv2.applyColorMap(frame, 2);
	frame = cv2.resize(frame, (0,0), fx = 1, fy = 1)
	cv2.imshow('frame_orig',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

		# Run at 25 fps
	while int(round(time.time() * 1000)) < startlooptime + frametime:
		pass

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
