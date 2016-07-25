import math

r = 6371000.0
kmdeg = 6371000*(2*math.pi/360)
hexR = 10.0

def getLoc(latitude,longitude,x,y):
    new_latitude  = latitude + (y/r)*(180/math.pi);
    new_longitude = longitude + (x / r) * (180/math.pi)/math.cos(latitude * math.pi/180);
    return str(new_latitude)+"  "+str(new_longitude)
print(getLoc(1,1,10,10))

myLat = 1
myLon = 1
print(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))

print(getLoc(myLat,myLon,hexR/2,hexR*math.sqrt(3)/2))

print(getLoc(myLat,myLon,hexR,0))

print(getLoc(myLat,myLon,hexR/2,-1*hexR*math.sqrt(3)/2))

print(getLoc(myLat,myLon,-1*hexR/2,-1*hexR*math.sqrt(3)/2))

print(getLoc(myLat,myLon,-10,0))

print(getLoc(myLat,myLon,-1*hexR/2,hexR*math.sqrt(3)/2))

