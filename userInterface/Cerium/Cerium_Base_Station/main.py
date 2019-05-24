#!/usr/bin/env python

# David Feinzimer  - dfeinzimer@csu.fullerton.edu
# Anette Ulrichsen - amulrichsen@csu.fullerton.edu

from finalimu.msg import fimu
from gnss.msg import gps
from fake_sensor_test.msg import imu
from pygame.sprite import Sprite
from std_msgs.msg import String
import conf.coords as coords
import pygame
import rospy
import socket
import sqlite3
import sys

color_background = (0,0,0)
color_text = (255, 255, 255)
display_image = None
display_LAT_TL = None
display_LON_TL = None
display_LAT_BR = None
display_LON_BR = None
icon_arrow = "images/icon2.png"
mode = "dev"                        # dev | prod
new_destination = ""
new_destination_type = ""           # DD | DDM | DMS
new_destination_LatLon = "LAT"      # LAT | LON
new_destination_set = []            # A LAT/LON set
roverLat = None
roverLon = None
screen_height = 530
screen_width = 1070
socket_TCP_IP = '192.168.1.237'
socket_TCP_PORT = 9600
socket_BUFFER_SIZE = 256
socket_message = "SOCKET TEST"
vehicle_x = 0                       # x offset of vehicle plotted on map
vehicle_y = 0                       # y offset of vehicle plotted on map
version = "05.23.2019.18.55"
yaw = 0

# Object for displaying the heading arrow on the map.
class Nav_Arrow(Sprite):
    global yaw
    global vehicle_x
    global vehicle_y
    def __init__(self, screen):
        super(Nav_Arrow, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(icon_arrow)
        self.rect = self.image.get_rect()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
    def blitme(self):
        image = self.image
        if mode == "prod":
            image = pygame.transform.rotate(image, yaw * -1)
        if mode == "dev":
            image = pygame.transform.rotate(image, float(yaw) * -1)
        rect = image.get_rect(center=self.rect.center)
        self.rect.centerx = vehicle_x
        self.rect.centery = vehicle_y
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.screen.blit(image, rect)

# Object for displaying the map.
class Nav_Background_Image(Sprite):
    def __init__(self, screen):
        super(Nav_Background_Image, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/'+display_image+'.png')
        self.rect = self.image.get_rect()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
    def blitme(self):
        image = pygame.image.load('images/'+display_image+'.png')
        rect = self.image.get_rect()
        rect = image.get_rect(center=rect.center)
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.rect.centerx = 0
        self.rect.centery = 0
        self.screen.blit(image, rect)

# Object for displaying the new destination coordinates users can type into
# at the bottom of the screen.
class Nav_Destination():
    global new_destination
    def blitme(self):
        self.update()
        self.screen.blit(self.high_score_image, self.high_score_rect)
    def update(self):
        high_score_str = new_destination
        self.high_score_image = self.font.render(high_score_str,
                                True, self.color_text, color_background)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.bottom = self.screen_rect.bottom
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color_text = color_text
        self.font = pygame.font.SysFont(None, 48)
        self.update()

# Object for displaying rover's current heading at the top of the screen.
class Nav_Text():
    def blitme(self):
        self.update()
        self.screen.blit(self.high_score_image, self.high_score_rect)
    def update(self):
        high_score = float(yaw)
        high_score_str = "{:,}".format(high_score)
        high_score_str = Append_Cardinal_Information(high_score_str)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.color_text, color_background)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.high_score_rect.top
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color_text = color_text
        self.font = pygame.font.SysFont(None, 48)
        self.update()

def Add_LAT_LON():
    global new_destination
    #new_destination = new_destination_LatLon + " "
    new_destination = new_destination_LatLon + " "

# Takes numerical vehicle heading value and appends a degree symbol and a
# a cardinal direction abbreviation.
def Append_Cardinal_Information(data):
    function_name = "Append_Cardinal_Information()"
    numerical_data = float(data)
    data = data + "* "
    if(numerical_data > 270):
        data = data + "NW"
    elif(numerical_data == 270):
        data = data + "W"
    elif(numerical_data > 180):
        data = data + "SW"
    elif(numerical_data == 180):
        data = data + "S"
    elif(numerical_data > 90):
        data = data + "SE"
    elif(numerical_data == 90):
        data = data + "E"
    elif(numerical_data > 0):
        data = data + "NE"
    elif(numerical_data == 0):
        data = data + "N"
    return data

def Attempt_Coordinate_Send():
    global new_destination_set
    if len(new_destination_set) == 2:
        print("Attempt_Coordinate_Send(): Ready to send")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket_TCP_IP, socket_TCP_PORT))
        destination = Get_Coordinate_Pair_String()
        dest_encoded = destination.encode()
        print("Attempt_Coordinate_Send(): Sending: ",dest_encoded)
        s.send(dest_encoded)
        s.close()
        Clear_Destination_Set()
    else:
        print("Attempt_Coordinate_Send(): Not ready: LAT & LON required")

# Determines which map tile to display
def Calculate_Display():
    function_name = "Calculate_Display()"
    global roverLat
    global roverLon
    result = "_"
    for x in coords.coords_list:
        if (roverLat <= coords.coords_data[x+"_TL_LAT"] and
            roverLat >= coords.coords_data[x+"_BR_LAT"]):
            if (roverLon <= coords.coords_data[x+"_BR_LON"] and
                roverLon >= coords.coords_data[x+"_TL_LON"]):
                result = x
                print function_name,"ANSWER",result
                Set_Display_Data(result)
                return

def Calculate_Vehicle_X_Y():
    function_name = "Calculate_Vehicle_X_Y()"
    global roverLat
    global roverLon
    global vehicle_x
    global vehicle_y
    global screen_height
    global screen_width
    global display_LAT_TL
    global display_LON_TL
    global display_LAT_BR
    global display_LON_BR
    if((roverLon != None) and (roverLat != None)):
        vehicle_x = (screen_width  / abs(display_LON_TL-display_LON_BR))
        vehicle_y = (screen_height / abs(display_LAT_TL-display_LAT_BR))
        vehicle_x = vehicle_x * (roverLon-display_LON_TL)
        vehicle_y = vehicle_y * (roverLat-display_LAT_TL) * -1
    else:
        print function_name,"roverLon and/or roverLat empty"
    print function_name,"Vehicle is at:",roverLat,roverLon
    print function_name,"Plot vehicle at:",vehicle_x,vehicle_y

def Callback_GNSS(data):
    function_name = "Callback_GNSS()\t"
    global roverLat
    global roverLon
    if mode == "prod":
        roverLat = float(data.roverLat)
        roverLon = float(data.roverLon)
        print function_name,"\tMODE",mode,"\tGNSS TRUE\t",roverLat,roverLon
    if mode == "dev":
        roverLat = float(data.roverLat)
        roverLon = float(data.roverLon)
        print function_name,"\tMODE",mode,"\tGNSS SIMULATED\t\t",roverLat,roverLon
    Calculate_Vehicle_X_Y()

def Callback_IMU(data):
    function_name = "Callback_IMU()\t"
    global yaw
    if mode == "prod":
        yaw = data.yaw.yaw
        print function_name,"\tMODE",mode,"\tHEADING TRUE\t",yaw
    if mode == "dev":
        yaw = data.yaw
        print function_name,"\tMODE",mode,"\tHEADING SIMULATED\t",yaw

# Respond to keypress and mouse events.
def Check_Control_Events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            Check_Keydown_Events(event)
        elif event.type == pygame.KEYUP:
            Check_Keyup_Events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

def Check_Keydown_Events(event):
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
        new_destination += "*"
        new_destination_type += "deg"
        print("Check_Keydown_Events(): new_destination_type: ",
              new_destination_type)
    elif event.key == pygame.K_m:
        new_destination += "\'"
        new_destination_type += "min"
        print("Check_Keydown_Events(): new_destination_type: ",
              new_destination_type)
    elif event.key == pygame.K_s:
        new_destination += "\""
        new_destination_type += "sec"
        print("Check_Keydown_Events(): new_destination_type: ",
              new_destination_type)
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

def Check_Keyup_Events(event):
    pass

def Clear_Destination_Set():
    global new_destination_set
    del new_destination_set[:]
    print("Clear_Destination_Set(): new_destination_set: ",new_destination_set)

def Convert_Coordinates():
    global new_destination
    global new_destination_type
    print("Convert_Coordinates(): Input Type:  ", new_destination_type)
    print("Convert_Coordinates(): Input Value: ", new_destination)
    if (new_destination_type == "deg"):
        new_destination_type = "DD Decimal Degrees"
    elif (new_destination_type == "degmin"):
        d = new_destination.split("*")
        m = d[1]
        d = d[0]
        m = m[:-1]
        m = float(m) / 60
        DD = float(d) + m
        new_destination_type = "DD Decimal Degrees"
        new_destination = DD
    elif (new_destination_type == "degminsec"):
        d = new_destination
        d = d.split("*")
        m = d[1]
        d = d[0]
        m = m.split("\'")
        s = m[1]
        s = s[:-1]
        m = m[0]
        DD = float(d) + float(m)/60 + float(s)/3600
        new_destination_type = "DD Decimal Degrees"
        new_destination = DD
    else:
        new_destination_type = "Invalid"
        new_destination = "Invalid"
    print("Convert_Coordinates(): Output Type:  ", new_destination_type)
    print("Convert_Coordinates(): Output Value: ", new_destination)

def Flip_LAT_LON():
    global new_destination_LatLon
    if new_destination_LatLon == "LAT":
        new_destination_LatLon = "LON"
        print("Flip_LAT_LON(): new_destination_LatLon set to LON")
    else:
        new_destination_LatLon = "LAT"
        print("Flip_LAT_LON(): new_destination_LatLon set to LAT")

def Get_Coordinate_Pair_String():
    global new_destination_set
    candidate = str(new_destination_set[0])+" "+str(new_destination_set[1])+" "+"HINT"
    print("Get_Coordinate_Pair_String(): candidate: ",candidate)
    return candidate

# Application entry point
def Launch_Application():
    Set_Display_Data("A")
    func_name = "Launch_Application()\t"
    global new_destination
    global new_destination_LatLon
    pygame.init()
    status = rospy.init_node('listener', anonymous=True)
    print func_name, "ROS Status:", status
    Subscribe_To_IMU() # Start listening to ROS
    Subscribe_To_GNSS() # Start listening to ROS
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Titan Rover - Cerium Base - ' + version)
    nav_arrow = Nav_Arrow(screen)
    nav_destination = Nav_Destination(screen)
    nav_bkgd = Nav_Background_Image(screen)
    nav_text = Nav_Text(screen)
    new_destination = new_destination_LatLon + " "
    while True:
        screen.fill(color_background)
        Check_Control_Events()
        Calculate_Display()
        nav_bkgd.blitme()
        nav_arrow.blitme()
        nav_destination.blitme()
        nav_text.blitme()
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

def Queue_Coordinate():
    global new_destination
    global new_destination_set
    new_destination_set.append(new_destination)
    print("Queue_Coordinate(): new_destination_set: ",new_destination_set)

def Remove_LAT_LON():
    global new_destination
    new_destination = new_destination.split(" ")
    new_destination = new_destination[1]
    print("Remove_LAT_LON(): new_destination: ",new_destination)

def Set_Display_Data(ID):
    global display_image
    global display_LAT_TL
    global display_LON_TL
    global display_LAT_BR
    global display_LON_BR
    TL_LAT = ID + "_TL_LAT"
    TL_LON = ID + "_TL_LON"
    BR_LAT = ID + "_BR_LAT"
    BR_LON = ID + "_BR_LON"
    display_image = ID
    display_LAT_TL = coords.coords_data[TL_LAT]
    display_LON_TL = coords.coords_data[TL_LON]
    display_LAT_BR = coords.coords_data[BR_LAT]
    display_LON_BR = coords.coords_data[BR_LON]

def Subscribe_To_GNSS():
    function_name = "Subscribe_To_GNSS()\t"
    connection_status = False
    if mode == "prod":
        connection_status = rospy.Subscriber("gnss", gps, Callback_GNSS)
    elif mode == "dev":
        connection_status = rospy.Subscriber("gnss", gps, Callback_GNSS)
    if connection_status == False:
        print function_name,"SUBSCRIPTION FAILURE"
    else:
        print function_name,"SUBSCRIPTION SUCCESS"

def Subscribe_To_IMU():
    function_name = "Subscribe_To_IMU()\t"
    connection_status = False
    if mode == "prod":
        connection_status = rospy.Subscriber("imu", fimu, Callback_IMU)
    elif mode == "dev":
        connection_status = rospy.Subscriber("imu", imu, Callback_IMU)
    if connection_status == False:
        print function_name,"SUBSCRIPTION FAILURE"
    else:
        print function_name,"SUBSCRIPTION SUCCESS"

Launch_Application()
