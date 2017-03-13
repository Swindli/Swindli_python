#!/usr/bin/env python

import socket,sys

host = '10.0.140.123'
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.connect((host,port))
except socket.gaierror,e:
    print "Address-related error connecting to server: %s" %e
    sys.exit(1)
except socket.error,e:
    print "Connection error: %s" %e
    sys.exit(1)

while 1:
    try:
        data = raw_input("I say: ")
        s.send(data)
        buf = s.recv(1024)
        if len(buf):
            print "He say:"+buf
    except:
        print"Dialogue Over"
        s.close()
        sys.exit(0)
