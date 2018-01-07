import picamera
import time
import datetime as dt

team_name = "Dave's team"
time_format = "%d/%m/%Y %H:%M:%S"

cam = picamera.PiCamera()
cam.annotate_background = picamera.Color('black')
cam.annotate_text_size = 50
cam.annotate_text = dt.datetime.now().strftime(time_format)
time.sleep(2)

count = 0

for filename in cam.capture_continuous("img_{counter:04d}.jpg"):    
    print(filename)    
    
    count += 1
    if count >= 10:
        break

    time.sleep(1)
    cam.annotate_text = dt.datetime.now().strftime(time_format)

print("done")
