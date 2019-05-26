from Landmark import Landmark

class LandmarkManager(object):
    def __init__(self):
        self.landmarks = []
    def Add_Landmark(self,lat,lon,type,image,screen):
        landmark = Landmark(lat,lon,len(self.landmarks),type,image,screen)
        self.landmarks.append(landmark)
    def Blit_Landmarks(self,screen_width,screen_height,display_LAT_TL,display_LON_TL,display_LAT_BR,display_LON_BR):
        for x in range(0, len(self.landmarks)):
            self.landmarks[x].blitme(screen_width,screen_height,display_LAT_TL,display_LON_TL,display_LAT_BR,display_LON_BR)
    def Get_Landmarks(self):
        return self.landmarks
