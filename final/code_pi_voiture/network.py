from struct import pack
from struct import unpack
from struct import calcsize as sizeof


CONNECT_TO_CAR = 1
MOVE_CAR = 2
GET_MALUS = 3
SEND_MALUS = 4


# Cree un paquet avec le code du type de message
def create_packet(op_code, data):
    return pack("!I{}s".format(len(data)), op_code, data.encode('utf-8'))


# Extrait le code du type de message ainsi que les donnees du paquet
def process_packet(packet):
    return unpack("!I{}s".format(len(packet)-sizeof("!I")), packet)

