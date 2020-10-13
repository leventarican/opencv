import cv2
import numpy as np
import matplotlib.pyplot as plt

# #############################################################################
# crop an image: extract a rectangular region of an image
file = 'lion.jpg'
img = cv2.imread(file)
plt.imshow(img[:,:,::-1])
print(img.shape)    # (480, 440, 3)

clone = img.copy()
plt.imshow(clone[...,::-1])

# x / column: 100 to 300
# y / row: 50 to 250
crop = clone[50:270, 120:300]
plt.imshow(crop[:,:,::-1])
print(crop.shape)   # (220, 180, 3)

plt.show()
