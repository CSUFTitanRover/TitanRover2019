import pygame

class Landmark(object):
    def __init__(self,lat,lon,id,type,image,screen):
        super(Landmark, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.lat = lat
        self.lon = lon
        self.id = id
        self.x = None
        self.y = None
        self.type = type
