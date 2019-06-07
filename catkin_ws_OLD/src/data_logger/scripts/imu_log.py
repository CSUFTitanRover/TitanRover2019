#!/usr/bin/env python
import rospy
from time import sleep
from inspect import currentframe,getframeinfo

countLog = 0

if __name__== "__main__":
    
    rospy.init_node(name='imu', log_level=rospy.DEBUG)

    
    while True:
        countLog += 1 
        
        if(countLog % 5 == 1):
            rospy.logdebug("This is a debug message "+str(countLog))

        if(countLog % 5 == 2):
            try:
                a = 1/0
            except ZeroDivisionError:
                
                rospy.loginfo("Cannot divide by zero  lineno - "+str(getframeinfo(currentframe()).lineno)+ " count -"+str(countLog))

        
        if(countLog % 5 == 3):
            try:
                raise IOError
            except IOError:
                rospy.logerr("IO Error has occurred lineno - "+str(getframeinfo(currentframe()).lineno)+ " count -"+str(countLog))

        if(countLog % 5 == 4):
            try:
                raise EOFError
            except EOFError:
                rospy.logwarn("Reached End-Of-File warning lineno - "+str(getframeinfo(currentframe()).lineno)+ " count -"+str(countLog))

        if(countLog % 5 == 0):
            try:
                raise FloatingPointError
            except FloatingPointError:
                rospy.logfatal("Fatal Error Occurred lineno - "+str(getframeinfo(currentframe()).lineno)+ " count -"+str(countLog))

        sleep(2.5) # Time in seconds.