import pygame

class Image():
    def __init__(self, screen, image):
        self.screen = screen
        self.image = pygame.image.load('res/images/'+image+'.png')
        self.rect = self.image.get_rect()
    def blitme(self):
        self.screen.blit(self.image, self.rect)
