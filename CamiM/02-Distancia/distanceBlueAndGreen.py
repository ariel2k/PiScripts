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

    green_lower=np.array([40,100,100],np.uint8)
    green_upper=np.array([80,255,255],np.uint8)
    green=cv2.inRange(hsv,green_lower,green_upper)

    kernalGreen = np.ones((5 ,5), "uint8")

    kernalblue = np.ones((5 ,5), "uint8") 
    blue=cv2.erode(blue,kernalblue, iterations=1)

    cv2.bitwise_and(frame, frame, mask = green)
    cv2.bitwise_and(frame, frame, mask = blue)


    (_,contoursblue,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    (_,contoursgreen,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.namedWindow("blue",cv2.WINDOW_NORMAL)
    cv2.imshow("blue",blue)
    cv2.namedWindow("green",cv2.WINDOW_NORMAL)
    cv2.imshow("green",green)
    for pic, contourgreen in enumerate(contoursgreen):
        area = cv2.contourArea(contourgreen) 
        if(area>100):
            x,y,w,h = cv2.boundingRect(contourgreen)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(80,150,100),2)
            cv2.putText(frame,"Punto Verde",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            M = cv2.moments(contourgreen) 
            cx = int(M['m10'] /M['m00'])
            cy = int(M['m01'] /M['m00'])
            centers.append([cx,cy])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            break

    for pic, contoursblue in enumerate(contoursblue):
        area = cv2.contourArea(contoursblue) 
        if(area>100):
            x,y,w,h = cv2.boundingRect(contoursblue)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"Punto Azul",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            M = cv2.moments(contoursblue) 
            cx = int(M['m10'] /M['m00'])
            cy = int(M['m01'] /M['m00'])
            centers.append([cx,cy])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            break

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
        cv2.putText(frame, str(p1x-p2x), (x-8,y-8),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2, cv2.LINE_AA)
        print("D. Entre Y: " + str(p1y-p2y))
        cv2.putText(frame, str(p1y-p2y), (x-8,y-8),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2, cv2.LINE_AA)
        print("Hipotenusa: " + str(D))
        cv2.putText(frame, str(D), (cx-100,cy-50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2, cv2.LINE_AA)
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