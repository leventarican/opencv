# ##############################################################################
# image with alpha channel
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt

# read grayscale image as color image
# change color of specific pixel
# change color of ROI (region of interest)

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imagePath = 'panther.png'

# IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
img = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)

# take first 3 channels(=color)
imgBGR = img[:,:,0:3]
# take only last channel (=alpha)
imgMask = img[:,:,3]

plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(imgBGR[:,:,::-1]);plt.title('Color channels');
plt.subplot(122);plt.imshow(imgMask,cmap='gray');plt.title('Alpha channel');
plt.show()
