# ##############################################################################
# create image mask
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def mask_coordinates(img):
    """
    Create a mask using coordinates
    """

    mask = np.zeros_like(img)
    # plt.imshow(mask)
    # plt.show()

    # row, column == y, x
    mask[50:300,150:300] = 255

    plt.figure(figsize=[15,15])
    plt.subplot(121);plt.imshow(img[:,:,::-1]);plt.title("Original Image")
    plt.subplot(122);plt.imshow(mask[:,:,::-1]);plt.title("Mask")
    plt.show()

    print(mask.dtype)
    # uint8

def mask_pixel_intensity(img):
    """
    Create a mask using pixel intensity or color

    dst =   cv2.inRange(    src, lowerb, upperb[, dst]  )
    https://docs.opencv.org/4.1.0/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981
    """
    
    # lower boundary BGR: (150,0,0)
    # upper boundary BGR: (100,100,255)
    mask = cv2.inRange(img, (0,0,150), (100,100,255))
    plt.figure(figsize=[15,15])
    plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Original Image")
    plt.subplot(122);plt.imshow(mask);plt.title("Masked Image")

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'
    img = cv2.imread('lion.jpg')

    mask_coordinates(img)
    mask_pixel_intensity(img)

    plt.show()
