#!/usr/bin/env python
# -*- coding:utf-8 -*-
import io
from math import radians, cos, sin, asin, sqrt,pow,log,tan,atan,sinh

class Tile():
   def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

def tileIndex2GeoPoint(x,y,zoom):
    n = pow(2,zoom)
    lng = x*1.0/n*360.0-180.0
    lat = atan(sinh(3.1415926*(1-2*y/n)))
    lat = lat*180.0/3.1415926
    return lng,lat


def geo2Tile(lon,lat,zoom):
    n = pow(2,zoom)
    dx = (lon + 180.0)/360.0*n
    dy = (1 - (log(tan(radians(lat)) + (1 / cos(radians(lat)))) /3.1415926)) /2 * n
    return Tile(int(dx),int(dy),zoom)

tile = geo2Tile(117.12,42.13,18)
print 'x=%d,y=%d,z=%d' % (tile.x,tile.y,tile.z)
(lng,lat) = tileIndex2GeoPoint(tile.x,tile.y,tile.z)
print 'geo(%f,%f)'%(lng,lat)

