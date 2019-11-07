import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../lion.jpg')

contrastPercentage = 30
contrastValue = (1+contrastPercentage/100)  # 1.3
# contrastHigh = img * contrastValue

# plt.figure(figsize=[20,20])
# plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("original Image")
# plt.subplot(122);plt.imshow(contrastHigh[...,::-1]);plt.title("High Contrast")

# plt.show()

# print("Original Image Datatype : {}".format(img.dtype))
# print("Contrast Image Datatype : {}".format(contrastHigh.dtype))

# print("Original Image Highest Pixel Intensity : {}".format(img.max()))
# print("Contrast Image Highest Pixel Intensity : {}".format(contrastHigh.max()))

# contrast is float datatype
# convert back to int
contrastImage = img *contrastValue
clippedContrastImage = np.clip(contrastImage, 0, 255)
contrastHighClippedUint8 = np.uint8(clippedContrastImage)

# here we keep it in float datatype
contrastHighNormalized = (img * contrastValue)/255
contrastHighNormalized01Clipped = np.clip(contrastHighNormalized,0,1)

plt.figure(figsize=[20,20])
plt.subplot(131);plt.imshow(img[...,::-1]);plt.title("original Image")
plt.subplot(132);plt.imshow(contrastHighClippedUint8[...,::-1]);plt.title("converted back to uint8")
plt.subplot(133);plt.imshow(contrastHighNormalized01Clipped[...,::-1]);plt.title("Normalized float to [0, 1]")

plt.show()