import socket
from time import sleep
import random as rd

list_cars = {}

CAR_IP = "192.168.66.2"
SERVER_IP = "192.168.66.1"
REMOTE_IP = "192.168.66.4"
UDP_PORT = 1337


sockcar = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockcontroller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockcar.bind((SERVER_IP, UDP_PORT))

sockcontroller.listen(10)
(clientsock, (ips, ports)) = sockcontroller.accept()



def gen_malus(seed) :
	sock.sendto("GET_MALUS".encode('utf-8'), (list_remotes[seed], UDP_PORT+1))
	print("Malus sent")

def main_loop() :
	print("Start program main loop")
	lol = True
	while lol :
		a = int(rd.random()*50000)
		if a < len(list_remotes) :
			gen_malus(a)
		try :
			data, addr = sockcontroller.recvfrom(UDP_PORT)
			lol = handle_message(data)

		except Exception as e :
			print("Error in messages", e)

def handle_message(data):
	op,data = network.process_packet(data)
	if op_code == "SEND_MALUS" :
		print("send to someone")
	else :
		# print(type(data))
		sockcar.sendto(data.decode(), (CAR_IP, UDP_PORT))
	return True


main_loop()
