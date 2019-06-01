import pygame
import res.obj.MenuButton as MenuButton
import res.obj.Text as Text

color_background = (0,0,0)
color_text = (255, 255, 255)

class Menu():
    # start_x = The x value that no objects should appear to the left of
    def __init__(self, screen, start_x):
        self.yaw_title_str = "Current Yaw:"
        self.new_hint_title_str = "Add new hint:"
        self.screen = screen
        self.start_x = start_x # No objects appear to the left of this
        self.buttons = self.build_buttons()
        self.build_info_displays()
    def blitme(self, yaw, new_destination):
        self.yaw_text.blitme(yaw)
        self.new_hint.blitme(new_destination)
        self.yaw_title.blitme(self.yaw_title_str)
        self.new_hint_title.blitme(self.new_hint_title_str)
        for button in self.buttons:
            button.blitme()
    def build_buttons(self):
        buttons = []
        self.add_ball_button = MenuButton.MenuButton(self.screen,(0,255, 0), self.start_x, 240, 200, 50, "+ BALL")
        buttons.append(self.add_ball_button)
        self.estop_button = MenuButton.MenuButton(self.screen,(255, 0, 0), self.start_x+100, 480, 100, 50, "E-STOP")
        buttons.append(self.estop_button)
        self.stop_button = MenuButton.MenuButton(self.screen,(255, 255, 0), self.start_x, 480, 100, 50, "STOP")
        buttons.append(self.stop_button)
        return buttons
    def build_info_displays(self): # Things that display values
        self.new_hint = Text.Text(self.screen,"",color_text,color_background,20,self.start_x,None,450,None)
        self.yaw_text = Text.YawText(self.screen,str(0),color_text,color_background,20,self.start_x,None,self.screen.get_rect().top+75,None) # Shows the yaw value
        self.yaw_title = Text.Text(self.screen,self.yaw_title_str,color_text,color_background,15,self.start_x,None,self.screen.get_rect().top+50,None)
        self.new_hint_title = Text.Text(self.screen,self.new_hint_title_str,color_text,color_background,15,self.start_x,None,self.screen.get_rect().top+425,None)
    def CheckForClickMatch(self, x, y):
        for button in self.buttons:
            result = button.ValidateClick(x, y)
            if result: return result
