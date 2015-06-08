from Frame import Frame
from Video import Video
from FireMask import FireMask

video = Video('aigfire.mp4')
frame = Frame()
frame.transformations.append(FireMask())
frame.setVideo(video)
frame.run()