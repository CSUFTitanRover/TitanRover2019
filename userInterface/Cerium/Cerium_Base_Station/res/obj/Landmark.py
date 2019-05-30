import pygame

class Landmark(object):
    def __init__(self,lat,lon,id,type,image,screen):
        super(Landmark, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.lat = lat
        self.lon = lon
        self.id = id # int, auto assigned
        self.type = type # BALL | HINT | VEHICLE
        self.x = None # x coordinate (for blitting)
        self.y = None # y coordinate (for blitting)
        self.yaw = 0 # Used for landmarks of type VEHICLE
    def blitme(self):
        self.image = pygame.transform.rotate(self.image, self.yaw * -1)
        self.rect = image.get_rect(center=self.rect.center)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.screen.blit(self.image, self.rect)
    def GetLatLon(self):
        return self.lat, self.lon
    def GetXY(self):
        return self.x, self.y
    def SetLatLon(lat, lon):
        self.lat = lat
        self.lon = lon
    def SetXY(x, y):
        self.x = x
        self.y = y
