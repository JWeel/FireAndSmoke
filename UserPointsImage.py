#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

img = cv2.imread('6.jpg')

USERPOINTS = [[(236,155), 10], [(223,94),20]]

def drawUserPoints(img, points) :
	pass

cv2.imshow('img_orig',img)

cv2.waitKey(0)
cv2.destroyAllWindows()