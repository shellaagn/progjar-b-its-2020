import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

namafile = "doge.jpg"
ukuran = os.stat(namafile).st_size

fp = open('doge.jpg', 'rb')
k = fp.read()
terkirim = 0
for x in k:
    k_bytes = bytes([x])
    sock.sendto(k_bytes, (TARGET_IP, TARGET_PORT))
    terkirim = terkirim + 1
    print(k_bytes, f"terkirim {terkirim} of {ukuran} ")
