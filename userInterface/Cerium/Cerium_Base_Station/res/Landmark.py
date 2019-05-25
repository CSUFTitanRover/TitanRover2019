import pygame

class Landmark(object):
    def __init__(self,lat,lon,id,type,image,screen):
        super(Landmark, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.lat = lat
        self.lon = lon
        self.id = id
        self.type = type # BALL | HINT | VEHICLE
        self.x = None
        self.y = None
        self.yaw = 0
    def blitme(self,screen_width,screen_height,display_LAT_TL,display_LON_TL,display_LAT_BR,display_LON_BR):
        self.Calculate_Landmark_X_Y(screen_width,screen_height,display_LAT_TL,display_LON_TL,display_LAT_BR,display_LON_BR)
        image = self.image
        image = pygame.transform.rotate(image, self.yaw * -1)
        rect = image.get_rect(center=self.rect.center)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.screen.blit(image, rect)
    def Calculate_Landmark_X_Y(self,screen_width,screen_height,display_LAT_TL,display_LON_TL,display_LAT_BR,display_LON_BR):
        function_name = "Calculate_Landmark_X_Y()"
        if((self.lat != None) and (self.lon != None)):
            self.x = (screen_width  / abs(display_LON_TL-display_LON_BR))
            self.y = (screen_height / abs(display_LAT_TL-display_LAT_BR))
            self.x = self.x * (self.lon-display_LON_TL)
            self.y = self.y * (self.lat-display_LAT_TL) * -1
        else:
            print function_name,"ERROR: lat and/or lon empty"
