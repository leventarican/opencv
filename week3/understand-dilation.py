# understand the Structuring element a.k.a Kernels

# There are 3 types of structuring elements supported by OpenCV.
# * Ellipse/Circular shaped
# * Rectangular shaped
# * Cross shaped

# there are 2 option to create a structuring element 
# * using numpy arrays. It is simply a matrix.
# * OpenCV: element = cv2.getStructuringElement(elementType, kernelSize, anchor)

# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#gac342a1bb6eabf6f55c803b09268e36dc

# Implement the Dilation operation using a elliptical structuring element 

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def createADemoImage():
    """
    create an empty matrix.
    add some white blobs on to image.
    """
    global im

    im = np.zeros((10,10),dtype='uint8')
    print(im);
    # plt.imshow(im)
    # plt.show()

    im[0,1] = 1
    im[-1,0]= 1
    im[-2,-1]=1
    im[2,2] = 1
    im[5:8,5:8] = 1

    print(im)
    plt.imshow(im)
    plt.show()

def createEllipseStructuringElement():
    """
    create a 3x3 ellipse structuring element.
    """
    global im, ksize, height, width, element

    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    print(element)
    # [[0 1 0]
    # [1 1 1]
    # [0 1 0]]
    print(element.shape)
    # (3, 3)
    
    ksize = element.shape[0]
    print(f"kernel size: {ksize}")
    # kernel size: 3

    height,width = im.shape[:2]
    print(f"image height: {height}; width: {width}")
    # image height: 10; width: 10

def dilationMethod1():
    """
    dilation from scratch with method 1:
    Scan the kernel through the image
    when you find a white pixel overlapping with the center of the kernel, 
    perform an OR operation of the Kernel and the pixel Neighborhood.
    """
    global ksize, height, width, element

    border = ksize//2   # // cast to integer
    print(f"copy image with border: {border}")
    # copy image with border: 1

    # Create a padded image with zeros padding
    # why are we doing this? to make space for the kernel

    # padded image method 1: with numpy zeros
    # row = height + border*2
    # col = width + border*2
    # print(f"padded image row: {row}; col: {col}")
    # padded image row: 12; col: 12
    # paddedIm = np.zeros((row, col))
    # plt.imshow(paddedIm);plt.show()

    # padded image method 2: with OpenCV copyMakeBorder function
    # The function copies the source image into the middle of the destination image. 
    # The areas to the left, to the right, above and below the copied source image will be filled with extrapolated pixels.
    # dst	=	cv.copyMakeBorder(	src, top, bottom, left, right, borderType[, dst[, value]]	)
    # https://docs.opencv.org/4.1.0/d2/de8/group__core__array.html#ga2ac1049c2c3dd25c2b41bffe17658a36
    paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
    # plt.imshow(paddedIm);plt.show()

    for h_i in range(border, height+border):
        for w_i in range(border,width+border):
            # When you find a white pixel
            if im[h_i-border,w_i-border]:
                print(f"\nwhite pixel found height, width: {h_i},{w_i}")
                
                row = (h_i - border, (h_i + border)+1)
                col = (w_i - border, (w_i + border)+1)

                print(f"row: {row}; col: {col}")
                
                # here happens the magic: replace pixel with OR structured element
                paddedIm[row[0]:row[1], col[0]:col[1]] = \
                    cv2.bitwise_or(paddedIm[row[0]:row[1], col[0]:col[1]], element)
                
                # intermediate result
                print(paddedIm)
                plt.imshow(paddedIm);plt.show()

def dilationWithOpenCV():
    """
    result when using OpenCV dilate funciton.
    """
    global im, element

    dilatedEllipseKernel = cv2.dilate(im, element)
    print(dilatedEllipseKernel)
    plt.imshow(dilatedEllipseKernel)
    plt.show()

if __name__ == "__main__":
    createADemoImage()
    createEllipseStructuringElement()
    dilationMethod1()
    dilationWithOpenCV()
