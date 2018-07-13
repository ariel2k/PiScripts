import numpy as np

class Color:
	# constuctor
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

	def toBGR(self):
		return np.array([self.b,self.g,self.r],np.uint8)

class RangeColor:
	# constuctor
	def __init__(self, name, colorMin, colorMax):
		self.name = name
		self.colorMin = colorMin
		self.colorMax = colorMax

	def toBGRmin(self):
		return self.colorMin.toBGR()

	def toBGRmax(self):
		return self.colorMax.toBGR()

def getColors():
	cBlueMin = color.Color(100,150,80)
	cBlueMax = color.Color(150,255,255)
	cGreenMin = color.Color(40,100,100)
	cGreenMax = color.Color(80,255,255)
	colorBlue = color.ColorRange("Blue",cBlueMin, cBlueMax)
	colorGreen = color.ColorRange("Green",cGreenMin, cGreenMax)
	return [colorBlue, colorGreen]