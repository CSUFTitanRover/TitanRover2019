from Image import Image
from Landmark import Landmark
import pygame
import res.coords as coords

icon_arrow = "res/images/vehicle.png"
icon_compass = "res/images/compass.png"

class Map(object):
    def __init__(self, screen, map_height, map_width):
        self.compass = pygame.image.load(icon_compass)
        self.landmarks = []
        self.lat_br = None
        self.lat_tl = None
        self.lon_br = None
        self.lon_tl = None
        self.map_height = map_height
        self.map_id = None
        self.map_image = None
        self.map_width = map_width
        self.screen = screen
        self.vehicle = self.AddLandmark(0,0,"VEHICLE",icon_arrow,self.screen)
    def AddLandmark(self,lat,lon,type,image,screen):
        landmark = Landmark(lat,lon,len(self.landmarks),type,image,screen)
        self.landmarks.append(landmark)
        return landmark
    def blitme(self, vehicle_lat, vehicle_lon):
        self.map_id = self.CalculateCorrectMap(vehicle_lat, vehicle_lon)
        # Set the correct map image
        self.UpdateMapImage()
        # Set the correct map boundaries
        self.UpdateMapBoundaries()
        # Calculate the correct position for each landmark
        self.UpdateMapLandmarks()
        # Now blit the map
        self.map_image.blitme()
        # Finally blit all landmarks
        for landmark in self.landmarks:
            landmark.blitme()
        self.compass = pygame.transform.scale(self.compass,(150,150))
        self.screen.blit(self.compass, (0,0))
    def CalculateCorrectMap(self, vehicle_lat, vehicle_lon):
        function_name = "CalculateCorrectMap()"
        if vehicle_lat and vehicle_lon:
            for location in coords.coords_list:
                if (vehicle_lat <= coords.coords_data[location+"_TL_LAT"] and
                    vehicle_lat >= coords.coords_data[location+"_BR_LAT"]):
                    if (vehicle_lon <= coords.coords_data[location+"_BR_LON"] and
                        vehicle_lon >= coords.coords_data[location+"_TL_LON"]):
                        return location
        else:
            # Return the default background
            return "_"
    def UpdateMapBoundaries(self):
        function_name = "UpdateMapBoundaries()"
        self.lat_br = coords.coords_data[self.map_id + "_BR_LAT"]
        self.lat_tl = coords.coords_data[self.map_id + "_TL_LAT"]
        self.lon_br = coords.coords_data[self.map_id + "_BR_LON"]
        self.lon_tl = coords.coords_data[self.map_id + "_TL_LON"]
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
                    # print function_name, "ERROR: maps lat/lon not set" FIXING
                    landmark.SetXY(0, 0)
            else:
                # print function_name, "ERROR: lat and/or lon empty" FIXING
                landmark.SetXY(0, 0)
    def GetAllLandmarks(self):
        return self.landmarks
    def GetVehicle(self):
        return self.vehicle
    def UpdateMapImage(self):
        self.map_image = Image(self.screen, self.map_id)
