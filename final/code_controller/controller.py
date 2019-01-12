import socket
from time import sleep
import xbox
import json
import network

import threading

joy = xbox.Joystick()

# car_data = network.create_packet(CONNECT_TO_CAR, network.)

import netifaces as ni
ip = ni.ifaddresses('wlp0s20f0u2')[ni.AF_INET][0]['addr']

REMOTE_IP = ip
SERVER_IP = "192.168.1.1"
SERVER_PORT = 1337


ourcar = json.dumps({'ip':'192.168.1.100', 'port':6666})

# print(REMOTE_IP)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))
# sock.bind((REMOTE_IP, SERVER_PORT))

# sleep(1)

if not joy.connected():
  print("xbox disconnected")

notend = True
straight = True
goingf = False
goingb = False

class listenmalus(threading.Thread):

	def __init__(self, sock) :
		threading.Thread.__init__(self)
		self.sockcpy = sock

	def run(self) :
		while True :
			print("Listening for malus")
			data, addr = sock.recvfrom(SERVER_PORT)
			op_code, data = network.process_packet(data)
			if op_code == "GET_MALUS" :
				print("You have a tortoise to send")

t = listenmalus(sock)
t.start()

while notend :
	# print("command issued")
	if joy.Start() :
		print("ASKED CONNECTION")
		sock.sendto(network.create_packet(network.CONNECT_TO_CAR, ourcar), (SERVER_IP, SERVER_PORT))
	if joy.B() :
		print("Stopping program")
		notend = False
		sock.sendto(network.create_packet(network.MOVE_CAR, "STOP"), (SERVER_IP, SERVER_PORT))
	if joy.X() :
		sock.sendto(network.create_packet(network.MOVE_CAR,"IDLE"), (SERVER_IP, SERVER_PORT))
	if joy.rightTrigger() > 0.2 :
		sock.sendto(network.create_packet(network.MOVE_CAR,"FORWARD"), (SERVER_IP, SERVER_PORT))
		goingf = True
	elif joy.rightTrigger() < 0.2 and goingf : 
		sock.sendto(network.create_packet(network.MOVE_CAR,"BRAKE"), (SERVER_IP, SERVER_PORT))
		goingf = False
	if joy.leftTrigger() > 0.2:
		sock.sendto(network.create_packet(network.MOVE_CAR,"BACKWARDS"), (SERVER_IP, SERVER_PORT))
		goingb = True
	elif joy.leftTrigger() < 0.2 and goingb :
		sock.sendto(network.create_packet(network.MOVE_CAR,"BRAKE"), (SERVER_IP, SERVER_PORT))
		goingb = False
	if joy.leftX() < -0.3 :
		sock.sendto(network.create_packet(network.MOVE_CAR,"LEFT"), (SERVER_IP, SERVER_PORT))
		straight = False
	elif joy.leftX() > 0.3 :
		sock.sendto(network.create_packet(network.MOVE_CAR,"RIGHT"), (SERVER_IP, SERVER_PORT))
		straight = False
	elif not straight :
		sock.sendto(network.create_packet(network.MOVE_CAR,"STRAIGHT"), (SERVER_IP, SERVER_PORT))
		straight = True
	if joy.A() :
		sock.sendto(network.create_packet(network.SEND_MALUS,""), (SERVER_IP, SERVER_PORT))
		print("malus sent")

	sleep(0.1)