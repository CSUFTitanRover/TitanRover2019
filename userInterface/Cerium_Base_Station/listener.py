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



def Split_Coordinates(data):
    global LAT
    global LON
    print("Split_Coordinates("+data+")")
    data = data.split(" ")
    print("Split_Coordinates(): data: ",data)
    LAT = float(data[0])
    LON = float(data[1])
    print("Split_Coordinates(): LAT: ",LAT)
    print("Split_Coordinates(): LON: ",LON)



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
    while 1:
        data = conn.recv(256).decode()
        print("new_socket(): Received: ", data)
        Split_Coordinates(data)
        print("new_socket(): LAT: ",LAT)
        print("new_socket(): LON: ",LON)
        db.insert(LAT,LON, "map")
	       #print(db.l("map"))
        if not data: break
        print("new_socket(): Received Data: ", data)
        conn.send(data)
    conn.close()
    return



if __name__ == '__main__':
    while 1:
        new_socket()
