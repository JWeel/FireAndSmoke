from ImageProcessor import ImageProcessor

class SimpleTransformationProcessor(ImageProcessor):
	def __init__(self, transformation):
		self.transformation = transformation

	def process(self, manager):
		return self.transformation.transform(manager.get('rgb', 0))