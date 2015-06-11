#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import os
import sys
import time

im1 = '00500_snap_RGB.bmp'
im2 = '00501_snap_RGB.bmp'

im1 = cv2.imread(im1)
im2 = cv2.imread(im2)

diff = cv2.bitwise_xor(im1, im2)

cv2.imshow('diff', diff) 