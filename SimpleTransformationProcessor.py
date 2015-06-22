from ImageProcessor import ImageProcessor

class SimpleTransformationProcessor(ImageProcessor):
	def __init__(self, transformation):
		self.transformation = transformation

	def process(self, manager):
		img = manager.get('rgb', 0)
		res = self.transformation.transform()
		return (img, res) 