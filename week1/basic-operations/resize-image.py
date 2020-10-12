# ##############################################################################
# Resizing an Image
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# use cv2.resize for image resize
# dst = cv2.resize( src, dsize[, dst[, fx[, fy[, interpolation]]]] )
# https://docs.opencv.org/4.1.0/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d

def scale_width_height():
    """
    scale with width and height
    """
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'

    img = cv2.imread('lion.jpg')

    resizeDownWidth = 300
    resizeDownHeight = 200
    # dst = cv2.resize(src, dsize, interpolation)
    resizedDown = cv2.resize(img, (resizeDownWidth, resizeDownHeight), interpolation= cv2.INTER_LINEAR)

    resizeUpWidth = 600
    resizeUpHeight = 900
    # dst = cv2.resize(src, dsize, interpolation)
    resizedUp = cv2.resize(img, (resizeUpWidth, resizeUpHeight), interpolation= cv2.INTER_LINEAR)

    plt.figure(figsize=[15,15])
    plt.subplot(131);plt.imshow(img[:,:,::-1]);plt.title("Original Image")
    plt.subplot(132);plt.imshow(resizedUp[:,:,::-1]);plt.title("Scaled Up Image")
    plt.subplot(133);plt.imshow(resizedDown[:,:,::-1]);plt.title("Scaled Down Image")
    plt.show()

def scale_factor():
    """
    scale with scale factor, BUT preserve the aspect ratio of the image
    """
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'

    img = cv2.imread('lion.jpg')

    scaleUpX = 1.5
    scaleUpY = 1
    scaleDown = 0.6

    scaledDown = cv2.resize(img, None, fx= scaleDown, fy= scaleDown, interpolation= cv2.INTER_LINEAR)
    scaledUp = cv2.resize(img, None, fx= scaleUpX, fy= scaleUpY, interpolation= cv2.INTER_LINEAR)

    plt.figure(figsize=[15,15])
    
    plt.subplot(131);plt.imshow(img[:,:,::-1]);plt.title("Original Image")

    plt.subplot(132);plt.imshow(scaledDown[:,:,::-1])
    plt.title(f'Scaled Down Image, size = { scaledDown.shape[:2] }')

    plt.subplot(133);plt.imshow(scaledUp[:,:,::-1])
    plt.title(f'Scaled Up Image, size = { scaledUp.shape[:2] }')

    plt.show()

if __name__ == "__main__":
    scale_width_height()
    scale_factor()
