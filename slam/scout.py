#!/usr/bin/env python

import sys
######################################################################################
# System Requirement of one argument for process instructions
if len (sys.argv) != 2 :
    print "Usage: Run Command Missing "
    sys.exit (1)

import rospy
from sensor_msgs.msg import LaserScan
    
curr_pos = []

def store_info(data):
    global scoutfile
    print(data.pos)


def start_scouting():
    print("Scouting has begun")
    rospy.init_node('listener', anonymous=True)
    
        
    rospy.Subscriber("gnss", gps_position, store_info)




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


