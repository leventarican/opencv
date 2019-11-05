import cv2
import numpy as np
import matplotlib.pyplot as plt

# #############################################################################
# resize an image
file = '../lion.jpg'
img = cv2.imread(file)
plt.imshow(img[...,::-1])

# resize with width and height
resizeWidth = 440//20
resizeHeight = 480//20
resized = cv2.resize(img, (resizeWidth, resizeHeight), interpolation=cv2.INTER_LINEAR)
plt.imshow(resized[:,:,::-1])
plt.show()

# resize with scaling
# INTER_NEAREST is faster but low quality
scaleX = 1.5
scaleY = 0.5
scaled = cv2.resize(img, None, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_NEAREST)
plt.imshow(scaled[:,:,::-1])
plt.show()