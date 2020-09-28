# ##############################################################################
# read a color image
# ##############################################################################

# most color images has 3 channels: RGB
# but there also the 4. channel alpha channel for transparency. png format supports that.

import matplotlib.pyplot as plt
import cv2

channels = 3
channels_transparency = 4

color_imagepath = 'lion.jpg'

img = cv2.imread(color_imagepath)
print(f'image shape/dimension; without alpha channel (number of ch=3): {img.shape}')
# output: image shape/dimension: (480, 440, 3)
