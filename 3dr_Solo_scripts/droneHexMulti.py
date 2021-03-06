from __future__ import division
from dronekit import *
from dronekit import connect
import math
import sys
import time
import json
import datetime
from threading import Thread
# make dict for dumping later
gpsData = {}
# Connect to UDP endpoint (and wait for default attributes to accumulate)
#target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
#print 'Connecting to ' + target + '...'
#vehicle = connect(target, wait_ready=True)
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
vehicle.mode = VehicleMode("GUIDED")
vehicle.groundspeed = 5
run = True
def runA():
    global run
    r = 6371000.0
    kmdeg = 6371000*(2*math.pi/360)
    hexR = 10.0
    alt = vehicle.location.global_frame.alt

    def getLoc(latitude,longitude,x,y):
        new_latitude  = latitude + (y/r)*(180/math.pi);
        new_longitude = longitude + (x / r) * (180/math.pi)/math.cos(latitude * math.pi/180);
        return (LocationGlobalRelative(new_latitude,new_longitude,alt))


    #need to change this to accept these as user input parameters
    myLat = vehicle.location.global_frame.lat
    myLon = vehicle.location.global_frame.lon

    vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.simple_goto(getLoc(myLat,myLon,hexR/2,hexR*math.sqrt(3)/2))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.simple_goto(getLoc(myLat,myLon,hexR,0))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.simple_goto(getLoc(myLat,myLon,hexR/2,-1*hexR*math.sqrt(3)/2))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,-1*hexR*math.sqrt(3)/2))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR,0))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.simple_goto(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.simple_goto(LocationGlobalRelative(myLat,myLon,alt))
    time.sleep(3)
    print " Global Location: %s" % vehicle.location.global_frame

    vehicle.close()
    run = False
    print("done")

def runB():
    global run
    while run:
        #gpsData[time.time()] = str(vehicle.location.global_frame)
        gpsData[datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')] = str(vehicle.location.global_frame)
        time.sleep(.1)
    with open('gpsTimestamps', 'w') as f:
        json.dump(gpsData, f)

if __name__ == "__main__":
    t1 = Thread(target = runA)
    t2 = Thread(target = runB)
    t1.isDaemon()
    t2.isDaemon()
    t1.start()
    t2.start()
    t1.join()
    t2.join()


