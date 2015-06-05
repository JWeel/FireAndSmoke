# Standard imports
import cv2
import numpy as np;

VIDEO_FILE = 'slaapkamerbrand2.mp4'

cap = cv2.VideoCapture(VIDEO_FILE);

while(cap.isOpened()):
	# Read frame from video
	RET, img = cap.read()

	# define range of fire color
	lower_fire = np.array([0,60,150])
	upper_fire = np.array([80,220,255])
	 
	# Threshold the HSV image to get only fire colors
	mask = cv2.inRange(img, lower_fire, upper_fire)

	blur = cv2.GaussianBlur(mask,(5,5),0)
	ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(th3,kernel,iterations=1)
	dilation = cv2.dilate(erosion,kernel,iterations=1)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(img,img, mask= dilation)

	cv2.imshow('frame',img)
	cv2.imshow('mask',dilation)
	cv2.imshow('res',res)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
