import pygame
import res.obj.Text as Text

class MenuButton():
    def __init__(self, screen, color, bound_left, bound_top, width, height, message):
        self.bound_left = bound_left
        self.bound_top = bound_top
        self.color = color
        self.height = height
        self.message = message = message
        self.screen = screen
        self.text = Text.Text(self.screen, self.message, (0,0,0), (0,0,0,color),20,self.bound_left+10,None,self.bound_top+10,None)
        self.width = width
    def blitme(self):
        rect = pygame.Rect(self.bound_left, self.bound_top, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rect, 0)
        self.text.blitme(self.message)
