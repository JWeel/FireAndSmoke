from Extractor import Extractor
import struct

class DoubleImageExtractor(Extractor):
    def getImageType(self):
        return 'DoubleImage'
    
    def getPixelByteCount(self):
        return 8
    
    def readPixel(self, pixelString):
        return struct.unpack('d', pixelString)