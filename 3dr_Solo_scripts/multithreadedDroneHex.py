from dronekit import *
from dronekit import connect
import math
import sys
import time
import json
import datetime


flying = True
# make dict for dumping later
gpsData = {}
# Connect to UDP endpoint (and wait for default attributes to accumulate)
#target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
#print 'Connecting to ' + target + '...'
#vehicle = connect(target, wait_ready=True)
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
vehicle.mode = VehicleMode("GUIDED")
vehicle.groundspeed = 5

r = 6371000.0
kmdeg = 371000*(2*math.pi/360)
hexR = 10.0
alt = vehicle.location.global_frame.alt

def getLoc(latitude,longitude,x,y):
    new_latitude  = latitude + (y/r)*(180/math.pi);
    new_longitude = longitude + (x / r) * (180/math.pi)/math.cos(latitude * math.pi/180);
    return LocationGlobalRelative(new_latitude,new_longitude,alt)


#need to change this to accept these as user input parameters
myLat = vehicle.location.global_frame.lat
myLon = vehicle.location.global_frame.lon

vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.simple_goto(getLoc(myLat,myLon,hexR/2,hexR*math.sqrt(3)/2))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.simple_goto(getLoc(myLat,myLon,hexR,0))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.simple_goto(getLoc(myLat,myLon,hexR/2,-1*hexR*math.sqrt(3)/2))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,-1*hexR*math.sqrt(3)/2))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.simple_goto(getLoc(myLat,myLon,-10,0))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.simple_goto(LocationGlobalRelative(myLat,myLon,alt))
time.sleep(3)
print " Global Location: %s" % vehicle.location.global_frame
#gpsData[time.time()] = vehicle.location.global_frame
gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = vehicle.location.global_frame

vehicle.close()
print("done")

with open('gpsTimestamps', 'w') as f:
    json.dump(gpsData, f)
