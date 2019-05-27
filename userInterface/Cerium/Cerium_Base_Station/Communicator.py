#!/usr/bin/env python

# Feinzimer, David. dfeinzimer@csu.fullerton.edu
# Updated 3/14/19

import socket
import sys
import subprocess

rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from roverdb import Database

global LAT
global LON
global TYPE

def Split_Coordinates(data):
    global LAT
    global LON
    global TYPE
    print "Split_Coordinates("+data+")"
    data = data.split(" ")
    print "Split_Coordinates(): data: ",data

    #LAT = float(data[0])
    #LON = float(data[1])

    LAT = data[0]
    LON = data[1]
    if LAT[len(LAT)-1] == "*":
        LAT = LAT[:-1]
    if LON[len(LON)-1] == "*":
        LON = LON[:-1]
    LAT = float(LAT)
    LON = float(LON)

    TYPE = data[2]
    print "Split_Coordinates(): LAT: ",LAT
    print "Split_Coordinates(): LON: ",LON
    print "Split_Coordinates(): TYPE: ",TYPE

def new_socket():
    global LAT
    global LON
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('', 9600)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)
    sock.listen(1)
    db = Database()
    conn, addr = sock.accept()
    print('Connection address:', addr)

    data = conn.recv(256).decode()
    print "new_socket(): Received: ", data
    Split_Coordinates(data)
    print ""
    data = conn.recv(256)
    print "new_socket(): LAT: ",LAT
    print "new_socket(): LON: ",LON
    print "new_socket(): TYPE: ",TYPE
    #db.insertMap("map",LAT,LON,TYPE)
    db.insertHint("hints",LAT,LON)
    #conn.send(data)

    conn.close()
    return



if __name__ == '__main__':
    while 1:
        new_socket()
