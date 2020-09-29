# ##############################################################################
# create image
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

# copy an image
imgCopy = img.copy()

# create an empty matrix with 3 channels
emptyMatrix = np.zeros((100,200,3),dtype='uint8')
plt.imshow(emptyMatrix)

# same but with color white
emptyMatrix = 255*np.ones((100,200,3),dtype='uint8')
plt.imshow(emptyMatrix)

# now create matrix based on copied image shade
emptyMatrix = 100*np.ones_like(img)
plt.imshow(emptyMatrix)

plt.show()
