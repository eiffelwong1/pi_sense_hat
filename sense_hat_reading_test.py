import sys
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_imu_config(True, True, True)
while True:
    print("+"*20)
    print("humidity",sense.get_humidity())
    print("h_temp", sense.get_temperature())
    print("pressure",sense.get_pressure())
    print("p_temp", sense.get_temperature_from_pressure())
    print("IMU")
    pitch, roll, yaw = sense.get_orientation_radians().values()
    print(f"p: {pitch}, r: {roll}, y:{yaw}")
    pitch, roll, yaw = sense.get_orientation_degrees().values()
    print(f"p: {pitch}, r: {roll}, y:{yaw}")
    sys.stdout.flush()
    time.sleep(3)
