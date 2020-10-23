# Image Filtering and Convolution

# Image Processing operations like Image Filtering are often used as a 
# preprocessing step in Computer Vision applications.

# https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html

# Signal processing jargon
# ########################
# image patch: 
# is a small region centered around a pixel
# 3x3 patch around a pixel := 3 by 3 neighborhood
#
# low frequency information: image patch is smooth and does not contain a lot of texture
# high frequency information: image patch contains a lot of textures 
#
# blurring an image / low pass filtering: it becomes more smooth. 
# low frequency information gets enhanced
#
# smoothing an image / high pass filtering: enhances edges and sharpens the image 
# so it lets the high frequency component pass and kinf of suppresses the low frequency component. 

# Image Filter
##############
# input: original image
# output: original image where each pixel has been modified based on its neighbors.
# this neighboors could be a 3x3 neighborhood or bigger
#
# also called linear filter. example: the middle pixel is the average of its neighbors.

# Convolution
# ###########
# an convolution kernel is used 
# a patch is multiplied with the kernel and added together. 
# both with the same size. e.g. 3x3
#
# this operation is used in many filters incl. 
# blurring filter, sharpening filter, edge detection, etc.
#
# convolutional kernels are also the basis of convolutional neural networks.
# 
# recap: to perform a convolutional operation we need an image patch and convolutional kernel

import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'

# dst =   cv.filter2D(    src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#ga27c049795ce870216ddfb366086b5a04

def defineKernel():
    kernel_size = 5
    # Create a 5*5 kernel with all elements equal to 1
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / kernel_size**2
    print (kernel)

    return kernel

# smoothing filter by convolving the image with a 5x5 kernel
def performConvolution(kernel, image):
    result = cv2.filter2D(image, -1, kernel, (-1, -1), delta=0, borderType=cv2.BORDER_DEFAULT)

    plt.figure(figsize=[20,10])
    plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("Original Image")
    plt.subplot(122);plt.imshow(result[...,::-1]);plt.title("Convolution Result")
    plt.show()

if __name__ == "__main__":
    image = cv2.imread("lion.jpg")
    kernel = defineKernel()
    performConvolution(kernel, image)
