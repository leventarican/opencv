# Binary Image Processing
# Contour Analysis

# what are contours? 
# contours are boundaries of objects. contours are different from edges.
# in case of contours we know the connectivity of the edge pixels.

# used algorithms: radial sweep, ...

# in OpenCV find contours is implemented in function findContours()
# input: image, mode, approximation algorithm
# - there are four modes: RETR_EXTERNAL, RETR_LIST, RETR_CCOMP, (retrieve connected component), RETR_TREE
# outout: array of countour pixels, hierarchy info: next, previous, first_child, parent

# OpenCV function approxPolyDP(): approximate polygon dynamic programming
# it takes a curve and creates an approximate polygon
# example: you have the contour of a DINA4 page and applying this function will return the four corner points

# Contours are simply the boundaries of an object or part of object in an image. 
# They are useful in shape analysis and object Detection/Recognition using traditional Computer Vision algorithms.

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def loadImage():
    imagePath = "week3/contour.png"
    image = cv2.imread(imagePath)
    imageCopy = image.copy()
    # Convert to grayscale
    imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    return image, imageGray

def displayImages(image, imageGray):
    plt.figure()
    plt.subplot(121)
    plt.imshow(image[:,:,::-1])
    plt.title("Original Image");
    plt.subplot(122)
    plt.imshow(imageGray)
    plt.title("Grayscale Image");
    plt.show()

# using OpenCV function findContours()
# mode - Contour retrieval mode, ( RETR_EXTERNAL, RETR_LIST, RETR_CCOMP, RETR_TREE )
# method - Contour approximation method. ( CHAIN_APPROX_NONE, CHAIN_APPROX_SIMPLE, CHAIN_APPROX_TC89_L1 etc )
# https://docs.opencv.org/4.1.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0
def findContour(imageGray):
    """
    docstring
    """
    # Find all contours in the image
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    print(f"Number of contours found = {len(contours)}")
    print(f"\nHierarchy : \n{hierarchy}")

    return contours, hierarchy

def drawContours(image, contours):
    """
    Contours are simply an array of pixel locations.
    """
    # Draw all the contours
    cv2.drawContours(image, contours, -1, (0,255,0), 3);
    plt.imshow(image[:,:,::-1])
    plt.show()

if __name__ == "__main__":
    image, imageGray = loadImage()
    # displayImages(image, imageGray)
    contours,_ = findContour(imageGray)
    drawContours(image, contours)
