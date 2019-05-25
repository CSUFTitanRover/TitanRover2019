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
        self.type = type # BALL | HINT
    def blitme(self):
        Calculate_Landmark_X_Y()
        image = self.image
        image = pygame.transform.rotate(image, yaw * -1)
        rect = image.get_rect(center=self.rect.center)
        self.rect.centerx = vehicle_x
        self.rect.centery = vehicle_y
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.screen.blit(image, rect)
    def Calculate_Landmark_X_Y():
        function_name = "Calculate_Landmark_X_Y()"
        if((roverLon != None) and (roverLat != None)):
            vehicle_x = (screen_width  / abs(display_LON_TL-display_LON_BR))
            vehicle_y = (screen_height / abs(display_LAT_TL-display_LAT_BR))
            vehicle_x = vehicle_x * (roverLon-display_LON_TL)
            vehicle_y = vehicle_y * (roverLat-display_LAT_TL) * -1
        else:
            print function_name,"roverLon and/or roverLat empty"
        print function_name,"Vehicle is at:",roverLat,roverLon
        print function_name,"Plot vehicle at:",vehicle_x,vehicle_y
