import Landmark

class LandmarkManager(object):
    def __init__(self):
        self.landmarks = []
    def Get_Landmarks(self):
        return self.landmarks
    def Add_Landmark(self,lat,lon,type):
        landmark = Landmark(lat,lon,len(self.landmarks),type)
        self.landmarks.append(landmark)
