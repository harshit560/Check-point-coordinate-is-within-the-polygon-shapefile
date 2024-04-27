#!/usr/bin/env python

import shapefile
from shapely.geometry import Point # Point class
from shapely.geometry import shape # shape() is a function to convert geo objects through the interface

point_to_check = (76.305,19.883) # an x,y tuple
shp = shapefile.Reader('C:\\Users\\Desktop\\shapefile\\Indi.shp') #set your location folder and open the shapefile
all_shapes = shp.shapes() # get all the polygons
all_records = shp.records()     
for i in range(1,len(all_shapes)):
    boundary = all_shapes[i] # get a boundary polygon
    #print(shape(boundary))
    if Point(point_to_check).within(shape(boundary)): # make a point and see if it's within the polygon
       c = all_records[i][4] # get the second field of the corresponding record, change according to the attribute table of your shapefile
       print(c)

