import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

GPIO.output(31,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)

GPIO.cleanup()
