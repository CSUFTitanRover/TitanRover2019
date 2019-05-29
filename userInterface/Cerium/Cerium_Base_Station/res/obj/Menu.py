import pygame
import res.obj.MenuButton as MenuButton

class Menu():
    # start_x = The x value that no objects should appear to the left of
    def __init__(self, screen, start_x):
        self.screen = screen
        self.start_x = start_x # No objects appear to the left of this
        self.build_buttons()
    def blitme(self):
        self.fuck_button.blitme()
        self.stop_button.blitme()
    def build_buttons(self):
        self.fuck_button = MenuButton.MenuButton(self.screen,(255,0,0), self.start_x+100, 480, 100, 50, "FUCK")
        self.stop_button = MenuButton.MenuButton(self.screen,(255,255,0), self.start_x, 480, 100, 50, "STOP")
