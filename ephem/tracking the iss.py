# sudo apt-get install libc6 libc6-dev
# sudo pip3 install ephem

# wget http://www.celestrak.com/NORAD/elements/stations.txt

import ephem
import time

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   17332.28575632  .00003326  00000-0  57234-4 0  9993"
line2 = "2 25544  51.6431 300.2614 0004099 158.9129 343.4648 15.54248554 87274"

iss = ephem.readtle(name, line1, line2)

while True:
    iss.compute()
    print("Lat:\t%s\tLong:\t%s" % (iss.sublat, iss.sublong))
    time.sleep(1)
