# ##############################################################################
# Copying a Region to another
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imagePath = 'lion.jpg'
img = cv2.imread(imagePath)
imgCopy = img.copy()

# like crop
# point 1: x= 150; y=100
# point 2: x= 300; y=250
# remember: img[row,column]
copyRoi = img[100:250,150:300]

# height and width of the ROI
roiHeight,roiWidth = copyRoi.shape[:2]

imgCopy[40:40+roiHeight, 10:10+roiWidth] = copyRoi

plt.figure(figsize=[15,15])

# subplot: 
# a 3-digit integer describing the position of the subplot.
# rows, columns, index
# read document for more
plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Original Image");
plt.subplot(122);plt.imshow(imgCopy[...,::-1]);plt.title("Output Image");
plt.show()
