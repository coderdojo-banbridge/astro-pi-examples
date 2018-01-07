import picamera
import time
import datetime as dt

time_format = "%d/%m/%Y %H:%M:%S"

cam = picamera.PiCamera()
cam.start_preview(alpha = 192)  # alpha = 192

cam.annotate_background = picamera.Color('black')
cam.annotate_text_size = 50

for i in range(5):
    cam.annotate_text = dt.datetime.now().strftime(time_format)
    time.sleep(1)

cam.capture("foo.jpg")
cam.stop_preview()
