import time
from sense_hat import SenseHat


COLOR = {
    'white': (255,255,255),
    'half_white':(128,128,128),
    'red': (255,0,0),
    'green': (0,255,0),
    'blue': (0,0,255),
    'off': (0,0,0),
    }

sense = SenseHat()

for i in range(64):
    sense.set_pixel(i%8,int(i/8),i*4+3,i*4+3,i*4+3)

sense.low_light=True
time.sleep(2)
sense.low_light=False
time.sleep(2)

sense.clear()
