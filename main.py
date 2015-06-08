from Frame import Frame
from Video import Video

video = Video('aigfire.mp4')
frame = Frame()
frame.setVideo(video)
frame.run()