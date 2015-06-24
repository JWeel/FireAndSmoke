from Video import Video

class VideoManager:
	def __init__(self, n=2):
		self.videos = {}
		self.n = n

	def addStream(self, name, filename):
		self.videos[name] = Video(filename, self.n)
		self.videos[name].open(filename)

	def get(self, name, t=0):
		return self.videos[name].get(t)

	def initialize(self):
		for i in range(self.n):
			self.read()

	def read(self):
		for name, video in self.videos.items():
			img = video.read()
			if img == None:
				return False
		return True

	def close(self):
		for name, video in self.videos.items():
			video.close()