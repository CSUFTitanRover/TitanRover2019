#!/usr/bin/env python

import rospy
from multijoy.msg import MultiJoy
from sensor_msgs.msg import Joy
import subprocess, sys

global drill
drill = 0.5

# To import packages from different Directories
rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from pysaber import DriveEsc


linear = DriveEsc(129, "notMixed")
motors = DriveEsc(128, "notMixed")

def main(data):
    global drill
    if data.joys[0].buttons[1] is 1 and drill >= 0.1:
        drill -= 0.05
    if data.joys[0].buttons[3] is 1 and drill <= 1.0:
        drill += 0.05
    #print(drill)
    motors.driveBoth(40*int(data.joys[0].axes[2]), 40*int(data.joys[0].axes[2]))
    #print(40*int(data.joys[0].axes[2]), 40*int(data.joys[0].axes[2]))
    linear.driveBoth(127*drill*int(data.joys[0].axes[5]), 127*drill*int(data.joys[0].axes[4]))
    #print(127*drill*int(data.joys[0].axes[5]), 127*drill*int(data.joys[0].axes[4]))

if __name__ == '__main__':
    rospy.init_node('talker_base_mobility', anonymous=True)
    rospy.Subscriber("/multijoy", MultiJoy, main)
    rospy.spin() 

