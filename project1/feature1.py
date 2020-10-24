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
    # edge-preserving smoothing filter
    cartoonImage = cv2.bilateralFilter(src=image, d=15, sigmaColor=80, sigmaSpace=80)
    return cartoonImage

def pencilSketch(image, arguments=0):
    
    ### YOUR CODE HERE
    image = cv2.blur(image,(5,5))
    image = cv2.Laplacian(image, cv2.CV_8U, ksize = 3, scale = 1, delta = 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binaryImage = cv2.threshold(image, thresh=10, maxval=255, type=cv2.THRESH_BINARY_INV)
    pencilSketchImage = cv2.cvtColor(binaryImage, cv2.COLOR_GRAY2BGR)
    return pencilSketchImage

# convert a RGB image into a cartoon
if __name__ == "__main__":
    imagePath = "project1/trump.jpg"
    image = cv2.imread(imagePath)

    cartoonImage = cartoonify(image)
    pencilSketchImage = pencilSketch(image)

    # print(cartoonImage.shape)
    # print(pencilSketchImage.shape)
    # print(cartoonImage.dtype)
    # print(pencilSketchImage.dtype)

    cartoonImage = cv2.bitwise_and(cartoonImage, pencilSketchImage)

    plt.figure(figsize=[20,10])
    plt.subplot(131);plt.imshow(image[:,:,::-1]);plt.title("original");
    plt.subplot(132);plt.imshow(pencilSketchImage[:,:,::-1]);plt.title("pencil sketch");
    plt.subplot(133);plt.imshow(cartoonImage[:,:,::-1]);plt.title("cartoon");
    plt.show()
