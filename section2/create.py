import cv2
import numpy as np
import matplotlib.pyplot as plt

# #############################################################################
# display an image
file = '../lion.jpg'
img = cv2.imread(file)
plt.imshow(img[:,:,::-1])

# #############################################################################
# copy an image
clone = img.copy()

# #############################################################################
# create an empty image
# images in python are numpy arrays ...
shape = (100, 200, 3)   # 3 channel image
datatype = 'uint8' # 8 bit unsigned integer
emptyMatrix = np.zeros(shape, dtype=datatype)
plt.imshow(emptyMatrix)

# fill with white pixels
emptyMatrixWhite = 255*np.ones(shape, dtype=datatype)
plt.imshow(emptyMatrixWhite)

# same size as original image
emptyOriginal = 100*np.ones_like(img)
plt.imshow(emptyOriginal)

plt.show()
