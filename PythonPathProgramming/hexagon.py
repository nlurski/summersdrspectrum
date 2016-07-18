#!/usr/bin/python
#coords     40.468065    -74.443756    map to field near winlab

#The algorithm is correct, however, I am having issues with precision
import math


def meterLat(longitude):
    temp = float(1 / 111111)
    return temp


def meterLon(latitude):
    temp = float(1 / 111111 * math.cos(latitude))
    return temp


def disp(lati, longi):
    temp = str(lati) + ' ' + str(longi)
    print (temp)
    return

lat = float((input('Input target latitude: ')))
lon = float((input('Input target longitude: ')))
rad = float((input('Input radius: ')))
rootThree = math.sqrt(3)

lat1 = lat - (rad * meterLat(lon))
lon1 = lon

lat2 = lat - (rad / 2 * meterLat(lon))
lon2 = lon - (rad * rootThree / 2 * meterLon(lat))

lat3 = lat + (rad / 2 * meterLat(lon))
lon3 = lon - (rad * rootThree / 2 * meterLon(lat))

lat4 = lat + (rad * meterLat(lon))
lon4 = lon

lat5 = lat + (rad / 2 * meterLat(lon))
lon5 = lon + (rad * rootThree / 2 * meterLon(lat))

lat6 = lat - (rad / 2 * meterLat(lon))
lon6 = lon + (rad * rootThree / 2 * meterLon(lat))

disp(lat1, lon1)
disp(lat2, lon2)
disp(lat3, lon3)
disp(lat4, lon4)
disp(lat5, lon5)
disp(lat6, lon6)