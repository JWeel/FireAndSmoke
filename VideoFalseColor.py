#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

#import os
#for file in os.listdir("."):
#    print(file)


VIDEO_FILE = 'kelder_LWIR.mp4'

cap = cv2.VideoCapture(VIDEO_FILE);
print cap

if not cap.isOpened():
	print 'error'

while(cap.isOpened()):
	print 'Open'
	# Capture frame-by-frame
	RET, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frameg = cv2.GaussianBlur(frame, (5,5), 0)
	frameh = cv2.equalizeHist(frameg)
	#frame = cv2.applyColorMap(frame, 2);

	#kernel = np.ones((20,20), np.uint8)
	mask = cv2.inRange(frameh, 230, 255)
	#mask = cv2.bitwise_not(mask)
	frame2 = cv2.bitwise_and(mask, frameh)
	cv2.imshow('2',frame2)
	cv2.imshow('1',frame)
	cv2.imshow('3',frameh)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
