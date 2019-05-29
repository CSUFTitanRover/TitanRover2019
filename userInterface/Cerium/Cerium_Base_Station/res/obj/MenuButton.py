import pygame

class MenuButton():
    def __init__(self, screen, color, bound_left, bound_top):
        self.bound_left = bound_left
        self.bound_top = bound_top
        self.color = color
        self.screen = screen
    def blitme(self):
        rect = pygame.Rect(self.bound_left, self.bound_top, 50, 50)
        pygame.draw.rect(self.screen, self.color, rect, 0)
