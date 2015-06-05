# Standard imports
import cv2
import numpy as np;
import sys

# Does blob detection on given frame and draws them onto the frame
def classifyBlobs(img):
	# HSV version of img
	hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	# Filter for colors from red to yellow
	filter_img = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX);

	# Invert img
	filter_img = (255 - filter_img)

	# Detect blobs.
	keypoints = detector.detect(filter_img)
	
	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob
	return cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

if len(sys.argv) < 2:
	VIDEO_FILE = 'slaapkamerbrand2.mp4'
else:
	VIDEO_FILE = sys.argv[1]

cap = cv2.VideoCapture(VIDEO_FILE);

cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', 2133, 600)

while(cap.isOpened()):
	# Read frame from video
	RET, img = cap.read()

	# Exit loop on last frame
	if img == None:
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

	res_blobs = classifyBlobs(res)

	double = np.hstack((img, res_blobs))



	cv2.imshow('Frame',double)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

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
FIRE_MIN = np.array([0, 10, 100],np.uint8)
FIRE_MAX = np.array([34, 250, 250],np.uint8)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
