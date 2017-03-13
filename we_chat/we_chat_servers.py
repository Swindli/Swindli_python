#!/usr/bin/env python

import socket,traceback,sys

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

ClientSork,ClientAddr = s.accept()
while 1:
    try:
        buf = ClientSork.recv(1024)
        if len(buf):
            print "He say:"+buf
        data = raw_input("I say: ")
        ClientSork.sendall(data)
    except:
        print "Dialogue Over"
        ClientSork.close()
        sys.exit(0)
