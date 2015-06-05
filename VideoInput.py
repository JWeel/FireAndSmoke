#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

#import os
#for file in os.listdir("."):
#    print(file)


VIDEO_FILE = 'slaapkamerbrand2.mp4'

cap = cv2.VideoCapture(VIDEO_FILE);
print cap

if not cap.isOpened():
	print 'error'

while(cap.isOpened()):
	print 'Open'
	# Capture frame-by-frame
	RET, frame = cap.read()

	cv2.imshow('frame_orig',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
