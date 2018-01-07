import picamera
import time
import datetime as dt

team_name = "Dave's team"
time_format = "%d/%m/%Y %H:%M:%S"

cam = picamera.PiCamera()

cam.start_preview()  # alpha = 192
cam.annotate_background = picamera.Color('black')
cam.annotate_text_size = 50

start = time.time()
cam.start_recording("foo.h264")

while time.time() - start < 10:
    info = []
    info.append(team_name)
    info.append(dt.datetime.now().strftime(time_format))    
    cam.annotate_text = "\n".join(info)
    cam.wait_recording(0.2)

cam.stop_preview()
cam.stop_recording()

# sudo apt-get update
# sudo apt-get install gpac
# MP4Box -add foo.h264 foo.mp4
# rm foo.h264
# omxplayer foo.mp4
