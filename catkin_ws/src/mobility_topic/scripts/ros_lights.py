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
from mobility_topic.msg import joystick, MultiJoy
from sensor_msgs.msg import Joy

from time import sleep
#import Adafruit_GPIO as GPIO
#import Adafruit_GPIO.FT232H as FT232H
from lights import Rover_Status_Lights
import threading
import sys

def update_mode(msg_data):
    print("enter update mode")
    global mode
    global last_updated
    last_updated = rospy.Time.now()
    mode = msg_data.mode.mode

def update_joy0(msg_data):
    print("enter joy0")
    global mode
    global last_updated
    last_updated = rospy.Time.now()
    mode = 5

def update_lights():
    print("enter update lights")
    status = Rover_Status_Lights(60)
    global mode
    global last_updated
    while not rospy.is_shutdown():
        if (rospy.Time.now() - last_updated) > rospy.Duration():
            mode = -1
            print("set mode to idle")
        status.update(mode)


if __name__ == '__main__':

    rospy.init_node('lights_node', anonymous=True)
    mode = 0
    last_updated = rospy.Time.now()

    rospy.Subscriber("joystick", joystick, update_mode)
    rospy.Subscriber("joy/0", Joy, update_joy0)

    threading.Thread(target=update_lights).start()
    rospy.spin()                                                  # Start the main loop



