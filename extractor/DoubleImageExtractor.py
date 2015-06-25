from Extractor import Extractor
import struct

'''
@class DoubleImageExtractor
JL DoubleImage extractor. Can be used to extract SWIR images.
'''
class DoubleImageExtractor(Extractor):
    def getImageType(self):
        return 'DoubleImage'
    
    def getPixelByteCount(self):
        return 8
    
    def readPixel(self, pixelString):
        return struct.unpack('d', pixelString)