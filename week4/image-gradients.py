# Image Gradients
# ###############

# We have seen that we can design convolution kernels for blurring an image. 

# The directional change in intensity of pixels is called gradient.

# In color images, gradients are calculated for every channel separately.
# In many applications color images are converted to grayscale 
# and gradients are calculated using the grayscale image.

# there are X gradiants and Y gradiants. Intensity changes in x direction and 
# respectivly in y direction.

# First Order Derivative Filter
# #############################

# Prewitt Filter
# --------------
# example X gradiant: find difference in intensity to the right 
# and to the left of the current pixel.

# 3x3 patch for X
# -1 0 -1
# -1 0 -1
# -1 0 -1

# 3x3 patch for Y
# -1 -2 -1 
# 0 0 0 
# -1 2 -1 

# Sobel Filter
# ------------
# apply a gausian blur filter and then gradiant filter (two convolution operations)

# 3x3 patch for X 
# -1 0 1
# -2 0 2 
# -1 0 1

# OpenCV provides a Sobel function
# dst =   cv2.Sobel(  src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]] )
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#gacea54f142e81b6758cb6f375ce782c8d

import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def sobelFilter():
    """
    First Order Derivative Filter
    """
    # work with grayscale image
    image = cv2.imread("truth.png", cv2.IMREAD_GRAYSCALE)
    # plt.imshow(image)
    # plt.show()

    # print(np.unique(image))
    # range from: 0 - 255

    # calculate X and Y gradiants

    # Apply sobel filter along x direction
    sobelx = cv2.Sobel(image, cv2.CV_32F, 1, 0)
    # Apply sobel filter along y direction
    sobely = cv2.Sobel(image,cv2.CV_32F,0,1)

    # print(np.unique(sobelx))
    # range from: -1020.0 - 1020.0

    # (OPTIONAL) Normalize image for display (plt)
    # the image is normalized by scaling and shifting so that all pixel values lie between 0 and 1.
    cv2.normalize(sobelx, 
        dst = sobelx, 
        alpha = 0, 
        beta = 1, 
        norm_type = cv2.NORM_MINMAX, 
        dtype = cv2.CV_32F)
    cv2.normalize(sobely, 
        dst = sobely, 
        alpha = 0, 
        beta = 1, 
        norm_type = cv2.NORM_MINMAX, 
        dtype = cv2.CV_32F)

    # print(np.unique(sobelx))
    # range from: 0.0 - 1.0

    plt.figure(figsize=[20,10])
    plt.subplot(121);plt.imshow(sobelx, cmap='gray');plt.title("Sobel X Gradients")
    plt.subplot(122);plt.imshow(sobely, cmap='gray');plt.title("Sobel Y Gradients")
    plt.show()

# http://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html#laplacian
#
# simple convolution kernel
# 0 1 0
# 1 -4 1
# 0 1 0
def laplacianFilter():
    """
    The Laplacian is a filter that is based on the second derivative.

    The Laplacian filter is very sensitive to noise 
    and therefore it is important to smooth the image before applying it.
    """
    img = cv2.imread("lion.jpg", cv2.IMREAD_GRAYSCALE)
    kernelSize = 3

    # make it smooth
    img1 = cv2.GaussianBlur(img,(3,3),0,0)
    # apply laplacian
    laplacian = cv2.Laplacian(img1, cv2.CV_32F, ksize = kernelSize, \
        scale = 1, delta = 0)

    # Normalize results
    cv2.normalize(laplacian, 
        dst = laplacian, 
        alpha = 0, 
        beta = 1, 
        norm_type = cv2.NORM_MINMAX, 
        dtype = cv2.CV_32F)
    
    plt.figure(figsize=[20,10])
    plt.imshow(laplacian,cmap='gray');plt.title("Laplacian")
    plt.show()

def imageSharpening():
    """
    In sharpening we want to enhance the edges and bring out more of the underlying texture.

    simple sharpening kernel:
    0 -1 0 
    -1 -5 -1
    0 -1 0
    """
    image = cv2.imread("lion.jpg")

    # Sharpen kernel
    sharpen = np.array((
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]), dtype="int")

    # Using 2D filter by applying the sharpening kernel
    sharpenOutput = cv2.filter2D(image, -1, sharpen)

    plt.figure(figsize=[20,10])
    plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("Original Image")
    plt.subplot(122);plt.imshow(sharpenOutput[...,::-1]);plt.title("Sharpening Result")
    plt.show()

if __name__ == "__main__":
    # sobelFilter()
    # laplacianFilter()
    imageSharpening()
