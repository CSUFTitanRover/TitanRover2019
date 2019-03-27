#!/usr/bin/env python

# Feinzimer, David. dfeinzimer@csu.fullerton.edu
# Updated 3/14/19

import socket
import sys
import subprocess

rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from roverdb import Database

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def new_socket():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('', 9600)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)
    sock.listen(1)

    db = Database()
    conn, addr = sock.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(256).decode()
	print("new_socket() Received: ", data)
        db.insert(data, "map")
	print(db.getTableSize("map"))
        if not data: break
        print("received data: ", data)
        conn.send(data)  # echo
    conn.close()
    return


if __name__ == '__main__':
    while 1:
        new_socket()

