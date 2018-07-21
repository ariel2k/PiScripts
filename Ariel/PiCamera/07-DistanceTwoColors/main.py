import cv2
import numpy as np
# módulo para los argumentos
import args
# módulo para el input de video
import video
# módulo para todo lo que tenga que ver con ventanas.
import window
# módulo para los colores a detectar
import color
# módulo para que trabaje con cada frame
import frame
 

def action(frame,colors):
    centers=[]
    hsv=frame.cvtColor(frame)

    (_,contoursblue,hierarchy) = frame.findColor(hsv,colors[0])
    (_,contoursgreen,hierarchy) = frame.findColor(hsv,colors[1])

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
    window.show(frame,'Output')    

################ MAIN ########################
args = args.getArgs()
vs = video.getSource(args)
colors = color.getColors()
while(1):
    frame = video.getFrame(vs)
    action(frame, colors)
    
    # Exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

window.destroy()