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
def getVideoSource(args):
    if args["picamera"] is not None:
        return initPiCamera()
    if args["video"] is not None:
        return initVideoFile(args["video"])
    else:
        return initWebCam()

def initPiCamera():
    from picamera import PiCamera
    import time
    camera = PiCamera()
    camera.framerate = 32
    return camera

def initVideoFile(path):
    return cv2.VideoCapture(path)

def initWebCam():
    return cv2.VideoCapture(0)

################ FRAME ########################
def getFrameNoPi(args, videoSource):
    if args["video"] is not None:
        _,frame = getFrameVideoFile(videoSource)
    else:
        _,frame = getFrameWebCam(videoSource)
    return frame

def getFrameVideoFile(videoSource):
    return videoSource.read()

def getFrameWebCam(videoSource):
    return videoSource.read()

################ ISPI ########################
def isPiCamera(args):
    return args["video"] is not None

################  PI  ########################
def yesPiCamera(videoSource):
    from picamera.array import PiRGBArray
    rawCapture = PiRGBArray(videoSource, size=(640, 480))
    for frame in videoSource.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        action(frame)
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # Exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

################ NOPI ########################
def noPiCamera(arg,videoSource):
    while(1):
        # ReadFrame
        frame = getFrameNoPi(args, videoSource)
        action(frame)

        # Exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

################ MAIN ########################
args = getArgs()
vs = getVideoSource(args)
if isPiCamera(args):
    yesPiCamera(vs)
else:
    noPiCamera(args,vs)
cv2.destroyAllWindows()