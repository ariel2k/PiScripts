import cv2
import numpy as np

def cvtColor(frame):
	return cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

def findColor(frame, color):
	#Se obtiene un histograma basada en las saturaciones de colores
	frameCVT = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#Se crea una mascara utilizando intervalos del color
	frameRange = cv2.inRange(frame,color.toBGRmin(),color.toBGRmax())
	#Crea una matriz de 5x5 la cual recorrera el video
	kernal = np.ones((5 ,5), "uint8")
	#Se erosiona utilizando el kernel sobre la mascara
	erosion = cv2.erode(frameRange,kernal, iterations=1)
	#La nueva imagen reemplazara a frame
	cv2.bitwise_and(frame, frame, mask = erosion)
	#Encuentra los contornos de los objetos que se ven en el filtro
	return cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)