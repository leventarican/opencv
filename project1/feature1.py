# Feature 1: Instagram Filters

# 1. Use the Jupyter Notebook that has been provided to you.
# 2. You have to complete the functions for cartoonification and pencil-sketching.
#
# implement two filters
# 
# 1. filter implementation: pencil sketch filter
# is using some sort of gradient or laplacian. 
# its not using canny edge detector, because edges are much thicker.
# background is white and the sketch is black.
# ~ 4-5 lines of code
#
# 2. filter implementation: cartoonify filter
# it has regions of constant color
# it is some sort of edge preserving filter
# the edges are colored (= some sort of edge detection is used)
# ~ 5-6 loc

# resources
# https://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/
# https://www.practicepython.org/blog/2016/12/20/instagram-filters-python.html
# https://www.youtube.com/watch?v=MVLuexuikv4

import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def cartoonify(image, arguments=0):
    
    ### YOUR CODE HERE

    # return cartoonImage
    return None

def pencilSketch(image, arguments=0):
    
    ### YOUR CODE HERE
    image = cv2.blur(image,(5,5))

    # Sharpen kernel
    sharpen = np.array((
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]), dtype="int")
    sharpenOutput = cv2.filter2D(image, -1, sharpen)

    blured = cv2.GaussianBlur(sharpenOutput,(3,3),0,0)
    
    kernelSize = 3
    laplacian = cv2.Laplacian(blured, cv2.CV_32F, ksize = kernelSize, scale = 1, delta = 3)

    thresh = 20
    maxValue = 100
    th, dst = cv2.threshold(laplacian, thresh, maxValue, cv2.THRESH_BINARY_INV)
    pencilSketchImage = dst

    cv2.normalize(pencilSketchImage, 
        dst = pencilSketchImage, 
        alpha = 0, 
        beta = 1, 
        norm_type = cv2.NORM_MINMAX, 
        dtype = cv2.CV_32F)

    return pencilSketchImage

def cartoonify_DEBUG(image):
    # edge-preserving smoothing filter
    image = cv2.bilateralFilter(src=image, d=15, sigmaColor=80, sigmaSpace=80)
    return image

def pencilSketch_DEBUG(image):
    image = cv2.blur(image,(5,5))
    image = cv2.Laplacian(image, cv2.CV_32F, ksize = 3, scale = 1, delta = 0)

    print(image.dtype)  # float32

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(image.dtype)  # float32
    
    th, image = cv2.threshold(image, thresh=10, maxval=255, type=cv2.THRESH_BINARY_INV)

    # cv2.normalize(image, dst = image, alpha = 0, beta = 1, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)

    return image

if __name__ == "__main__":
    imagePath = "project1/trump.jpg"
    image = cv2.imread(imagePath)

    # cartoonImage = cartoonify(image)
    # pencilSketchImage = pencilSketch(image)

    cartoonImage = cartoonify_DEBUG(image)
    pencilSketchImage = pencilSketch_DEBUG(image)

    print(cartoonImage.shape)
    print(pencilSketchImage.shape)

    image = cartoonImage + pencilSketchImage

    plt.figure(figsize=[20,10])
    plt.subplot(131);plt.imshow(image[:,:,::-1]);
    plt.subplot(132);plt.imshow(cartoonImage[:,:,::-1]);
    plt.subplot(133);plt.imshow(image);
    plt.show()
