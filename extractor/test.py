from DoubleImageExtractor import DoubleImageExtractor
from Int16ImageExtractor import Int16ImageExtractor

extractor = DoubleImageExtractor()
#extractor = Int16ImageExtractor()
print extractor.extract('lwir.jl')