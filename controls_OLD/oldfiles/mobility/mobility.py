'''
File:        mobility.py
Authors:      Chary Vielma / Shripal Rawal
Emails:       chary.vielma@csu.fullerton.edu / rawalshreepal000@gmail.com
Description: Mobility script reads in a text file with configuration for various controllers. User actions
             are interpreted by pygame and mapped to rover Actions for wheel and arm control. Communicating 
             these values is handled by a separate classes.

             To start program with a different configuration than rumblepad, list .txt file after script name:
             e.g. <python version> mobility.py dual.txt
'''

import sys
import os
import socket
from struct import *
from time import sleep, time, clock
import multiprocessing
from datetime import datetime
import pygame
import numpy as np
import subprocess
import threading
from smbus2 import SMBusWrapper

global system
global armAction
import serial
#polo = serial.Serial('/dev/serial/by-id/usb-Pololu_Corporation_Pololu_A-Star_32U4-if00', 9600)

#armAddress = { 0 : 0x08, 1 : 0x09, 2 : 0x10, 3 : 0x11}
#armAddress = 0x08
#arm1 = [0,0,0,0];
#arm2 = [0,0,0,0];

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

#elif "tegra-ubuntu" in system:
#    system = "tx2"
#    sys.path.insert(0, subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8') + '/gpio/')
#    from tx2gpio import Tx2Gpio
#   
#    armAction = { 0 : {'pwm' : 396, 'dir' : 466, 'enab' : 397, 'sleep' : .000005},
#                  1 : {'pwm' : 429, 'dir' : 428, 'enab' : 427, 'sleep' : .000005},
#                  2 : {'pwm' : 398, 'dir' : 298, 'enab' : 389, 'sleep' : .000005},
#                  3 : {'pwm' : 481, 'dir' : 254, 'enab' : 430, 'sleep' : .000004}
#                }
#    
#    pinsUsed = [ 396, 466, 397,
#                 429, 428, 427,
#                 398, 298, 389,
#                 481, 254, 430 ]
#
#    tx2 = Tx2Gpio(pinsUsed)                        # Instantiating The Class Object
#
#    for i in range(len(pinsUsed)):
#        tx2.setup(pinsUsed[i], 'out')
#
#    for i in range(2, len(pinsUsed), 3):
#        tx2.output(pinsUsed[i], 1)

else:
    system = "none"


# To import packages from different Directories
rootDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8')
sys.path.insert(0, rootDir + '/build/resources/python-packages')
from pysaber import DriveEsc
from lights import Rover_Status_Lights

# Instantiating The Class Object
wheels = DriveEsc(128, "mixed")
armMix = DriveEsc(129, "notMixed")

# Initialize pygame and joysticks
os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.init()
pygame.joystick.init()

# System setup wait
sleep(2)

#Global declarations
global paused
global controlString
global controls  # Holds file configurations
global modeNum  # Current mode index to toggle modeNames lst
global mode  # Current set name (string) in use
global modeNames  # List of set names (strings) from .txt file
global actionTime  # Seconds needed to trigger pause / mode change
global maxRotateSpeed
global turnInPlace
global armIndependent
global armAttached
armAttached = True
armIndependent = True  # True means Independent Mode for Linear Actuators
paused = False
modeNum = 0
actionTime = 3
maxRotateSpeed = 50
turnInPlace = None

actionList = ['motor1', 'motor2', 'arm2', 'arm3', 'joint1', 'joint4', 'joint5a',
              'joint5b', 'reserved1', 'ledMode']  # List in order of output values

global roverActions

def setRoverActions():
    global roverActions
    roverActions =  {
              'motor1':    {'special': 'motor', 'rate': 'motor', 'direction': 1, 'value': 0},
              'motor2':    {'special': 'motor', 'rate': 'motor', 'direction': 1, 'value': 0},
              'arm3':      {'special': 'motor', 'rate': 'none', 'direction': 1, 'value': 0},
              'joint1':    {'special': 'none', 'rate': 'none', 'direction': 1, 'value': 0},
              'arm2':      {'special': 'motor', 'rate': 'none', 'direction': 1, 'value': 0},
              'joint4':    {'special': 'none', 'rate': 'none', 'direction': 1, 'value': 0},
              'joint5a':   {'special': 'none', 'rate': 'none', 'direction': 1, 'value': 0},
              'joint5b':   {'special': 'none', 'rate': 'none', 'direction': 1, 'value': 0},
              'reserved1': {'special': 'none', 'rate': 'none', 'direction': 1, 'value': 0},
              'ledMode':   {'special': 'none', 'rate': 'none', 'direction': 1, 'value': 0}}
    # Not rover actions, but stored in same location. These actions trigger events within this module
    roverActions['pause'] = {'held': False, 'direction': 1, 'value': 0, 'set': 0}  # Added to support 'pause' action
    roverActions['mode'] = {'held': False, 'direction': 1, 'value': 0}  # Added to support 'mode' action
    roverActions['throttle'] = {'direction': 1, 'value': 0.0}  # Throttle value for 'motor' rate multiplier (-1 to 1)
    roverActions['throttleStep'] = {'held': False, 'direction': 1, 'value': 0}  # Added to support button throttle
    roverActions['rotate'] = {'special': 'none', 'rate': 'none', 'direction': 1, 'value': 0}  # Added to support turn in place
    roverActions['armMode'] = {'held': False, 'direction': 1, 'value': 0, 'set': 0} # Added to support Mixed and Single Mode for Linear Actuators

setRoverActions()  # Initiate roverActions to enter loop

def startUp(argv):
    global controlString, controls, modeNames, mode, roverActions
    fileName = "rumblepad.txt"
    if len(sys.argv) == 2:
        fileName = str(sys.argv[1])
    elif len(sys.argv) > 2:
        print("Exceeded arguments")
        sys.exit()
    try:
        configDir = subprocess.check_output('locate TitanRover2019 | head -1', shell=True).strip().decode('utf-8') + '/controls/mobility/txtConfig/' + fileName
        controlString = open(configDir).read().replace('\n', '').replace('\r', '')
    except IOError:
        print ("Unable to open file " + configDir)
        sys.exit()
    controls = eval(controlString)
    modeNames = list(sorted(controls.keys()))
    mode = modeNames[modeNum]  # mode 0 = both, mode 1 = mobility, mode 2 = arm, mode 3 = arm Single(Not Mixed)
    roverActions['mode']['set'] = modeNum
    roverActions['ledMode']['value'] = controls[mode]['ledCode']

def stop():
    global paused
    paused = True

def getZero(*arg):
    return 0

def getOne(*arg):
    return 1

def getRate():
    return roverActions['throttle']['direction'] * roverActions['throttle']['value']  # If axis needs to be reversed

specialMultipliers = {'motor': 110, 'none': 1}
rateMultipliers = {'motor': getRate, 'none': getOne}

def throttleStep():
    global roverActions
    if (not roverActions['throttleStep']['held'] and roverActions['throttleStep']['value']):  # New button press
        roverActions['throttleStep']['held'] = True
        throttle = round(roverActions['throttle']['value'] * 10.0) / 10  # Round out analog value to tenths place
        change = roverActions['throttleStep']['direction'] * roverActions['throttleStep']['value'] * 0.2
        throttle += change
        if throttle < -0.6:
            throttle = -0.6
        if throttle > 0.8:
            throttle = 0.8
        roverActions['throttle']['value'] = throttle
    if (roverActions['throttleStep']['held'] and not roverActions['throttleStep']['value']):  # Button held, but released
        roverActions['throttleStep']['held'] = False

def computeSpeed(key):
    val = roverActions[key]
    throttleValue = rateMultipliers[val['rate']]()  # Get current rate multiplier (-1 to +1), calls getRate or getOne accordingly
    calcThrot = np.interp(throttleValue, [-1 , 1], [0, 1])
    return int(specialMultipliers[val['special']] * calcThrot * val['direction'] * val['value'])

def checkArmMode():
    global armIndependent, roverActions, modeNum, mode
    if (not roverActions['armMode']['held'] and roverActions['armMode']['value']):  # New button press
        roverActions['armMode']['held'] = True
        roverActions['armMode']['lastpress'] = datetime.now()
    if (roverActions['armMode']['held'] and not roverActions['armMode']['value']):  # Button held, but now released
        roverActions['armMode']['held'] = False
    if (roverActions['armMode']['held'] and roverActions['armMode']['value'] and (
        datetime.now() - roverActions['armMode']['lastpress']).seconds >= actionTime):  # Button held for required time
        roverActions['armMode']['lastpress'] = datetime.now()  # Keep updating time as button may continue to be held
        armIndependent = not armIndependent
        modeNum = 0 if armIndependent else 3
        mode = modeNames[modeNum]
        setRoverActions()  # Clear all inputs
        roverActions['mode']['set'] = modeNum
        roverActions['ledMode']['value'] = controls[mode]['ledCode']


def checkPause():
    global paused, roverActions
    if (not roverActions['pause']['held'] and roverActions['pause']['value']):  # New button press
        roverActions['pause']['held'] = True
        roverActions['pause']['lastpress'] = datetime.now()
    if (roverActions['pause']['held'] and not roverActions['pause']['value']):  # Button held, but now released
        roverActions['pause']['held'] = False
    if (roverActions['pause']['held'] and roverActions['pause']['value'] and (
        datetime.now() - roverActions['pause']['lastpress']).seconds >= actionTime):  # Button held for required time
        roverActions['pause']['lastpress'] = datetime.now()  # Keep updating time as button may continue to be held
        paused = not paused

def checkModes():
    global modeNum, mode, roverActions
    if (not roverActions['mode']['held'] and roverActions['mode']['value']):  # New button press
        roverActions['mode']['held'] = True
        roverActions['mode']['lastpress'] = datetime.now()
    if (roverActions['mode']['held'] and not roverActions['mode']['value']):  # Button held, but now released
        roverActions['mode']['held'] = False
    if (roverActions['mode']['held'] and roverActions['mode']['value'] and (datetime.now() - roverActions['mode'][
        'lastpress']).seconds >= actionTime and not paused):  # Button held for required time
        roverActions['mode']['lastpress'] = datetime.now()  # Keep updating time as button may continue to be held
        modeNum += 1
        if modeNum >= len(modeNames):
            modeNum = 0
        mode = modeNames[modeNum]
        setRoverActions()  # Clear all inputs
        roverActions['mode']['set'] = modeNum
        roverActions['ledMode']['value'] = controls[mode]['ledCode']

def checkButtons(currentJoystick):
    global roverActions
    name = currentJoystick.get_name()
    joyForSet = controls[mode].get(name)  # Get joystick in current set
    if (joyForSet):
        typeForJoy = joyForSet.get('buttons')  # Get joystick control type
        if (typeForJoy):
            buttons = currentJoystick.get_numbuttons()
            for i in range(buttons):
                control_input = typeForJoy.get(i)  # Check if input defined for controller
                if (control_input):
                    val = currentJoystick.get_button(i)  # Read button value, assign to roverActions
                    if (val == 0 and roverActions[control_input[0]]['direction'] == control_input[1]) or val != 0:
                        roverActions[control_input[0]]['value'] = val
                        roverActions[control_input[0]]['direction'] = control_input[1]  # Set direction multiplier

def checkAxes(currentJoystick):
    global roverActions
    name = currentJoystick.get_name()
    joyForSet = controls[mode].get(name)  # Get joystick in current set
    if (joyForSet):
        typeForJoy = joyForSet.get('axes')  # Get joystick control type
        if (typeForJoy):
            axes = currentJoystick.get_numaxes()
            for i in range(axes):
                control_input = typeForJoy.get(i)  # Check if input defined for controller
                if (control_input):
                    val = currentJoystick.get_axis(i)  # Read axis value, assign to roverActions
                    roverActions[control_input[0]]['value'] = val
                    roverActions[control_input[0]]['direction'] = control_input[1]  # Set direction multiplier

def checkHats(currentJoystick):
    global roverActions
    name = currentJoystick.get_name()
    joyForSet = controls[mode].get(name)  # Get joystick in current set
    if (joyForSet):
        typeForJoy = joyForSet.get('hats')  # Get joystick control type
        if (typeForJoy):
            count = currentJoystick.get_numhats()
            for x in range(count):
                val = currentJoystick.get_hat(x)  # Store hat value, needed more than once
                for y in range(len(val)):  # Get the number of controller values
                    # Input may be stored multiple times, check both
                    control_input = typeForJoy.get((x, y))  # Check if east/west defined
                    if (control_input):
                        roverActions[control_input[0]]['value'] = val[y]
                        roverActions[control_input[0]]['direction'] = control_input[1]  # Set direction multiplier


def checkRotate():
    global turnInPlace
    if roverActions['rotate']['value'] !=0:
        turnInPlace = roverActions['rotate']['direction']


def turn(outVal):
    global turnInPlace
    if turnInPlace == 1:
        outVal[0]
        outVal[1] = maxRotateSpeed
    elif turnInPlace == -1:
        outVal[0]
        outVal[1] = -maxRotateSpeed
    turnInPlace = None
    return outVal


def runPwmPi():
    global armAction
    while True:
        GPIO.output(armAction[0]['pwm'], 1)
        sleep(.00038)
        GPIO.output(armAction[0]['pwm'], 0)
        sleep(.00003)

def runPwmTx2(joint):
    global armAction
    while True:
        tx2.output(armAction[joint]['pwm'], 1)
        sleep(armAction[joint]['sleep'])
        tx2.output(armAction[joint]['pwm'], 0)
        #sleep(armAction[joint]['sleep'])

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
    '''
    elif system == 'pi':
        for i in range(1):#len(data)):
            if data[i] != 0:
                GPIO.output(armAction[i]['enab'], 0)
                GPIO.output(armAction[i]['dir'], int(checkArmDirection(data[i])))
            else:
                GPIO.output(armAction[i]['enab'], 1)
    '''


def main(*argv):
    global armIndependent, armAction, arm1, arm2
    startUp(argv)  # Load appropriate controller(s) config file
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        pygame.joystick.Joystick(i).init()

    while True:
        pygame.event.pump()  # Keeps pygame in sync with system, performs internal upkeep
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            print("No joystick attached")
            stop()
            sleep(1)
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            checkAxes(joystick)
            checkHats(joystick)
            checkButtons(joystick)
            throttleStep()
            checkRotate()
            checkPause()
            checkModes()
            checkArmMode()

            if paused:
                outVals = list(map(getZero, actionList))
            else:
                outVals = turn(list(map(computeSpeed, actionList))) # Output string determined by actionList[] order
            outVals = list(map(str, outVals))
            outString = ','.join(outVals)
            print(outString)
            #writeToBus(controls[mode]['ledCode'], controls[mode]['ledCode'])
            #led.update(int(outVals[-1]))
            try:
                wheels.driveBoth(int(outVals[0]), int(outVals[1]))
                if armAttached:
                    #with SMBusWrapper(1) as bus:
                    #for i in range(4):  #To grab current arm values for compare to old in arm2
                        #arm1[i] = int(str(i+1)+str(int(outVals[i+4])+1))
                    #for i in range(4):  #Only write to smbus if change in arm values
                        #if arm1[i] != arm2[i]:
                            #polo.write((str(i+1)+str(int(outVals[i+4])+1)).encode('utf-8'))
                            #pass
                            #bus.write_byte_data(armAddress, 0, int(str(i+1)+str(int(outVals[i+4])+1)))
                        #else:
                            #polo.write(b'a')
                    #arm2[0:4] = arm1[0:4]
                    #moveJoints([int(outVals[4]), int(outVals[5]), int(outVals[6]), int(outVals[7])])
                    if armIndependent:
                        armMix.driveBoth(int(outVals[2]), int(outVals[3]))                        
                    else:
                        armMix.driveBoth(-(int(outVals[3])), int(outVals[3]))            
            except:
                print("Mobility-main-drive error")

if __name__ == '__main__':
    # Only start the threads if the arm is attached
    try:
        if armAttached:
            if system == 'tx2':
                pass
                #p1 = multiprocessing.Process(target=runPwmTx2, args=(0,))
                #p1.start()
                #p2 = multiprocessing.Process(target=runPwmTx2, args=(1,))
                #p2.start()
                #p3 = multiprocessing.Process(target=runPwmTx2, args=(2,))
                #p3.start()
                #p4 = multiprocessing.Process(target=runPwmTx2, args=(3,))
                #p4.start()
            elif system == 'pi':
                pass
                #p1 = multiprocessing.Process(target=runPwmPi)
                #p1.start()

        # Start the main loop
        main()
    except (KeyboardInterrupt, SystemExit):
        #p1.terminate()
        #p2.terminate()
        #p3.terminate()
        #p4.terminate()
        raise


