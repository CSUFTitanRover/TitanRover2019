from finalimu.msg import fimu
from pygame.sprite import Sprite
from std_msgs.msg import String
import pygame
import rospy
import sys


color_background = (0,0,0)
color_text = (255, 255, 255)
mode = "dev" # "dev" \\ "prod"
screen_height = 500
screen_width = 500
version = "3.3.19.01.17.30"
yaw = 0
new_destination = ""


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


class Nav_Text():

    def blitme(self):
        self.update()
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def update(self):
        high_score = float(yaw)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.color_text, color_background)
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
    nav_text = Nav_Text(screen)
    nav_arrow = Nav_Arrow(screen)
    while True:
        screen.fill(color_background)
        check_control_events()
        nav_text.blitme()
        nav_arrow.blitme()
        pygame.display.flip()


def callback(data):
    global yaw

    if (mode == "prod"):
        yaw = data.yaw.yaw
        #print("callback(): [PROD]: ", yaw)

    if (mode == "dev"):
        yaw = data.data
        print("callback(): [DEV]: ", yaw)


def check_control_events():
    # Respond to keypress and mouse events.
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
    if event.key == pygame.K_q:
        sys.exit()
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
    elif event.key == pygame.K_PERIOD:
        new_destination += "."
    elif event.key == pygame.K_RETURN:
        print("Added destination:", new_destination)
        new_destination = ""



def check_keyup_events(event):
    pass


def listener():

    status = rospy.init_node('listener', anonymous=True)
    print("Status", status)

    if mode == "prod":
        rospy.Subscriber("imu", fimu, callback)

    elif mode == "dev":
        rospy.Subscriber("chatter", String, callback)


run()
