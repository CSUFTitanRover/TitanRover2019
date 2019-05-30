from Image import Image
from Landmark import Landmark

icon_arrow = "../images/vehicle.png"

class Map(object):
    def __init__(self, screen):
        self.landmarks = []
        self.lat_br = None
        self.lat_tl = None
        self.lon_br = None
        self.lon_tl = None
        self.map_height = None
        self.map_image = None
        self.map_width = None
        self.screen = screen
        self.vehicle = AddLandmark(0,0,"VEHICLE",icon_arrow,self.screen)
    def AddLandmark(self,lat,lon,type,image,screen):
        landmark = Landmark(lat,lon,len(self.landmarks),type,image,screen)
        self.landmarks.append(landmark)
        return landmark
    def blitme(self, vehicle_lat, vehicle_lon):
        # Calculate the correct map image
        self.UpdateMapImage(vehicle_lat, vehicle_lon)
        # Calculate the correct position for each landmark
        self.UpdateMapLandmarks()
        # Now blit the map
        self.map_image.blitme()
        # Finally blit all landmarks
        for landmark in self.landmarks:
            landmark.blitme()
    def CalculateCorrectMapImage(self, vehicle_lat, vehicle_lon):
        function_name = "CalculateCorrectMapImage()"
        if vehicle_lat and vehicle_lon:
            for location in coords.coords_list:
                if (roverLat <= coords.coords_data[location+"_TL_LAT"] and
                    roverLat >= coords.coords_data[location+"_BR_LAT"]):
                    if (roverLon <= coords.coords_data[location+"_BR_LON"] and
                        roverLon >= coords.coords_data[location+"_TL_LON"]):
                        print function_name, "found correct map image"
    def UpdateMapLandmarks(self):
        function_name = "UpdateMapLandmarks()"
        for landmark in self.landmarks:
            landmark_lat, landmark_lon = landmark.GetLatLon()
            if landmark_lat != None and landmark_lon != None:
                if self.lat_tl and self.lat_br and self.lon_tl and self.lon_br:
                    x = (self.map_width  / abs(self.lon_tl-self.lon_br))
                    y = (self.map_height / abs(self.lat_tl-self.lat_br))
                    #if self.lat[len(self.lat)-1] == u"\u00B0":
                    #    self.lat = self.lat[:-1]
                    #if self.lon[len(self.lon)-1] == u"\u00B0":
                    #    self.lon = self.lon[:-1]
                    x = x * (float(landmark_lon)-float(self.lon_tl))
                    y = y * (float(landmark_lat)-float(self.lat_tl)) * -1
                    landmark.SetXY(x, y)
            else:
                print function_name,"ERROR: lat and/or lon empty"
    def GetAllLandmarks(self):
        return self.landmarks
    def UpdateMapImage(self, vehicle_lat, vehicle_lon):
        if vehicle_lat and vehicle_lon:
            map_id = self.CalculateCorrectMapImage(vehicle_lat, vehicle_lon)
        else:
            self.map_id = "logo_large"
        self.map_image = Image(self.screen, self.map_id)
