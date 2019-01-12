import socket
import RPi.GPIO as GPIO 
import time
import sys
import network

UDP_IP = "192.168.1.100"
SERVER_IP = "192.168.1.1"
UDP_PORT = 6666
SERVER_PORT = 1337
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', UDP_PORT))

sock.listen(10)
print("listening waiting for server connection")
(clientsocket, (ips, ports)) = sock.accept()

def message_loop():
    print("Car started")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    lel = True
    while lel:
        try:
            #print("listening for commands")
            data = clientsocket.recv(1048)
            lel = handle_message(data)
            
        except Exception as e:
            print("error when handling message", e)
        #time.sleep(0.1)

def handle_message(data):
    m_code, message = network.process_packet(data)
    if m_code == network.SEND_MALUS:
        return malus_message()
    else :
        return move_message(data.decode())
    return True

def malus_message():
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(37,GPIO.LOW)
    time.sleep(1)
    return True  

def move_message(message):
    #print("moving")
    if(message == "FORWARD"):
        GPIO.output(31,GPIO.HIGH)
        GPIO.output(37,GPIO.LOW)
    if(message == "BRAKE"):
        GPIO.output(31,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
    if(message == "RIGHT"):
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(33,GPIO.LOW)
    if(message == "LEFT"):
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.LOW)
    if(message == "STRAIGHT"):
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.LOW)
    if(message == "BACKWARDS"):
        GPIO.output(37,GPIO.HIGH)
        GPIO.output(31,GPIO.LOW)
    if(message == "IDLE"):
        GPIO.output(31,GPIO.LOW)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
    if(message == "STOP"):
        GPIO.output(31,GPIO.LOW)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
        GPIO.cleanup()
        return False
    return True
       
    
message_loop()
