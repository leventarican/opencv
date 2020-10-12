# ##############################################################################
# crop image
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imagePath = 'lion.jpg'
img = cv2.imread(imagePath)
plt.imshow(img[:,:,::-1])
plt.show()

# crop out a rectangle
crop = img[70:220,140:300]
plt.imshow(crop[:,:,::-1])
plt.show()
