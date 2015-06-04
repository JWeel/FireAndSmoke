#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

VIDEO_FILE = 'C:\Users\Yuri\Documents\UvA\Tweedejaarsproject\Data\Computer Vision on Drones\Testdag\GoPro Films\slaapkamerbrand2.mp4'

cap = cv2.VideoCapture(VIDEO_FILE);
print cap

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
