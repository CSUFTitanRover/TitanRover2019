import pygame
import res.obj.MenuButton as MenuButton
import res.obj.Text as Text

color_background = (0,0,0)
color_text = (255, 255, 255)

class Menu():
    # start_x = The x value that no objects should appear to the left of
    def __init__(self, screen, start_x):
        self.screen = screen
        self.start_x = start_x # No objects appear to the left of this
        self.build_buttons()
        self.build_info_displays()
    def blitme(self, yaw):
        self.fuck_button.blitme()
        self.nav_text.blitme(yaw)
        self.stop_button.blitme()
    def build_buttons(self):
        self.fuck_button = MenuButton.MenuButton(self.screen,(255,0,0), self.start_x+100, 480, 100, 50, "FUCK")
        self.stop_button = MenuButton.MenuButton(self.screen,(255,255,0), self.start_x, 480, 100, 50, "STOP")
    def build_info_displays(self): # Things that display values
        self.nav_text = Text.YawText(self.screen,str(0),color_text,color_background,20,self.start_x,None,self.screen.get_rect().top,None) # Shows the yaw value
