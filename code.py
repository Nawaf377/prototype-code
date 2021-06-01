import RPi.GPIO as GPIO
import time

# USE GPIO NUMBERS NOT PIN NUMBERS
GPIO.setmode(GPIO.BCM)

# PIN DEFINITION
Buzzer = 18
Triger = 23
Echo = 24


GPIO.setup(Triger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
GPIO.setup(Buzzer, GPIO.OUT)

# FUNCTIONS

def dits():
    GPIO.output(Triger, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(Triger, GPIO.LOW)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(Echo) == 0:
        StartTime = time.time()
    while GPIO.input(Echo) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    dits = (TimeElapsed * 34300) / 2
        

    
    return dits
        
    

try:
    while 1:
        dis = dits()
        
        if dis >= 25 or dis <= 0:
            GPIO.output(Buzzer, GPIO.LOW)
        else:
            GPIO.output(Buzzer, GPIO.HIGH)
            
        time.sleep(0.001)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    





