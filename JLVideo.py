from Video import Video
import os.path
import sys

class JLVideo(Video):
	def __init__(self, filename, filenameFormat, extractor, n=2):
		Video.__init__(self, filename, n)
		self.filename = filename
		self.format = filenameFormat
		self.extractor = extractor
		self.currentIndex = 0
	
	def open(self, filename):
		if not os.path.exists(filename):
			print 'Directory not found'
			sys.exit()
		self.currentIndex = 0
		
	def read(self):
		filename = (self.filename + '/' + self.format) % self.currentIndex
		self.currentIndex += 1
		if not os.path.exists(filename):
			return None
		image = self.extractor.extract(filename)
		if image == None:
			return None
		self.addToBuffer(image)
		return image
	
	def close(self):
		pass