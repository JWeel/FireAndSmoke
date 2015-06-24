import numpy as np

'''
@class Extractor
@abstract

Abstract JL image extractor.
'''
class Extractor:
    def __init__(self, verbose=True):
        self.verbose = verbose
    
    '''
    Image header type.
    
    @return string
    '''
    def getImageType(self):
        pass
    
    '''
    Number of bytes per pixel.
    
    @return int
    '''
    def getPixelByteCount(self):
        pass
    
    '''
    Reads a string of byte characters and returns a pixel value.
    
    @return mixed
    '''
    def readPixel(self, pixelString):
        pass
    
    '''
    Reads an image JL Double file and returns a double image
    
    @param string filename
    @return np.Mat
    '''
    def extract(self, filename):
        f = open(filename, 'rb')
        header = f.read(2)
        if header != 'JL':
            if self.verbose:
                print 'Not a JL file'
            return None
        f.read(1)
        typeMatcher = 'DoubleImage'
        headerType = f.read(len(typeMatcher))
        f.read(1)
        if headerType != typeMatcher:
            if self.verbose:
                print headerType + ' is not a double image'
            return None
        height = int(f.read(4))
        width = int(f.read(4))
        size = height * width
        f.read(2)
        pixels = []
        byteCountPerPixel = self.getPixelByteCount()
        for i in xrange(size):
            pixelString = f.read(byteCountPerPixel)
            pixel = self.readPixel(pixelString)
            pixels.append(pixel)
        f.close()
        
        return np.reshape(np.array(pixels), (height, width))