from imutils.video import VideoStream
webcam = VideoStream(src=0).start()
while True:
    frame = webcam.read()
    print(frame)
