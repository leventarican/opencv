# morphological operations

# blobs: collection of pixels after binarizing an image
# ex. in threshold.png each digit is a blob
# morphology; english meaning: the study of forms things or shapes
# dilation; english meaning: expand or larger a shape. ex. make white regions bigger
# erosion: english meaning: shrink a shape

# Morphological Gradient: is the difference between dilation and erosion of an image.
# https://docs.opencv.org/4.1.0/d9/d61/tutorial_py_morphological_ops.html

# Dilation is used to merge or expand white regions which may be close to each other and
# Erosion is used to separate or shrink white regions

# dilation is mostly used to fill up black gaps/holes between a white region 
# and erosion is mostly used to further refine a white region

# dst =   cv.dilate(  src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#ga4ff0f3318642c4f469d0e11f242f3b6c

# dst =   cv.erode(   src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#gaeb1e0c1033e3f6b891a25d0511362aeb

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imageDilation = "dilation_example.jpg"
imageErosion = "erosion_example.jpg"

image = None
kernel1 = None
kernel2 = None

# smaller kernel with multiple iterations
def kernel2():
    global kernel2

    kSize = (3,3)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kSize)
    plt.imshow(kernel2)
    plt.show()

# single big kernel
def kernel1():
    global kernel1

    # Get structuring element/kernel which will be used for dilation
    kSize = (7,7)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kSize)
    plt.imshow(kernel1)
    # plt.show()

# ##############################################################################

# like drawing with photoshop
def applyDilateFunction(kernel):
    if kernel == 1:
        imageDilated = cv2.dilate(image, kernel1)
    elif kernel == 2:
        imageDilated = cv2.dilate(image, kernel2)

    plt.figure(figsize=[15,15])
    plt.subplot(121);plt.imshow(image);plt.title("Original Image")
    plt.subplot(122);plt.imshow(imageDilated);plt.title("Dilated Image");
    plt.show()

def checkDilationImage():
    global image
    
    image = cv2.imread(imageDilation)
    if image is None:  
        print("Could not open or find the image")
    plt.imshow(image)
    # plt.show()

# ##############################################################################

def applyErodisionFunction(kernel):
    if kernel == 1:
        # Eroding the image , decreases brightness of image
        imageEroded = cv2.erode(image, kernel1)
    elif kernel == 2:
        imageEroded = cv2.erode(image, kernel2)

    plt.figure(figsize=[15,15])
    plt.subplot(121);plt.imshow(image);plt.title("Original Image")
    plt.subplot(122);plt.imshow(imageEroded);plt.title("Eroded Image");
    plt.show()

def checkErosionImage():
    global image
    
    image = cv2.imread(imageErosion)
    if image is None:  
        print("Could not open or find the image")
    plt.imshow(image)
    plt.show()

# ##############################################################################

def dilationExample():
    checkDilationImage()
    applyDilateFunction(kernel=2)

# target: get rid of white spots in the 2 coins
def erosionExample():
    checkErosionImage()
    applyErodisionFunction(kernel=2)

if __name__ == "__main__":
    kernel1()
    kernel2()

    # dilationExample()
    erosionExample()
