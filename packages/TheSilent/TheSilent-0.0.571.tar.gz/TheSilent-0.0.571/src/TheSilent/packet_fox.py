import binascii
import socket
import struct
import threading
from TheSilent.clear import clear

CYAN = "\033[1;36m"
RED = "\033[1;31m"

def packet_thread(interface,data):
    sniffer_socket = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    sniffer_socket.bind((interface[1],0))
    print(CYAN + f"listening on interface {interface[1]}")
    if not data:
        while True:
            try:
                packet = sniffer_socket.recv(65536)
                my_data = binascii.hexlify(packet).decode()
                with open("hex_dump.txt", "a") as file:
                    file.write(my_data + "\n")

            except OSError:
                print(RED + f"interface {interface[1]} is down")
                break

    port_list = ["20","21","23","25","53","80","8000","8080","9100"]
    if data:
        while True:
            try:
                packet = sniffer_socket.recv(65536)
                port_send = binascii.hexlify(struct.unpack("!2s", packet[32:34])[0]).decode()
                port_recv = binascii.hexlify(struct.unpack("!2s", packet[34:36])[0]).decode()
                for port in port_list:
                    if port == str(int(port_send, 16)) or port == str(int(port_recv, 16)):
                        my_data = binascii.hexlify(packet).decode()
                        with open("hex_dump.txt", "a") as file:
                            file.write(my_data + "\n")

            except OSError:
                print(RED + f"interface {interface[1]} is down")
                break

            except struct.error:
                continue

def packet_fox(data=False):
    clear()
    interfaces = socket.if_nameindex()
    for interface in interfaces:
        if "lo" not in interface[1] and "bond" not in interface[1]:
            my_thread = threading.Thread(target=packet_thread, args=[interface,data]).start()
