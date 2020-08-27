# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/plumb_line-2020-08-27-14-07-00.py"

from time import sleep
from sense_hat import SenseHat
from PIL import Image, ImageDraw

sense = SenseHat()
sense.set_imu_config(True, True, True)  # enables all
sense.clear()
origin = (7, 7)
while True:
    a = sense.get_compass_raw()
    # Use the old trick of drawing something too big then down-sizing to get an
    # anti-aliased line
    img = Image.new('RGB', (15, 15))
    draw = ImageDraw.Draw(img)
    dest = (origin[0] + a['x'] * 7.0, origin[1] + a['y'] * 7.0)
    draw.line([origin, dest], fill=(255, 255, 255), width=3)
    img = img.resize((8, 8), Image.BILINEAR)
    sense.set_pixels(list(img.getdata()))
    sleep(0.04)

