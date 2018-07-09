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
    return vars(ap.parse_args())

def getVideoSource(args):
    if args["video"] is not None:
        return cv2.VideoCapture(args["video"])
    else:
        return cv2.VideoCapture(0)

def getFrame(videoSource):
    _,frame = videoSource.read()
    return frame

################ MAIN ########################
args = getArgs()
vs = getVideoSource(args)
while(1):
    # ReadFrame
    frame = getFrame(vs)
    action(frame)
    # Exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()