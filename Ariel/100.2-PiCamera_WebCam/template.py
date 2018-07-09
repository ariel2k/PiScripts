import cv2
import argparse
import time

# HERE MODIFY!!!!! 
def action(frame):
    show(frame,'Output')    

# Show Window
def show(frame,WindowName):
    cv2.namedWindow(WindowName,cv2.WINDOW_NORMAL)
    cv2.imshow(WindowName,frame)
    cv2.resizeWindow(WindowName,640,480)

def getArgs():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", 
        help = "path to the video (optional) default WebCam")
    ap.add_argument("-pi", "--picamera", 
        help = "if use PiCamera (optional) default 0")
    return vars(ap.parse_args())

################ INIT ########################
def videoSource(args):
    if args["picamera"] is not None:
        return initPiCamera()
    if args["video"] is not None:
        return initVideoFile(args["video"])
    else:
        return initWebCam()

def initPiCamera():
    from picamera.array import PiRGBArray
    import time
    camera = PiCamera()
    time.sleep(0.1)
    return camera

def initVideoFile(path):
    return cv2.VideoCapture(path)

def initWebCam():
    return cv2.VideoCapture(0)

################ FRAME ########################
def getFrame(args, videoSource):
    if args["picamera"] is not None:
        return framePiCamera(videoSource)
    elif args["video"] is not None:
        _,frame = frameVideoFile(videoSource)
    else:
        _,frame = frameWebCam(videoSource)
    return frame

def framePiCamera(videoSource):
    from picamera.array import PiRGBArray
    rawCapture = PiRGBArray(videoSource)
    videoSource.capture(rawCapture, format="bgr")
    image = rawCapture.array
    return image

def frameVideoFile(videoSource):
    return videoSource.read()

def frameWebCam(videoSource):
    return videoSource.read()


################ MAIN ########################
args = getArgs()
vs = videoSource(args)
while(1):
    # ReadFrame
    frame = getFrame(args, vs)
    action(frame)

    # Exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()