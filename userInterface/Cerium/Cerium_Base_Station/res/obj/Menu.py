# coding=utf-8

import pygame

class Menu():
    def blitme(self):
        self.update()
        #self.screen.blit()
    def update(self):
        pass
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
