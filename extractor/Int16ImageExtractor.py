from Extractor import Extractor
import struct

class Int16ImageExtractor(Extractor):
	def getImageType(self):
		return 'Int16Image'
		
	def getPixelByteCount(self):
		return 2
		
	def readPixel(self, pixelString):
		return struct.unpack('h', pixelString)