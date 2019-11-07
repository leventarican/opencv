import cv2
import numpy as np
import matplotlib.pyplot as plt

# #############################################################################
# convert image from int to float 1 to 255 -> 0 to 1.0
# this is needed on math operations

img = cv2.imread('../lion.jpg')

plt.imshow(img[...,::-1])
plt.show()

scalingFactor = 1/255.0
print(f'scalingFactor [we want values between 0 to 1.0]: {scalingFactor}')

# convert unsigned int to float
img = np.float32(img)
img = img * scalingFactor
print(f'image datatype [float expected]: {img.dtype}')

# convert float to unsigned int
img = img * (1.0/scalingFactor)
img = np.uint8(img)
print(f'image datatype [uint expected]: {img.dtype}')