#!/usr/bin/python3
import ephem
import math
import time

sun = ephem.Sun()

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   17332.28575632  .00003326  00000-0  57234-4 0  9993"
line2 = "2 25544  51.6431 300.2614 0004099 158.9129 343.4648 15.54248554 87274"

iss = ephem.readtle(name, line1, line2)
twilight = math.radians(-6)

while True:
    iss.compute()
    
    observer = ephem.Observer()
    observer.lat = iss.sublat
    observer.long = iss.sublong
    observer.elevation = 0

    sun.compute(observer)

    sun_angle = math.degrees(sun.alt)

    day_or_night = "Day" if sun_angle > twilight else "Night"

    print("Lat:\t%s\tLong:\t%s\t%s" % (iss.sublat, iss.sublong, day_or_night))

    time.sleep(1)
