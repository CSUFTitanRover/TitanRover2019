# David Feinzimer
# dfeinzimer@csu.fullerton.edu


from finalimu.msg import fimu
from pygame.sprite import Sprite
from std_msgs.msg import String
import pygame
import rospy
import sqlite3
import sys


color_background = (0,0,0)
color_text = (255, 255, 255)
mode = "dev"                   # dev | prod
screen_height = 500
screen_width = 500
version = "3.10.19.23.00.00"
yaw = 0
new_destination = ""           # Numeric
new_destination_type = ""      # DD | DDM | DMS
new_destination_LatLon = ""    # LAT | LON


# Object for displaying the heading arrow in the middle of the screen
class Nav_Arrow(Sprite):
    global yaw
    def __init__(self, screen):
        super(Nav_Arrow, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/icon.png')
        self.rect = self.image.get_rect()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
    def blitme(self):
        rect = self.image.get_rect()
        image = self.image
        if (mode == "prod"):
            image = pygame.transform.rotate(image, yaw * -1)
        if (mode == "dev"):
            image = pygame.transform.rotate(image, float(yaw) * -1)
        rect = image.get_rect(center=rect.center)
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.rect.centerx = 300
        self.rect.centery = 300
        self.screen.blit(image, rect)


# Object for displaying new destination entry at the bottom of the screen
class Nav_Destination():
    global new_destination
    def blitme(self):
        self.update()
        self.screen.blit(self.high_score_image, self.high_score_rect)
    def update(self):
        high_score = float(yaw)
        high_score_str = "{:,}".format(high_score)
        high_score_str = new_destination
        self.high_score_image = self.font.render(high_score_str, True, 
                                self.color_text, color_background)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.bottom = self.screen_rect.bottom
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color_text = color_text
        self.font = pygame.font.SysFont(None, 48)
        self.update()


# Object for displaying current heading at the top of the screen
class Nav_Text():
    def blitme(self):
        self.update()
        self.screen.blit(self.high_score_image, self.high_score_rect)
    def update(self):
        high_score = float(yaw)
        high_score_str = "{:,}".format(high_score)
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


def run():
    pygame.init()
    listener() # Start listening to ROS
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Titan Rover - Heading - ' + version)
    nav_arrow = Nav_Arrow(screen)
    nav_destination = Nav_Destination(screen)
    nav_text = Nav_Text(screen)
    while True:
        screen.fill(color_background)
        check_control_events()
        nav_arrow.blitme()
        nav_destination.blitme()
        nav_text.blitme()
        pygame.display.flip()


def callback(data):
    global yaw
    if (mode == "prod"):
        yaw = data.yaw.yaw
        #print("callback(): [PROD]: ", yaw)
    if (mode == "dev"):
        yaw = data.data
        #print("callback(): [DEV]: ", yaw)


# Respond to keypress and mouse events.
def check_control_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()


def check_keydown_events(event):
    global new_destination
    global new_destination_type
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_BACKSPACE:
        new_destination = new_destination[:-1]
        new_destination_type = new_destination_type[:-3]
    elif event.key == pygame.K_PERIOD:
        new_destination += "."
    elif event.key == pygame.K_MINUS:
        new_destination += "-"
    elif event.key == pygame.K_RETURN:
        process_destination()
        new_destination = ""
        new_destination_type = ""
        new_destination_LatLon = ""
    elif event.key == pygame.K_d:
        new_destination += "°"
        new_destination_type += "deg"
    elif event.key == pygame.K_m:
        new_destination += "\'"
        new_destination_type += "min"
    elif event.key == pygame.K_s:
        new_destination += "\""
        new_destination_type += "sec"   
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


def check_keyup_events(event):
    pass


def listener():
    status = rospy.init_node('listener', anonymous=True)
    print("listener(): ROS Status:", status)
    if mode == "prod":
        rospy.Subscriber("imu", fimu, callback)
    elif mode == "dev":
        rospy.Subscriber("chatter", String, callback)


def process_destination():
    global new_destination
    global new_destination_type
    print("process_destination(): Input Type: ", new_destination_type)
    print("process_destination(): Input Value:", new_destination)
    if (new_destination_type == "deg"):
        new_destination_type = "DD Decimal Degrees"
    elif (new_destination_type == "degmin"):
        d = new_destination.split("°")
        m = d[1]
        d = d[0]
        m = m[:-1]
        m = float(m) / 60
        DD = float(d) + m
        new_destination_type = "DD Decimal Degrees"
        new_destination = DD
    elif (new_destination_type == "degminsec"):
        d = new_destination
        d = d.split("°")
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
    print("process_destination(): Output Type: ", new_destination_type)
    print("process_destination(): Output Value:", new_destination)


run()
