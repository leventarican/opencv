import cv2
import numpy as np
import matplotlib.pyplot as plt

# #############################################################################
# image mask has same size as original
# binary: white pixel we interested in; black not interested in
file = 'lion.jpg'
img = cv2.imread(file)

mask = np.zeros_like(img)
# blue channel 0 (lower boundary) to 100 (upper boundary)
# green channel 0 (lower boundary) to 100 (upper boundary)
# red channel 150 (lower boundary) to 255 (upper boundary)
mask = cv2.inRange(img, (0,0,140), (100,100,255))

plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(img[:,:,::-1]);plt.title("Original Image")
plt.subplot(122);plt.imshow(mask);plt.title("Mask")
plt.show()