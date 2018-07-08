# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	#image = frame.array



##############################
    # Take each frame
    _, image = frame.array

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([10,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(image,image, mask= mask)

    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.imshow('frame',image)
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
##############################
cv2.destroyAllWindows()


