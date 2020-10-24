# HSV color space

# Hue - indicates the color / tint of the pixel
# Saturation - indicates the purity (or richness) of the color
# Value - indicates the amount of brightness of the pixel

# HSV color space converts the RGB color space 
# from cartesian coordinates to cylindrical coordinates.

# dst =   cv2.cvtColor(   src, code[, dst[, dstCn]]   )
# https://docs.opencv.org/4.1.0/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab

import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def convertToHSV():
    bgr = cv2.imread("lion.jpg")
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    plt.figure(figsize=(20,15))
    plt.subplot(131)
    plt.imshow(hsv[:,:,0],cmap='gray')
    plt.title("Hue");
    plt.subplot(132)
    plt.imshow(hsv[:,:,1],cmap='gray')
    plt.title("Saturation");
    plt.subplot(133)
    plt.imshow(hsv[:,:,2],cmap='gray')
    plt.title("Value");
    plt.show()

def fromScratchHSV():
    """
    create HSV image from scratch and observe value, saturation, hue
    """

# value
for i in range(0,7):
    # create 50x50 image with 3 channels; values zero;
    imhsv = np.zeros((50, 50, 3), dtype=np.uint8)
    
    # Set Hue = 0, Saturation = 0, Value = i x 40
    v = i * 40
    imhsv[:,:,:] = (0, 0, v)
    
    # Convert HSV to RGB
    imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)

    # Display image
    ax = plt.subplot(1, 7, i+1)
    plt.imshow(imrgb)
    plt.axis('off')
    ax.set_title('V='+ str(v), fontdict={'fontsize': 15, 'fontweight': 'medium'})
plt.show()

# saturation
for i in range(0,7):
    imhsv = np.zeros((50, 50, 3), dtype=np.uint8)
    
    # Set Hue = 0, Saturation = i * 40, Value = 128
    s = i * 40
    imhsv[:,:,:] = (0, s, 128)

    imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)
    
    ax = plt.subplot(1, 7, i+1)
    plt.imshow(imrgb)
    plt.axis('off')
    ax.set_title('S='+ str(s), fontdict={'fontsize': 15, 'fontweight': 'medium'})
plt.show()

# hue
for i in range(0,7):
    imhsv = np.zeros((50, 50, 3), dtype=np.uint8)

    # Set Hue = i x 30, Saturation = 128, and Value = 128.
    h = i * 30
    imhsv[:,:,:] = ( h, 128, 128)
    
    imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2RGB)
    
    ax = plt.subplot(1, 7, i+1)
    plt.imshow(imrgb)
    plt.axis('off')
    ax.set_title('H='+ str(h), fontdict={'fontsize': 15, 'fontweight': 'medium'})
plt.show()

if __name__ == "__main__":
    # convertToHSV()
    fromScratchHSV()
