from dronekit import *
from dronekit import connect
import math
import sys

# Connect to UDP endpoint (and wait for default attributes to accumulate)
#target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
#print 'Connecting to ' + target + '...'
#vehicle = connect(target, wait_ready=True)
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
vehicle.mode = VehicleMode("GUIDED")

r = 6371000.0
kmdeg = 371000*(2*math.pi/360)
hexR = 10.0
alt = vehicle.location.global_frame.alt

def getLoc(latitude,longitude,x,y):
    new_latitude  = latitude + (y/r)*(180/math.pi);
    new_longitude = longitude + (x / r) * (180/math.pi)/math.cos(latitude * math.pi/180);
    return LocationGlobalRelative(new_latitude,new_longitude,alt)

myLat = vehicle.location.global_frame.lat
myLon = vehicle.location.global_frame.lon

vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))

vehicle.simple_goto(getLoc(myLat,myLon,hexR/2,hexR*math.sqrt(3)/2))

vehicle.simple_goto(getLoc(myLat,myLon,hexR,0))

vehicle.simple_goto(getLoc(myLat,myLon,hexR/2,-1*hexR*math.sqrt(3)/2))

vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,-1*hexR*math.sqrt(3)/2))

vehicle.simple_goto(getLoc(myLat,myLon,-10,0))

vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))

vehicle.simple_goto(LocationGlobalRelative(myLat,myLon,alt))

vehicle.close()
print("done")
