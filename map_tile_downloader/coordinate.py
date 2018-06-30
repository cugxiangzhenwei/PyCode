#!/usr/bin/env python
# -*- coding:utf-8 -*-
import io
from math import radians, cos, sin, asin, sqrt,pow,log,tan

class Tile():
   def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


def geo2Tile(lon,lat,zoom):
    n = pow(2,zoom)
    dx = (lon + 180.0)/360.0*n
    dy = (1 - (log(tan(radians(lat)) + (1 / cos(radians(lat)))) /3.1415926)) /2 * n
    return Tile(int(dx),int(dy),zoom)

#tile = geo2Tile(117.12,42.13,18)
#print 'x=%d,y=%d,z=%d' % (tile.x,tile.y,tile.z)

