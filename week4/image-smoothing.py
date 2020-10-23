# Image Smoothing

# Box Blur
# Gaussian Blur
# Median Blur
# Bilateral Filtering


# deciding which filter to use for your problem 
# ---------------------------------------------
# Median filtering is the best way to smooth images which have salt-pepper type of noise (sudden high / low values in the neighborhood of a pixel).
# Gaussian filtering can be used if there is low Gaussian noise.
# Bilateral Filtering should be used if there is high level of Gaussian noise, and you want the edges intact while blurring other areas.
# In terms of execution speed, Gaussian filtering is the fastest and Bilateral filtering is the slowest.

import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'

# the OpenCV function blur() uses function filter2D()
# dst =   cv2.blur(   src, ksize[, dst[, anchor[, borderType]]]   )
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37
def boxBlur():
    """
    A very common use case for convolution is blurring or smoothing or Low pass filtering.
    It reduces the noise in the image. 
    """
    img = cv2.imread("lion.jpg")

    # anchor: anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.

    # Apply box filter - kernel size 3
    dst1=cv2.blur(img,ksize=(3,3),anchor=(-1,-1))

    # Apply box filter - kernel size 7
    dst2=cv2.blur(img,(7,7),(-1,-1))

    plt.figure(figsize=[20,10])
    plt.subplot(131);plt.imshow(img[...,::-1]);plt.title("Original Image")
    plt.subplot(132);plt.imshow(dst1[...,::-1]);plt.title("Box Blur Result 1 : KernelSize = 3")
    plt.subplot(133);plt.imshow(dst2[...,::-1]);plt.title("Box Blur Result 2 : KernelSize = 7")
    plt.show()

# dst =   cv2.GaussianBlur(   src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]   )
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1
def gaussianBlur():
    """
    An image blurred using the Gaussian kernel looks less blurry compared to a box kernel of the same size.
    Small amount of Gaussian blurring is frequently used to remove noise from an image.
    
    It is also applied to the image prior to a noise sensitive image filtering operations.
    For example, the Sobel kernel used for calculating the derivative of an image 
    is a combination of a Gaussian kernel and a finite difference kernel.
    """
    img = cv2.imread("lion.jpg")

    # Apply gaussian blur
    dst1=cv2.GaussianBlur(img,(5,5),0,0)
    dst2=cv2.GaussianBlur(img,(25,25),50,50)

    lineType=4
    fontScale=1

    combined = np.hstack((img, dst1,dst2))

    plt.figure(figsize=[20,10])
    plt.subplot(131);plt.imshow(img[...,::-1]);plt.title("Original Image")
    plt.subplot(132);plt.imshow(dst1[...,::-1]);plt.title("Gaussian Blur Result 1 : KernelSize = 5")
    plt.subplot(133);plt.imshow(dst2[...,::-1]);plt.title("Gaussian Blur Result 2 : KernelSize = 25")
    plt.show()

# dst =   cv2.medianBlur( src, ksize[, dst]   )
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9
def medianBlur():
    """
    Median Filter.
    Median blur filtering is a nonlinear filtering technique that is most 
    commonly used to remove salt-and-pepper noise from images.
    
    In OpenCV’s implementation of the median blur, a square kernel is used.
    """
    img = cv2.imread("lion.jpg")

    # Defining the kernel size
    kernelSize = 5

    # Performing Median Blurring and store it in numpy array "medianBlurred"
    medianBlurred = cv2.medianBlur(img,kernelSize)

    # Display the original and median blurred image
    plt.figure(figsize=[20,10])
    plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Original Image")
    plt.subplot(122);plt.imshow(medianBlurred[...,::-1]);plt.title("Median Blur Result : KernelSize = 5")
    plt.show()

# dst =   cv2.bilateralFilter(    src, d, sigmaColor, sigmaSpace[, dst[, borderType]] )
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed
def bilateralBlur():
    """
    A Bilateral Filter is nonlinear, edge-preserving and noise-reducing smoothing filter.
    """
    img = cv2.imread("lion.jpg")

    # diameter of the pixel neighbourhood used during filtering
    dia=15;

    # Larger the value the distant colours will be mixed together 
    # to produce areas of semi equal colors
    sigmaColor=80

    # Larger the value more the influence of the farther placed pixels 
    # as long as their colors are close enough
    sigmaSpace=80

    #Apply bilateralFilter
    result = cv2.bilateralFilter(img, dia, sigmaColor, sigmaSpace)

    plt.figure(figsize=[20,10])
    plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("Original Image")
    plt.subplot(122);plt.imshow(result[...,::-1]);plt.title("Bilateral Blur Result")
    plt.show()

if __name__ == "__main__":
    # boxBlur()
    # gaussianBlur()
    # medianBlur()
    bilateralBlur()
