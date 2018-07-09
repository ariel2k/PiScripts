import cv2
import argparse
import time
import sys

# HERE MODIFY!!!!! 
def action(frame):
    show(frame,'Output')    

# Show window
def show(frame,WindowName):
    cv2.namedWindow(WindowName,cv2.WINDOW_NORMAL)
    cv2.imshow(WindowName,frame)
    cv2.resizeWindow(WindowName,640,480)

# construct the argument parse and parse the arguments
def getArgs():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", 
        help = "path to the video (optional) default WebCam")
    ap.add_argument("-pi", "--picamera", 
        help = "if use PiCamera (optional) default 0")
    return vars(ap.parse_args())

# Get VideoSource
def getVideoSource(args, versionPy):
    vsTxt = "Video source: "
    if args["picamera"] is not None:
        vsTxt += "PiCamera "
        initPiCamera(versionPy)
    elif args["video"] is not None:
        vsTxt += "Video File "
        cap = cv2.VideoCapture(args["video"])
    else:
        vsTxt += "WebCam "
        cap = cv2.VideoCapture(0)
    print (vsTxt)
    print ("Press 'q' for exit...")
    return cap

def initPiCamera():
    if versionPy == '2':
        execfile('templatePiCamera.py')
    else:
        exec(open("./templatePiCamera.py").read())

############################ MAIN ##############################
versionPy = sys.version[0:1]
args = getArgs()
cap = getVideoSource(args,versionPy)

while(1):
    # Take each frame
    _, frame = cap.read()

    action(frame)

    # if the `q` key was pressed, break from the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
