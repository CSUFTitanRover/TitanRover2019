#!/usr/bin/env python

import rospy
import os
import sys
import collections

# rosout msg format
from rosgraph_msgs.msg import Log



# Checks the Command Line Argument
if(len(sys.argv) >= 2):
    nodeName = sys.argv
else:
    print('Please enter name of Nodes as arguments') 
    exit()



# Initialize Circular Lists
InfoLogList = collections.deque(maxlen=5)
WarnLogList = collections.deque(maxlen=5)
DebugLogList = collections.deque(maxlen=5)
ErrorLogList = collections.deque(maxlen=5)
FatalLogList = collections.deque(maxlen=5)


# Data structure for Log Messages
class LogMsg(object):
    msg=''
    name=''
    file=''
    level=0



# Add subscribed data to Lists
def AddToList(data):
    temp = LogMsg()
    temp.msg = data.msg
    temp.name = data.name
    temp.file = data.file
    temp.level = data.level


    if data.level == 2:
        InfoLogList.append(temp)
    elif data.level == 4:
        WarnLogList.append(temp)
    elif data.level == 1:
        DebugLogList.append(temp)
    elif data.level == 8:
        ErrorLogList.append(temp)
    elif data.level == 16:
        FatalLogList.append(temp)


# Clear screen and print latest list data
def DisplayData():
    os.system('clear')

    print("************ INFO ************")
    for m in InfoLogList:
        print(m.msg + "\t" + m.name + "\t" + m.file)

    print("\n")

    print("************ WARN ************")
    for m in WarnLogList:
        print(m.msg + "\t" + m.name + "\t" + m.file)

    print("\n")

    print("************ DEBUG ************")
    for m in DebugLogList:
        print(m.msg + "\t" + m.name + "\t" + m.file)

    print("\n")

    print("************ ERROR ************")
    for m in ErrorLogList:
        print(m.msg + "\t" + m.name + "\t" + m.file)

    print("\n")

    print("************ FATAL ************")
    for m in FatalLogList:
        print(m.msg + "\t" + m.name + "\t" + m.file)


# Create a callback function for the subscriber
def callback(data):
    
    if data.name in nodeName:        
        AddToList(data)

    DisplayData()



def listener():
    # Get the ~private namespace parameters from command line or launch file.
    topic = rospy.get_param('~topic', 'rosout')
    # Create a subscriber with appropriate topic, custom message and name of callback function.
    rospy.Subscriber(topic, Log, callback)    

    # Wait for messages on topic, go to callback function when new messages arrive.
    rospy.spin()


# Main function
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('log_listener', anonymous = True)
    # Go to the main loop.
    listener()

