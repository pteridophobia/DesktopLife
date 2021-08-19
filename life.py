import ctypes
import numpy
import uuid
import random
import os, time
from PIL import Image, ImageDraw

time.sleep(.01)


def createImage():
    height = 128
    width = 128
    rand_pixels = [random.randint(0, 255) for _ in range(width * height * 3)]
    rand_pixels_as_bytes = bytes(rand_pixels)
    text_and_filename = str(uuid.uuid4())

    random_image = Image.frombytes('RGB', (width, height), rand_pixels_as_bytes)

    draw_image = ImageDraw.Draw(random_image)
    draw_image.text(xy=(0, 0), text=text_and_filename, fill=(255, 255, 255))
    random_image.save("random.jpg".format(file_name=text_and_filename))
    random_image.close()


i = 0
while i < 100000:
    time.sleep(.1)
    SPI_SETDESKWALLPAPER = 20 
    createImage()
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"D:\GIT\desktoplife\DesktopLife\random.jpg" , 0)




