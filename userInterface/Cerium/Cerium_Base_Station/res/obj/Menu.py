import pygame
import res.obj.MenuButton as MenuButton
import res.obj.Text as Text

color_background = (0,0,0)
color_text = (255, 255, 255)

class Menu():
    # start_x = The x value that no objects should appear to the left of
    def __init__(self, screen, start_x, app_title):
        self.app_title_str = app_title
        self.screen = screen
        self.start_x = start_x # No objects appear to the left of this
        self.buttons = self.build_buttons()
        self.build_info_displays()
    def blitme(self, yaw, new_destination):
        self.app_title.blitme(self.app_title_str)
        self.nav_text.blitme(yaw)
        self.nav_destination.blitme(new_destination)
        for button in self.buttons:
            button.blitme()
    def build_buttons(self):
        buttons = []
        self.fuck_button = MenuButton.MenuButton(self.screen,(255,0,0), self.start_x+100, 480, 100, 50, "F#!K")
        self.stop_button = MenuButton.MenuButton(self.screen,(255,255,0), self.start_x, 480, 100, 50, "STOP")
        buttons.append(self.fuck_button)
        buttons.append(self.stop_button)
        return buttons
    def build_info_displays(self): # Things that display values
        self.nav_destination = Text.Text(self.screen,"",color_text,color_background,20,self.start_x,None,450,None)
        self.nav_text = Text.YawText(self.screen,str(0),color_text,color_background,20,self.start_x,None,self.screen.get_rect().top+50,None) # Shows the yaw value
        self.app_title = Text.Text(self.screen,self.app_title_str,color_text,color_background,12,self.start_x,None,self.screen.get_rect().top,None)
    def CheckForClickMatch(self, x, y):
        for button in self.buttons:
            result = button.ValidateClick(x, y)
            if result: return result
