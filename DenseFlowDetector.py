import cv2
import numpy as np

SIZE = 40
threshold = 0

cap = cv2.VideoCapture("aigfire.mp4")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

def drawVector(img, flow):
	xmean = int(np.round(np.mean(flow[...,0]) * 500))
	ymean = int(np.round(np.mean(flow[...,1]) * 500))
	img = cv2.line(img, (50,50), (50+xmean, 50+ymean), (255,50,0), 1)
	return img


while(1):
	ret, frame2 = cap.read()
	next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

	flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 10, 3, 5, 1.2, 0)

	# mean x-comp
	xmean= np.mean(flow[...,0]) 
	# mean y-comp
	ymean= np.mean(flow[...,1]) 

	norm_flow = (np.subtract(flow[...,0], xmean), np.subtract(flow[...,1], ymean))

	xmean= np.mean(flow[...,0]) 
	# mean y-comp
	ymean= np.mean(flow[...,1]) 

	# Visuzalize in hsv space
	mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1]) 

	low_mag_ind = mag < threshold
	mag[low_mag_ind] = 0


	hsv[...,0] = ang*180/np.pi/2
	hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
	rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

	frame2 = drawVector(frame2, flow)

	cv2.imshow('frame2',rgb)
	cv2.imshow('frame3',frame2)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
	elif k == ord('s'):
		cv2.imwrite('opticalfb.png',frame2)
		cv2.imwrite('opticalhsv.png',rgb)
	prvs = next


cap.release()
cv2.destroyAllWindows()