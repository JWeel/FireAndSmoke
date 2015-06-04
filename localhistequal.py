# Standard imports
import cv2
import numpy as np;
#from matplotlib import pyplot as plt


VIDEO_FILE = 'slaapkamerbrand2.mp4'

cap = cv2.VideoCapture(VIDEO_FILE);

while(cap.isOpened()):
	print 'hoi'
	# Read image
	#img = cv2.imread("sl11.jpg", cv2.IMREAD_COLOR)
	#img = cv2.imread("fish.png", cv2.IMREAD_GRAYSCALE)
	#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	RET, img = cap.read()

	# create a CLAHE object (Arguments are optional).
	#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(32,32))
	#cl1 = clahe.apply(hsv[2])

	# Create histogram
	#hist = cv2.calcHist([img],[0],None,[256],[0,256])

	# Create histogram graph
	#plt.hist(cl1.ravel(),256,[0,256]); plt.show()

	# define range of fire color
	#lower_fire = np.array([0,60,150],uint8)
	#upper_fire = np.array([80,220,255],uint8)
	 
	# Threshold the HSV image to get only fire colors
	#mask = cv2.inRange(img, lower_fire, upper_fire)

	#blur = cv2.GaussianBlur(mask,(5,5),0)
	#ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


	#kernel = np.ones((7,7), np.uint8)
	#erosion = cv2.erode(th3,kernel,iterations=1)
	#dilation = cv2.dilate(erosion,kernel,iterations=1)

	# Bitwise-AND mask and original image
	#res = cv2.bitwise_and(img,img, mask= dilation)

	cv2.imshow('frame',img)
	#cv2.imshow('mask',dilation)
	#cv2.imshow('res',res)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Attach input and output images horizontally
#res = np.hstack((img,hsv))

# Show output image
#cv2.imshow("Equalized image", res)
#cv2.waitKey(0)