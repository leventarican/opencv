import cv2
import numpy as np
import matplotlib.pyplot as plt

# #############################################################################
# copy a region to another
file = '../lion.jpg'
img = cv2.imread(file)
plt.imshow(img[...,::-1])

clone = img.copy()
plt.imshow(clone[...,::-1])

# roi: region of interest
roi = clone[50:270,120:300]
roiHeight, roiWidth = roi.shape[:2]

# copy roi into clone image
clone[40:40+roiHeight, 10:10+roiWidth] = roi

plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Original Image")
plt.subplot(122);plt.imshow(clone[...,::-1]);plt.title("Output Image")

plt.show()
