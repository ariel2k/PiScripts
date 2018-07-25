import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
 
for i in range(5):
   #Mover el motor hacia delante...
   GPIO.output(16, GPIO.HIGH)
   GPIO.output(18, GPIO.LOW)
   time.sleep(2)
 
   #...y hacia atras
   GPIO.output(16, GPIO.LOW)
   GPIO.output(18, GPIO.HIGH)
   time.sleep(2)
 
   #STOP!
   GPIO.output(16, GPIO.LOW)
   GPIO.output(18, GPIO.LOW)
   time.sleep(1)
 
GPIO.cleanup()