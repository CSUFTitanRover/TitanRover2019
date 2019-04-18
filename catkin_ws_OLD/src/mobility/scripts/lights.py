#!/usr/bin/env python2.7
'''
Author: Georden Grabuskie ggrabuskie@csu.fullerton.edu
Driving ws2812 LED light strip from an SPI bus.

This code operates by syncing sent data to match the expected input
timing of the ws2812 LED light strips.
Uses the FT232H breakout board to add SPI capability to an open
USB port.

All base code taken directly from 
https://learn.adafruit.com/adafruit-ft232h-breakout/spi
'''
import rospy
from mobility.msg import Status
import threading
#import Adafruit_GPIO as GPIO
#import Adafruit_GPIO.FT232H as FT232H
from ws2812 import Rover_Status_Lights

def update_mode(msg_data):
    global mode, source
    print(msg_data)
    mode = msg_data.mode
    source = msg_data.source

def update_lights():
    status = Rover_Status_Lights(60)
    global mode
    while not rospy.is_shutdown():
        status.update(mode, source)
    status.set_all(0, 0, 0)


if __name__ == '__main__':
    mode = 0
    source = 0

    rospy.init_node('lights_node', anonymous=True)
    rospy.Subscriber("/telemetry", Status, update_mode)

    threading.Thread(target=update_lights).start()
    rospy.spin()                                                  # Start the main loop



