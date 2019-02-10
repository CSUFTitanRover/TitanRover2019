#!/usr/bin/env python

import sys
######################################################################################
# System Requirement of one argument for process instructions
if len (sys.argv) != 2 :
    print("Usage: Run Command Missing ")
    sys.exit (1)

import rospy
from sensor_msgs.msg import LaserScan
from finalimu.msg import fimu

mode_info = None
acceleration = 0
curr_pos = []

def update_acceleration(data):
    global acceleration
    acceleration = data.accel

def store_info(data):
    global scoutfile, acceleration
    scoutfile.write(data.pos)
    #print(data.pos + ' ' + acceleration + '/n')

def mode_update(data):
    global mode_info
    mode_info = data.data


def start_scouting():
    print("Scouting has begun")
    #rospy.init_node('listener', anonymous=True)
    #rospy.Subscriber("mode", mobility, mode_update)
    #rospy.Subscriber("imu", fimu, update_acceleration)
    #rospy.Subscriber("gnss", gps_position, store_info)
    #ros.spin()



def parse_map_file():
    print('Parsing the Scout file')



if __name__ == '__main__':
    if sys.argv[1] == 'scout':
        scoutfile = open("scoutfile.txt", "w")
        start_scouting()
    elif sys.argv[1] == 'parse':
        parse_map_file()
    else:
        print('Unknown argument ' + sys.argv[1])
        exit()


