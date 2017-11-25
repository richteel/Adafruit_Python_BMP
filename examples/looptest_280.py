#!/usr/bin/env python3
"""Loop test for BMP280 (Works with Python 2 & 3"""

import time
import Adafruit_BMP.BMP280 as BMP280

SENSOR = BMP280.BMP280()

while True: # loop
    temperature = SENSOR.read_temperature()
    pressure = SENSOR.read_pressure()
    altitude = SENSOR.read_altitude()
    sealevel_pressure = SENSOR.read_sealevel_pressure()

    print('Temp = {0:0.2f} *C '.format(temperature) +
          'Pressure = {0:0.2f} Pa '.format(pressure) +
          'Altitude = {0:0.2f} m '.format(altitude) +
          'Sealevel Pressure = {0:0.2f} Pa'.format(sealevel_pressure))
    time.sleep(0.5)