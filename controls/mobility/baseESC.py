import sys
import os
import socket
from struct import *
from time import sleep, time, clock
import multiprocessing
import pygame
import numpy as np
import subprocess

global armAttached
armAttached = False

'''
global system
global armAction
system = subprocess.check_output("uname -a", shell=True).strip().decode("utf-8")
if "raspberrypi" in system:
    system = "pi"
    import RPi.GPIO as GPIO                 # For Arm Movement

    armAction = { 0 : {'pwm' : 17, 'dir' : 27, 'enab' : 22},
                  1 : {'pwm' : 16, 'dir' : 20, 'enab' : 21},
                  2 : {'pwm' : 18, 'dir' : 23, 'enab' : 24},
                  3 : {'pwm' : 5,  'dir' : 6,  'enab' : 13}
                }

    GPIO.setmode(GPIO.BCM)

    for i in range(len(armAction)):
        GPIO.setup(armAction[i]['pwm'], GPIO.OUT)
        GPIO.setup(armAction[i]['dir'], GPIO.OUT)
        GPIO.setup(armAction[i]['enab'], GPIO.OUT)

elif "tegra-ubuntu" in system:
    system = "tx2"
    sys.path.insert(0, subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8') + '/gpio/')
    from tx2gpio import Tx2Gpio
   
    armAction = { 0 : {'pwm' : 396, 'dir' : 466, 'enab' : 397},
                  1 : {'pwm' : 429, 'dir' : 428, 'enab' : 427},
                  2 : {'pwm' : 398, 'dir' : 298, 'enab' : 389},
                  3 : {'pwm' : 481, 'dir' : 254, 'enab' : 430}
                }
    
    pinsUsed = [ 396, 466, 397,
                 429, 428, 427,
                 398, 298, 389,
                 392, 296, 481 ]

    tx2 = Tx2Gpio(pinsUsed)                        # Instantiating The Class Object

    for i in range(len(pinsUsed)):
        tx2.setup(pinsUsed[i], 'out')

else:
    system = "none"
'''


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9898))
    sock.listen(5)

    while True:
        try:
            #accept connections from outside
            client, address = sock.accept()
            print("connection from ", client, address)
            break
        except:
            print("waiting for connection")

except:
    print("cannot connect to Base Station")


# To import packages from different Directories
rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from pysaber import DriveEsc

# Instantiating The Class Object
wheels = DriveEsc(128, "mixed")
armMix = DriveEsc(129, "notMixed")

'''
def runPwmPi():
    global armAction
    while True:
        GPIO.output(armAction[0]['pwm'], 1)
        sleep(.00038)
        GPIO.output(armAction[0]['pwm'], 0)
        sleep(.00003)

def runPwmTx2():
    global armAction
    while True:
        tx2.output(armAction[0]['pwm'], 1)
        sleep(.00038)
        tx2.output(armAction[0]['pwm'], 0)
        sleep(.00003)

def checkArmDirection(val):
    if val == -1:
        return '0' 
    elif val == 1:
        return '1'

def moveJoints(data):
    global armAction, system

    if system == 'tx2':
        for i in range(1):#len(data)):
            if data[i] != 0:
                tx2.output(armAction[i]['enab'], 0)
                tx2.output(armAction[i]['dir'], int(checkArmDirection(data[i])))
            else:
                tx2.output(armAction[i]['enab'], 1)

    elif system == 'pi':
        for i in range(1):#len(data)):
            if data[i] != 0:
                GPIO.output(armAction[i]['enab'], 0)
                GPIO.output(armAction[i]['dir'], int(checkArmDirection(data[i])))
            else:
                GPIO.output(armAction[i]['enab'], 1)
'''

def main():
    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)
        outVals = data.split(',')
        try:
            wheels.driveBoth(int(outVals[0]), int(outVals[1]))
            '''
            if armAttached:
                moveJoints([int(outVals[4]), int(outVals[5]), int(outVals[6]), int(outVals[7])])
                if outVals[-1] != '4':
                    armMix.driveBoth(int(outVals[2]), int(outVals[3]))                        
                else:
                    armMix.driveBoth(-(int(outVals[3])), int(outVals[3]))    
            '''        
        except:
            print("Mobility-main-drive error")


if __name__ == '__main__':

    # Only start the threads if the arm is attached
    try:
        '''
        if armAttached:
            if system == 'tx2':
                p1 = multiprocessing.Process(target=runPwmTx2)
                p1.start()
            elif system == 'pi':
                p1 = multiprocessing.Process(target=runPwmTx2)
                p1.start()
        '''

        # Start the main loop
        main()
    except (KeyboardInterrupt, SystemExit):
        #p1.terminate()
        raise