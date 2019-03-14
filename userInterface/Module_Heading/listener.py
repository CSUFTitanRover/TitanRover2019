#!/usr/bin/env python

# Feinzimer, David. dfeinzimer@csu.fullerton.edu
# Updated 3/14/19

import socket

TCP_IP = '10.0.1.140'
TCP_PORT = 9600
BUFFER_SIZE = 1024


def new_socket():
    print("new socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Make the address reusable
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        data.decode()
        if not data: break
        print "received data:", data
        conn.send(data)  # echo
    conn.close()
    return


if __name__ == '__main__':
    while 1:
        new_socket()
