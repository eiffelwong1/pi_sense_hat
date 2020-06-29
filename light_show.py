import time
import random
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = False
while True:
    i = random.randint(0,63)
    time.sleep(random.randint(0,100)/1000)
    sense.set_pixel(i%8, int(i/8), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))

