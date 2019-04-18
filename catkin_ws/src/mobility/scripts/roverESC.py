#!/usr/bin/env python

'''
File:         roverESC.py
Authors:      Georden Grabuskie / Shripal Rawal / Timothy Parks
Emails:       ggrabuskie@csu.fullerton.edu / rawalshreepal000@gmail.com / parkstimothyj@gmail.com
Description:  sends movement commands to ESC's and updates telemetry data node
'''
import rospy, subprocess, sys
from multijoy.msg import MultiJoy
from mobility.msg import Status
from sensor_msgs.msg import Joy

# To import packages from different Directories
rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from pysaber import DriveEsc
import pyarm



# Instantiating The Class Object For PySabertooth
wheels = DriveEsc(128, "mixed")
armMix = DriveEsc(129, "notMixed")

IDLE_TIMEOUT = 15 #seconds
#use actual button numbers instead of 0-indexed array
b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12 = range(12)
a1, a2, a3 = range(3)

#comms source for reference (variables not used)
ERROR = -1
LOCAL = 0
GHZ = 1
MHZ = 2

#modes
PAUSE = -1 #LS + B3
IDLE = 0
MOBILITY = 1 #LS + B2
ARM = 2    #LS + B4
BOTH = 3  #R2 + B1

#instantiate publisher structure
telem = Status()
telem.source = -1
telem.mode = MOBILITY
telem.throttle = .3
telem.armAttached = True

#global variables
last_mode = telem.mode
last_active
#axes and buttons
a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12
def setStop(joy_data):
    joy_data.joys[0].axes[0] = 0 
    joy_data.joys[0].axes[1] = 0 
    joy_data.joys[0].axes[2] = 0 
    joy_data.joys[0].axes[3] = 0 
    joy_data.joys[0].axes[4] = 0 
    joy_data.joys[0].axes[5] = 0 
    joy_data.joys[0].buttons[0] = 0 
    joy_data.joys[0].buttons[1] = 0 
    joy_data.joys[0].buttons[2] = 0 
    joy_data.joys[0].buttons[3] = 0 
    joy_data.joys[0].buttons[4] = 0 
    joy_data.joys[0].buttons[5] = 0 
    joy_data.joys[0].buttons[6] = 0 
    joy_data.joys[0].buttons[7] = 0 
    joy_data.joys[0].buttons[8] = 0 
    joy_data.joys[0].buttons[9] = 0 
    joy_data.joys[0].buttons[10] = 0
    joy_data.joys[0].buttons[11] = 0
    return joy_data

def setVals(joy_data):
    global a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12
    a1 = joy_data.joys[0].axes[0]
    a2 = joy_data.joys[0].axes[1] 
    a3 = joy_data.joys[0].axes[2] 
    a4 = joy_data.joys[0].axes[3] 
    a5 = joy_data.joys[0].axes[4] 
    a6 = joy_data.joys[0].axes[5] 
    b1 = joy_data.joys[0].buttons[0] 
    b2 = joy_data.joys[0].buttons[1] 
    b3 = joy_data.joys[0].buttons[2] 
    b4 = joy_data.joys[0].buttons[3] 
    b5 = joy_data.joys[0].buttons[4] 
    b6 = joy_data.joys[0].buttons[5] 
    b7 = joy_data.joys[0].buttons[6]
    b8 = joy_data.joys[0].buttons[7] 
    b9 = joy_data.joys[0].buttons[8] 
    b10 = joy_data.joys[0].buttons[9] 
    b11 = joy_data.joys[0].buttons[10]
    b12 = joy_data.joys[0].buttons[11]

def isActive(msg_data):
    try:
        if (abs(msg_data.joys[0].axes[0]) > 0 \
        or abs(msg_data.joys[0].axes[1]) > 0 \
        or abs(msg_data.joys[0].axes[2]) > 0 \
        or abs(msg_data.joys[0].axes[3]) > 0 \
        or abs(msg_data.joys[0].axes[4]) > 0 \
        or abs(msg_data.joys[0].axes[5]) > 0 \
        or abs(msg_data.joys[0].buttons[0]) > 0 \
        or abs(msg_data.joys[0].buttons[1]) > 0 \
        or abs(msg_data.joys[0].buttons[2]) > 0 \
        or abs(msg_data.joys[0].buttons[3]) > 0 \
        or abs(msg_data.joys[0].buttons[4]) > 0 \
        or abs(msg_data.joys[0].buttons[5]) > 0 \
        or abs(msg_data.joys[0].buttons[6]) > 0 \
        or abs(msg_data.joys[0].buttons[7]) > 0 \
        or abs(msg_data.joys[0].buttons[8]) > 0 \
        or abs(msg_data.joys[0].buttons[9]) > 0 \
        or abs(msg_data.joys[0].buttons[10]) > 0 \
        or abs(msg_data.joys[0].buttons[11]) > 0):
            return True
        else:
            return False
    except:
        print("error in getActive")




def main(data):
    global telem, last_active, last_mode, a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12
    setVals(data)
    #wake from sleep
    if isActive(data):
        last_active = data.header.stamp
        if telem.mode == IDLE:
            telem.mode = last_mode 

    telem.source = data.source
    if telem.source == 3:
        telem.mode = MOBILITY
    #go to sleep if time and save the last used mode other than idle
    if (rospy.Time.now() - last_active) > rospy.Duration(IDLE_TIMEOUT):
        if (telem.mode != IDLE):
            last_mode = telem.mode
        telem.mode = IDLE
        telem_pub.publish(telem)
    #set mode
    if(data.joys[0].buttons[b9]):
        #data = setStop(data) #set no movement
        if(b3):
            telem.mode = PAUSE
        elif(b2):
            telem.mode = MOBILITY
        elif(b4):
            telem.mode = ARM
        elif(b1):
            telem.mode = BOTH
    else:#single key presses for throttle
        if(b4 and (telem.throttle < 1) and ((rospy.Time.now() - last_active) > rospy.Duration(0.25))):
            telem.throttle += 0.1
            last_active = rospy.Time.now()
        elif (b2 and (telem.throttle > .3) and ((rospy.Time.now() - last_active) > rospy.Duration(0.25))):
            telem.throttle -= 0.1
            last_active = rospy.Time.now()
        else:
            try:
                print(telem)
                telem_pub.publish(telem)
                if telem.mode in {MOBILITY, BOTH}:
                    #turn in place
                    if b1:
                        wheels.driveBoth(0,-63)
                    elif b3:
                        wheels.driveBoth(0,63)
                    else:
                        #normal movement
                        if telem.source is 3:
                            wheels.driveBoth(int(a2),int(a1))
                        else:
                            wheels.driveBoth(int(telem.throttle*127*a2),int(-1 * telem.throttle*127*a1))

                if telem.armAttached and telem.mode in {BOTH, ARM}:
                    armMix.driveBoth(int(127*a3),int(127*a4))#j2, j3
                    pyarm.armData(a5, a6, b5, b6, b7, b8) #j1, j4, j51, j52
            except:
                print("Mobility-main-drive error")

if __name__ == '__main__':
    try:
        rospy.init_node('rover_mobility', anonymous=True)
        last_active = rospy.Time.now()
        telem_pub = rospy.Publisher("telemetry", Status, queue_size=1)
        rospy.Subscriber("/multijoy", MultiJoy, main)

        rospy.spin() 
    except(KeyboardInterrupt, SystemExit):
        rospy.signal_shutdown("scheduled")
        raise

