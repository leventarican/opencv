# ##############################################################################
# modify color pixels
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt

# read grayscale image as color image
# change color of specific pixel
# change color of ROI (region of interest)

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imagePath = 'number_zero.jpg'

# IMREAD_GRAYSCALE has 1 channel
# IMREAD_COLOR has 3 channels even its grayscale channel. the channels are cloned.
testImage = cv2.imread(imagePath, cv2.IMREAD_COLOR)

plt.imshow(testImage)
plt.show()

# access pixel
print(testImage[0,0])
# [1 1 1]

# modify pixel
plt.figure(figsize=[10,10])

# testImage[:,:,::-1] => reverse the order of the 3rd dimension (=channels): from BGR to RGB
testImage[0,0] = (0,255,255)
plt.subplot(131);plt.imshow(testImage[:,:,::-1])
testImage[1,1] = (255,255,0)
plt.subplot(132);plt.imshow(testImage[:,:,::-1])
testImage[2,2] = (255,0,255)
plt.subplot(133);plt.imshow(testImage[:,:,::-1])

plt.show()
