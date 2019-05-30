from Image import Image
from Landmark import Landmark

class Map(object):
    def __init__(self, screen):
        self.landmarks = []
        self.lat_br = None
        self.lat_tl = None
        self.lon_br = None
        self.lon_tr = None
        self.map_height = None
        self.map_image = None
        self.map_width = None
        self.screen = screen
        self.vehicle = None
    def AddLandmark(self,lat,lon,type,image,screen):
        landmark = Landmark(lat,lon,len(self.landmarks),type,image,screen)
        self.landmarks.append(landmark)
        return landmark
    def blitme(self, vehicle_lat, vehicle_lon):
        # Calculate the correct map image
        self.UpdateMapImage(vehicle_lat, vehicle_lon)
        # Now blit the map
        self.map_image.blitme()
        # Then blit any landmarks
        for landmark in self.landmarks:
            landmark.blitme()
        # Lastly, blit the vehicle
        #self.vehicle.blitme() FIXING
    def CalculateCorrectMapImage(self, vehicle_lat, vehicle_lon):
        function_name = "CalculateCorrectMapImage()"
        if vehicle_lat and vehicle_lon:
            for location in coords.coords_list:
                if (roverLat <= coords.coords_data[location+"_TL_LAT"] and
                    roverLat >= coords.coords_data[location+"_BR_LAT"]):
                    if (roverLon <= coords.coords_data[location+"_BR_LON"] and
                        roverLon >= coords.coords_data[location+"_TL_LON"]):
                        print function_name, "found correct map image"
    def GetAllLandmarks(self):
        return self.landmarks
    def UpdateMapImage(self, vehicle_lat, vehicle_lon):
        if vehicle_lat and vehicle_lon:
            map_id = self.CalculateCorrectMapImage(vehicle_lat, vehicle_lon)
        else:
            map_id = "logo_large"
        self.map_image = Image(self.screen, map_id)


    def Set_Display_Data(ID):
        global display_image
        global display_LAT_TL
        global display_LON_TL
        global display_LAT_BR
        global display_LON_BR
        TL_LAT = ID + "_TL_LAT"
        TL_LON = ID + "_TL_LON"
        BR_LAT = ID + "_BR_LAT"
        BR_LON = ID + "_BR_LON"
        display_image = ID
        display_LAT_TL = coords.coords_data[TL_LAT]
        display_LON_TL = coords.coords_data[TL_LON]
        display_LAT_BR = coords.coords_data[BR_LAT]
        display_LON_BR = coords.coords_data[BR_LON]
