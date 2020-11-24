import socket
import time
import math

UDP_IP = "192.168.1.224"
UDP_PORT = 5000
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes

    if data:
        sock.sendto("Pong", addr)
