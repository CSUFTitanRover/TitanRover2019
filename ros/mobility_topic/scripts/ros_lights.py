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
from mobility_topic.msg import joystick

from time import sleep
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H
from lights import Rover_Status_Lights


def update_lights(msg_data):
        print(msg_data.mode.mode)
        status.update(msg_data.mode.mode)

if __name__ == '__main__':
    try:
        status = Rover_Status_Lights(60)
        rospy.init_node('lights_node', anonymous=True)
        rospy.Subscriber("joystick", joystick, update_lights)
        rospy.spin()                                                  # Start the main loop

    except (KeyboardInterrupt, SystemExit):
        rospy.signal_shutdown()
        raise

