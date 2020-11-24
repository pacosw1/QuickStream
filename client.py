import socket
import time
import cv2

UDP_IP = "192.168.1.224"
UDP_PORT = 5000
MESSAGE = "Hello, World!"


fps = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


fps = 1 / 10


while True:
    sentAt = time.clock()
    sock.sendto("PING", (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(2048)

    if data:
        recvAt = time.clock()
        dt = (recvAt - sentAt) * 1000
        print(str(dt) + "ms")
    time.sleep(fps)
