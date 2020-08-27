from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_gyroscope_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

# alternatives
print(sense.gyro_raw)
print(sense.gyroscope_raw)