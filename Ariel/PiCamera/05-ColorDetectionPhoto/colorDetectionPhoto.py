# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries -- BGR no RGB
boundaries = [
        #ROJO
	([16, 10, 100], [162, 124, 182]),
        #AZUL
	([85, 72, 0], [211, 174, 0]),
        #AMARILLO
	([10, 195, 142], [155, 215, 191]),
        #BLANCO
	([210, 211, 171], [255, 255, 255])
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.namedWindow("images",cv2.WINDOW_NORMAL)
	cv2.imshow("images", np.hstack([image, output]))
	cv2.resizeWindow("images",1920,1080)
	cv2.waitKey(0)
