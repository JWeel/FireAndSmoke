from SimpleFireMask import SimpleFireMask
import cv2
import numpy as np

class MotionEstimator:
    def __init__(self, size=32, origin=(100, 100), offset=16, stepSize=1):
        self.size = size
        self.origin = origin
        self.offset = offset
        self.stepSize = stepSize
        self.threshold = np.array([20], dtype=np.uint8)
    
    def estimate(self, img1, img2):
        bestOffset = (0, 0)
        mostMatches = 0
        f1 = img1
        f2 = img2
        #transformation = SimpleFireMask()
        #f1 = transformation.transform(img1)
        #f2 = transformation.transform(img2)
        g1 = f1.view()
        g2 = f2.view()
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, -1), (-1, 1)]
        for step in steps:
            for i in xrange(self.offset):
                offset = (self.origin[0] + step[0] * i, self.origin[1] + step[1] * i)
                h1 = g1[self.origin[0]:self.origin[1]:self.stepSize]
                h2 = g2[offset[0]:offset[1]:self.stepSize]
                diff = cv2.absdiff(h1, h2)
                diff = cv2.inRange(diff, np.array([0], dtype=np.uint8), self.threshold)
                numMatches = cv2.countNonZero(diff)
                if numMatches > mostMatches:
                    mostMatches = numMatches
                    bestOffset = offset
        return bestOffset