#!/usr/bin/env python3.5

# External module imports
import RPi.GPIO as GPIO
import time
import os
import threading
import rospy
from sensor_msgs.msg import Joy

os.environ["ROS_MASTER_URI"] = "http://192.168.1.2:11311"
os.environ["ROS_IP"] = "192.168.1.136"

global armData
armData = [0,0,0,0]

armAction = { 0 : {'pwm' : 17, 'dir' : 27},
              1 : {'pwm' : 16, 'dir' : 20},
              2 : {'pwm' : 18, 'dir' : 23},
              3 : {'pwm' : 5,  'dir' : 6 }
            }

GPIO.setmode(GPIO.BCM)

for i in range(len(armAction)):
    GPIO.setup(armAction[i]['pwm'], GPIO.OUT)
    GPIO.setup(armAction[i]['dir'], GPIO.OUT)

def checkArmDirection(val):
    if val == '1':
        return 0
    else: 
        return 1


def pwm(j):
    global armData, armAction
    i = int(j)
    while True:
        GPIO.output(armAction[i]['pwm'], abs(armData[i]))
        time.sleep(5/1000000.0)
        GPIO.output(armAction[i]['pwm'], 0)
        #time.sleep(2/1000000.0)

def main(data):
    global armData
    try:
        armData = [int(data.axes[4]), int(data.axes[5]), data.buttons[4] - data.buttons[6], data.buttons[5] - data.buttons[7]]
        for i in range(4):
            GPIO.output(armAction[i]['dir'], checkArmDirection(str(armData[i])))
        #print(armData)
    except:
        #pass
        print("Mobility-main-drive error")


if __name__ == '__main__':
    try:
        threading.Thread(target=pwm, args=('0')).start()
        threading.Thread(target=pwm, args=('1')).start()
        threading.Thread(target=pwm, args=('2')).start()
        threading.Thread(target=pwm, args=('3')).start()

        rospy.init_node('talker_base_mobility', anonymous=True)
        rospy.Subscriber("joy/0", Joy, main)
        rospy.spin()
    except(KeyboardInterrupt, SystemExit):
        rospy.signal_shutdown()
        raise


#J1  = 0-Left   1-Right SleepOn=15/1000000.0    SleepOff=None   Resistor = Yellow
# Green(step) - Yellow(dir)
#90 degree = 156000
#1  degree = 1733.3333

#J4  = 0-UP     1-Down  SleepOn=15/1000000.0    SleepOff=       Resistor = Gray
# Yellow(step) - Orange(dir)
#90 degree = 
#1  degree = 

#5.1 = 0-       1-      SleepOn=  /1000000.0    SleepOff=       Resistor = Orange
# Gray(step) - White(dir)
#90 degree = 
#1  degree = 

#5.2 = 0-       1-      SleepOn=  /1000000.0    SleepOff=       Resistor = 
# Purple(step) - Blue(dir)
#90 degree = 
#1  degree = 

