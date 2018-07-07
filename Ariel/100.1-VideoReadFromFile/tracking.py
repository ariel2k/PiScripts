import cv2
import argparse
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the video")
args = vars(ap.parse_args())

if args["video"] is None:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(args["video"])

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([10,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.imshow('frame',frame)
    cv2.resizeWindow('frame',400,250)

    cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
    cv2.imshow('mask',mask)
    cv2.resizeWindow('mask',400,250)

    cv2.namedWindow('res',cv2.WINDOW_NORMAL)
    cv2.imshow('res',res)
    cv2.resizeWindow('res',400,250)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()