class LandmarkManager(object):
    def __init__(self):
        self.landmarks = []
    def Get_Landmarks(self):
        return self.landmarks
    def Add_Landmark(self,LAT,LON,TYPE):
        landmark = {
            "LAT":"E-21",
            "LON":"Campus Drive",
            "ID":len(self.landmarks)+1,
            "TYPE":TYPE
        }
        self.landmarks.append(landmark)
