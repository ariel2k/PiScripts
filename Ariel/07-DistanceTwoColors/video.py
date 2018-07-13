import cv2

def getSource(args):
    if args["video"] is not None:
        return cv2.VideoCapture(args["video"])
    else:
        return cv2.VideoCapture(0)

def getFrame(videoSource):
    _,frame = videoSource.read()
    return frame

