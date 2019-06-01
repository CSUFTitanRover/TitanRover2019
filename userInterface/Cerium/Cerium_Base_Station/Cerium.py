#!/usr/bin/env python
# coding=utf-8

# David Feinzimer  - dfeinzimer@csu.fullerton.edu
# Anette Ulrichsen - amulrichsen@csu.fullerton.edu

from fake_sensor_test.msg import imu as dev_imu
from fake_sensor_test.msg import gps as dev_gps
from finalimu.msg import fimu as prod_imu
from gnss.msg import gps as prod_gps
from mobility.msg import driver_Status
from pygame.sprite import Sprite
from res.funcs import AppendCardinalInformation
from res.funcs import SafeConnect
from res.funcs import SetModeAndIP
from res.obj.Map import Map
from res.obj.Menu import Menu
from std_msgs.msg import String
import pygame
import res.coords as coords
import res.obj.Text as Text
import res.obj.Image as Image
import res.obj.Menu as Menu
import rospy
import socket
import sqlite3
import sys
import threading

app_title = "Titan Rover - Cerium Base Station"
color_background = (0,0,0)
color_text = (255, 255, 255)
display_image = None
display_LAT_TL = None
display_LON_TL = None
display_LAT_BR = None
display_LON_BR = None
icon_arrow = "res/images/vehicle.png"
icon_ball = "res/images/ball.png"
icon_hint = "res/images/hint.png"
map_width = 1070 # The width of the map area
mode = None
new_destination = ""
new_destination_type = "" # DD | DDM | DMS
new_destination_LatLon = "LAT" # LAT | LON
new_destination_set = [] # A LAT/LON set
roverLat = None
roverLon = None
screen = None
screen_height = 530
screen_width = 1270 # The full window width
socket_TCP_IP = None # Vehicle IP (for socket connection) TODO Give meaningful name
socket_TCP_PORT = 9600
socket_BUFFER_SIZE = 256
status = None # Holds the ROS connection status
vehicle_x = 0 # x offset of vehicle plotted on map
vehicle_y = 0 # y offset of vehicle plotted on map
version = "05.31.2019.21.52"
yaw = 0

def Add_LAT_LON():
    global new_destination
    new_destination = new_destination_LatLon + " "

def Attempt_Coordinate_Send():
    function_name = "Attempt_Coordinate_Send()"
    global new_destination_set
    if len(new_destination_set) == 2:
        print "Attempt_Coordinate_Send(): Ready to send"
        destination = Get_Coordinate_Pair_String()
        print "Get_Coordinate_Pair_String() returned", destination
        if destination == "Invalid":
            print "ERROR", function_name, "INVALID COORDINATES"
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # If connection doesn't pickup within 1 seconds, kill the call
                s.settimeout(1)
                s.connect((socket_TCP_IP, socket_TCP_PORT))
                dest_encoded = destination.encode()
                print "INFO", function_name, "SENDING"
                s.send(dest_encoded)
                s.close()
            except:
                print "ERROR", function_name, "SEND FAILED"

        Clear_Destination_Set()
    else:
        print "Attempt_Coordinate_Send(): Not ready: LAT & LON required"

def Callback_GNSS(data):
    function_name = "Callback_GNSS()"
    global roverLat
    global roverLon
    roverLat = float(data.roverLat)
    roverLon = float(data.roverLon)
    map.GetVehicle().SetLatLon(roverLat, roverLon)

def Callback_IMU(data):
    function_name = "Callback_IMU()"
    global mode
    global yaw
    if mode == "prod":
        yaw = data.yaw.yaw
    elif mode == "dev":
        yaw = data.yaw
    map.GetVehicle().SetYaw(yaw)

# Respond to keypress and mouse events.
def Check_Control_Events(menu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            Check_Keydown_Events(event)
        elif event.type == pygame.KEYUP:
            Check_Keyup_Events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            result = menu.CheckForClickMatch(x, y) # result  = "F#!K" | "STOP" | None
            if result:
                if result == "F#!K":
                    PublishStop("HARD")
                elif result == "STOP":
                    PublishStop("SOFT")

def Check_Keydown_Events(event):
    function_name = "Check_Keydown_Events()"
    global new_destination
    global new_destination_type
    global new_destination_LatLon
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_BACKSPACE:
        if len(new_destination) >= 5:
            new_destination = new_destination[:-1]
            new_destination_type = new_destination_type[:-3]
    elif event.key == pygame.K_PERIOD:
        new_destination += "."
    elif event.key == pygame.K_MINUS:
        new_destination += "-"
    elif event.key == pygame.K_RETURN:
        Process_Destination()
        new_destination_type = ""
    elif event.key == pygame.K_d:
        new_destination += u"\u00B0"
        new_destination_type += "deg"
        print function_name, "new_destination_type:", new_destination_type
    elif event.key == pygame.K_m:
        new_destination += "\'"
        new_destination_type += "min"
        print function_name, "new_destination_type:", new_destination_type
    elif event.key == pygame.K_s:
        new_destination += "\""
        new_destination_type += "sec"
        print function_name, "new_destination_type:", new_destination_type
    elif event.key == pygame.K_0:
        new_destination += "0"
    elif event.key == pygame.K_1:
        new_destination += "1"
    elif event.key == pygame.K_2:
        new_destination += "2"
    elif event.key == pygame.K_3:
        new_destination += "3"
    elif event.key == pygame.K_4:
        new_destination += "4"
    elif event.key == pygame.K_5:
        new_destination += "5"
    elif event.key == pygame.K_6:
        new_destination += "6"
    elif event.key == pygame.K_7:
        new_destination += "7"
    elif event.key == pygame.K_8:
        new_destination += "8"
    elif event.key == pygame.K_9:
        new_destination += "9"
    elif event.key == pygame.K_UP:
        new_destination += " N"
    elif event.key == pygame.K_DOWN:
        new_destination += " S"
    elif event.key == pygame.K_LEFT:
        new_destination += " W"
    elif event.key == pygame.K_RIGHT:
        new_destination += " E"

def Check_Keyup_Events(event):
    pass

def Clear_Destination_Set():
    global new_destination_set
    del new_destination_set[:]
    print "Clear_Destination_Set(): new_destination_set:", new_destination_set

def Convert_Coordinates():
    function_name = "Convert_Coordinates()"
    global new_destination
    global new_destination_type
    print "Convert_Coordinates(): Input Type:  ", new_destination_type
    print "Convert_Coordinates(): Input Value: ", new_destination
    if (new_destination_type == "deg"):
        new_destination_type = "DD Decimal Degrees"
        new_destination = new_destination[:-1]
    elif (new_destination_type == "degmin"):
        d = new_destination.split(u"\u00B0")
        m = d[1]
        card = m.split("\'")
        m = card[0]
        card = card[1]
        d = d[0]
        m = float(m) / 60
        DD = float(d) + m
        new_destination_type = "DD Decimal Degrees"
        new_destination = DD
        if card == "W" or card == "S":
            new_destination = new_destination * -1
    elif (new_destination_type == "degminsec"):
        d = new_destination
        d = d.split(u"\u00B0")
        m = d[1]
        d = d[0]
        m = m.split("\'")
        s = m[1]
        m = m[0]
        card = s.split("\"")
        s = card[0]
        card = card[1]
        DD = float(d) + float(m)/60 + float(s)/3600
        new_destination_type = "DD Decimal Degrees"
        new_destination = DD
        if card == "W" or card == "S":
            new_destination = new_destination * -1
    else:
        new_destination_type = "Invalid"
        new_destination = "Invalid"
    print function_name, "Output Type:", new_destination_type
    print function_name, "Output Value:", new_destination

def Flip_LAT_LON():
    global new_destination_LatLon
    if new_destination_LatLon == "LAT":
        new_destination_LatLon = "LON"
        print("Flip_LAT_LON(): new_destination_LatLon set to LON")
    else:
        new_destination_LatLon = "LAT"
        print("Flip_LAT_LON(): new_destination_LatLon set to LAT")

def Get_Coordinate_Pair_String():
    function_name = "Get_Coordinate_Pair_String()"
    global map
    global new_destination_set
    if new_destination_set[0] == "Invalid" or new_destination_set[1] == "Invalid":
        return "Invalid"
    else:
        candidate = str(new_destination_set[0])+" "+str(new_destination_set[1])+" "+"HINT"
        result = map.AddLandmark(new_destination_set[0], new_destination_set[1], "HINT", icon_hint, screen)
        print "RESULT", result
    print function_name, "candidate:", candidate
    return candidate

# Application entry point
def Launch_Application():
    func_name = "Launch_Application()"
    global map
    global mode
    global new_destination
    global new_destination_LatLon
    global roverLat
    global roverLon
    global screen
    global status
    global yaw
    instance_config = SetModeAndIP.SetModeAndIP()
    mode = instance_config[0]
    socket_TCP_IP = instance_config[1]
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(app_title + ' - ' + version)
    Set_Application_Icon()
    # Attempt to connect to roscore
    status = SafeConnect.SafeConnect()
    # Subscribe to imu and gnss topics
    IMU_SUBSCRIBTION = threading.Thread(target=Subscribe_To_IMU,args=(mode,))
    IMU_SUBSCRIBTION.start()
    GNSS_SUBSCRIBTION = threading.Thread(target=Subscribe_To_GNSS,args=(mode,))
    GNSS_SUBSCRIBTION.start()
    map = Map(screen,screen_height,map_width)
    menu = Menu.Menu(screen, map_width, app_title)
    new_destination = new_destination_LatLon + " "
    while True:
        screen.fill(color_background)
        Check_Control_Events(menu)
        map.blitme(roverLat, roverLon)
        menu.blitme(yaw, new_destination)
        pygame.display.flip()

# Re-append LAT/LON
def Process_Destination():
    global new_destination
    global new_destination_type
    Remove_LAT_LON() # Strip away LAT/LON for conversion and add it back later
    Convert_Coordinates() # Convert any format into decimal degrees
    Queue_Coordinate() # Put this latest coordinate into temporary storage
    Attempt_Coordinate_Send() # Try to send the coordinates to vehicle
    Flip_LAT_LON() # Flip LAT for LON or vice versa
    Add_LAT_LON()

def PublishStop(level): # param = "HARD" | "SOFT"
    function_name = "PublishStop("+level+")"
    pub = rospy.Publisher("driver_Status", driver_Status, queue_size=10)
    pub.publish(autoActive=False)


def Queue_Coordinate():
    global new_destination
    global new_destination_set
    new_destination_set.append(new_destination)
    print "Queue_Coordinate(): new_destination_set: ",new_destination_set

def Remove_LAT_LON():
    global new_destination
    new_destination = new_destination.split(" ")
    if len(new_destination) == 3: # Type was dm or dms
        new_destination = new_destination[1] + new_destination[2]
    if len(new_destination) == 2: # Type was dd
        new_destination = new_destination[1]

def Set_Application_Icon():
    function_name = "Set_Application_Icon()"
    try:
        icon = pygame.image.load(icon_arrow)
        pygame.display.set_icon(icon)
    except:
        print "ERROR",function_name,"Cannot set application icon"

def Subscribe_To_GNSS(mode):
    function_name = "Subscribe_To_GNSS("+mode+")"
    if mode == "prod":
        try:
            rospy.Subscriber("gnss", prod_gps, Callback_GNSS)
        except:
            print function_name, "SUBSCRIPTION FAILURE"
    elif mode == "dev":
        try:
            rospy.Subscriber("gnss", dev_gps, Callback_GNSS)
        except:
            print function_name, "SUBSCRIPTION FAILURE"

def Subscribe_To_IMU(mode):
    function_name = "Subscribe_To_IMU("+mode+")"
    if mode == "prod":
        try:
            rospy.Subscriber("imu", prod_imu, Callback_IMU)
        except:
            print function_name, "prod SUBSCRIPTION FAILURE"
    elif mode == "dev":
        try:
            rospy.Subscriber("imu", dev_imu, Callback_IMU)
        except:
            print function_name, "dev SUBSCRIPTION FAILURE"

Launch_Application()
