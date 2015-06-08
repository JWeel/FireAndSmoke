import cv2
import time
import numpy as np
from Video import Video

class Frame:
	def __init__(self):
		cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
		cv2.resizeWindow('Frame', 2133, 600)
		self.video = None

	def setVideo(self, video):
		self.video = video

	def close(self):
		if self.video != None:
			self.video.close()
		cv2.destroyAllWindows()

	def run(self):
		ticks = int(time.time() * 1000)
		while self.video != None:
			newTicks = int(time.time() * 1000)
			if newTicks > (ticks + self.video.getInterval()):
				ticks = newTicks
				if not self.step():
					break

	def step(self):
		if cv2.waitKey(1) & 0xFF == ord('q'):
			self.close()
			return False
		img = res = self.video.read()
		double = np.hstack((img, res))
		cv2.imshow('Frame',double)
		return True