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
    def blitme(self):
        Calculate_Landmark_X_Y()
        image = self.image
        image = pygame.transform.rotate(image, yaw * -1)
        rect = image.get_rect(center=self.rect.center)
        self.rect.centerx = vehicle_x
        self.rect.centery = vehicle_y
        self.screen.blit(image, rect)
    def Calculate_Landmark_X_Y():
        function_name = "Calculate_Landmark_X_Y()"
        if((self.lat != None) and (self.lon != None)):
            self.x = (screen_width  / abs(display_LON_TL-display_LON_BR))
            self.y = (screen_height / abs(display_LAT_TL-display_LAT_BR))
            self.x = self.x * (self.lon-display_LON_TL)
            self.y = self.y * (self.lat-display_LAT_TL) * -1
        else:
            print function_name,"ERROR: lat and/or lon empty"
        print function_name,"landmark lat/lon:",self.lat,self.lon
        print function_name,"landmarl x/y:",self.x,self.y
