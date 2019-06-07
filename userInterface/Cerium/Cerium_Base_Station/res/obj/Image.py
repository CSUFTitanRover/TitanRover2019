import pygame

class Image():
    def __init__(self, screen, image):
        self.screen = screen
        if image != None:
            self.image = pygame.image.load('res/images/'+image+'.png')
        else:
            self.image = pygame.image.load('res/images/error.png')
            print "ERROR: Requested image was None"
        self.rect = self.image.get_rect()
    def blitme(self):
        self.screen.blit(self.image, self.rect)
