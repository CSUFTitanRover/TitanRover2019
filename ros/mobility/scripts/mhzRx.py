#!/usr/bin/env python

'''
File:         mhzRx.py
Authors:      Georden Grabuskie / Shripal Rawal / Timothy Parks 
Emails:        ggrabuskie@csu.fullerton.edu / rawalshreepal000@gmail.com / parkstimothyj@gmail.com 
Description:  Listens to Ebyte E32 transceiver and publishes telecommands to ROS
'''

import rospy, serial, struct
from multijoy.msg import MultiJoy
from sensor_msgs.msg import Joy
from mobility.msg import Status

 #to use sockets instead of rf for debug
import socket
host = "192.168.1.2"
port = 8888  # Make sure it's within the > 1024 $$ <65535 range
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))


def getRF(size_of_payload): #added argument to make it more function-like
    try:
        rf_uart = serial.Serial("/dev/serial/by-id/usb-Silicon_Labs_Rover433_0001-if00-port0", 19200, timeout=None)
        rf_uart.setDTR(True) #if the extra pins on the ttl usb are connected to m0 & m1 on the ebyte module
        rf_uart.setRTS(True) #then these two lines will send low logic to both which puts the module in transmit mode 0
        while True:
            n = rf_uart.read(1) #read bytes one at a time
            print("read 1")
            if not n:
                return 0
            if n == b's': #throw away bytes until start byte is encountered
                data = rf_uart.read(size_of_payload) #read fixed number of bytes
                n = rf_uart.read(1) #the following byte should be the stop byte
                if n == b'f':
                    return data
                else: #if that last byte wasn't the stop byte then something is out of sync
                    return -1
    except:
        print("error in getRF()")
        return -1
    return -1 #should never hit this return



def getSock():
    try:
        s.listen(1)
        client_socket, addr = s.accept()
        while True:
            data = client_socket.recv(128)
            if data:
                break
        return data
    except:
        print("Error in getSock()")


def unpackDEEZNUTZ(message): #object to bytes
    try:
        data = struct.unpack('iibbbbbbbbbbbbbbbbbb', message)
        t_joy = Joy()
        t_joy.header.stamp.secs = data[0]
        t_joy.header.stamp.nsecs = data[1]
        for i in range(2, 8):
            t_joy.axes.append(float(float(data[i]) / float(127)))
        for i in range(8, 20):
            t_joy.buttons.append(data[i])
        
        print("axes")
        for i in range(6):
            print(t_joy.axes[i])
        print("buttons")
        for i in range(0, 12):
            print(t_joy.buttons[i])
        
        return t_joy
    except:
        print("Error in D")


def monitor():
    rospy.init_node('MHz_Publisher', anonymous=True)
    multijoy_pub=rospy.Publisher('/multijoy', MultiJoy, queue_size=1)   #publisher for multijoy

    while not rospy.is_shutdown():
        try:
            message = getRF(26)
            msg = MultiJoy()
            joy0 = Joy()
            if message:
                joy0 = unpackDEEZNUTZ(message)
                msg.source = 2
                msg.header = joy0.header
                msg.njoys.data = 1
                msg.joys.append(joy0)
                print(msg)
                multijoy_pub.publish(msg)
        except:
            print("Error in main loop")

if __name__ == '__main__':
    try:
        monitor()
    except rospy.ROSInterruptException:
        pass