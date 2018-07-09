import cv2
import argparse
import time
import numpy as np

# HERE MODIFY!!!!! 
def action(frame):
    centers=[]
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    blue_lower=np.array([80,150,100],np.uint8)
    blue_upper=np.array([150,255,255],np.uint8)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    kernal = np.ones((5 ,5), "uint8") 
    blue=cv2.erode(blue,kernal, iterations=1)
    res1=cv2.bitwise_and(frame, frame, mask = blue) 
    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    i=1
    for pic, contour in enumerate(contours):
        iPunto = "p" + str(i)
        area = cv2.contourArea(contour) 
        if(area>100):
            x,y,w,h = cv2.boundingRect(contour)
            # puntoTxt = "> " + iPunto
            # puntoTxt += " x: " + str(x-w) + " y: " + str(y-h)
            # print(puntoTxt)
            #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,iPunto,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            M = cv2.moments(contour) 
            cx = int(M['m10'] /M['m00'])
            cy = int(M['m01'] /M['m00'])
            centers.append([cx,cy])
            # puntoTxt = "> " + iPunto
            # puntoTxt += " cx: " + str(cx) + " cy: " + str(cy)
            # print(puntoTxt)
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
        if len(centers)==2:
            p1x = centers[0][0]
            p1y = centers[0][1]
            p2x = centers[1][0]
            p2y = centers[1][1]
            # linea entre los centros
            frame = cv2.line(frame, (p1x,p1y),(p2x,p2y), (255, 55, 40),6)
            # linea eje x
            frame = cv2.line(frame, (p1x,p1y),(p2x,p1y), (55, 255, 40),6)
            # linea eje y
            frame = cv2.line(frame, (p2x,p2y),(p2x,p1y), (55, 255, 40),6)

            D = np.linalg.norm(cx-cy)
            print("D. Entre X: " + str(p1x-p2x))
            print("D. Entre Y: " + str(p1y-p2y))
            print("Hipotenusa: " + str(D))
        i=i+1
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