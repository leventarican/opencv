# morpological operation on binary images
# combining erosion and dilation operations

# Opening refers Erosion followed by Dilation and these operations is used for clearing white blobs and
# Closing refers Dilation followed by Erosion and are used for clearing black holes

# remember: erosion removes white region and dilation adds white region. 
# Thus, if we want to remove small white spots, perform erosion followed by dilation
# Similarly remove black spots using dilation followed by erosion.

# in OpenCV the opening and closing operations are implemented using MorphologyEx function
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html?fbclid=IwAR1GtoDsIv4Fi8o7vrZ8SGb3bb1uiU_Nyt94fc9J2sHKF7FlbDNT1fq-kI0#ga67493776e3ad1a3df63883829375201f

# Openening
# imageMorphOpened = cv2.morphologyEx( src, cv2.MORPH_OPEN, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )

# Closing
# imageMorphClosed = cv2.morphologyEx( src, cv2.MORPH_CLOSE, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def loadImageOpening():
    image = cv2.imread("opening.png", cv2.IMREAD_GRAYSCALE)

    # Check for invalid input
    if image is None:  
        print("Could not open or find the image")
    # plt.imshow(image)
    # plt.show()

    return image

def loadImageClosing():
    # Image taken as input
    image = cv2.imread("closing.png", cv2.IMREAD_GRAYSCALE)

    # Check for invalid input
    if image is None:  
        print("Could not open or find the image")
    plt.imshow(image)
    plt.show()

    return image

def method1Opening(image):
    """
    Opening : Method 1 - Using combination of Erosion and Dilation
    """
    # Specify Kernel Size
    kernelSize = 10

    # Create the Kernel
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*kernelSize+1, 2*kernelSize+1),\
        (kernelSize, kernelSize))

    # Perform Erosion
    imEroded = cv2.erode(image, element, iterations=1)
    # Perform Dilation
    imOpen = cv2.dilate(imEroded, element, iterations=1)

    # Display Kernel
    # plt.imshow(element);plt.title(f"Structuring Element : Ellipse, Kernel Size : {kernelSize}");
    # plt.show()

    # Display Output
    plt.figure(figsize=[15,15])
    plt.subplot(131);plt.imshow(image);plt.title("Original Image")
    plt.subplot(132);plt.imshow(imEroded,cmap='gray');plt.title("After Erosion Operation")
    plt.subplot(133);plt.imshow(imOpen,cmap='gray');plt.title("After Dilation Operation");
    plt.show()

def method2Opening(image):
    """
    Opening : Method 2 - Using MorphologyEx function with MORPH_OPEN
    """
    # Get structuring element/kernel which will be used 
    # for opening operation
    openingSize = 3

    # Selecting a elliptical kernel
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,\
        (2 * openingSize + 1, 2 * openingSize + 1),\
            (openingSize,openingSize))

    imageMorphOpened = cv2.morphologyEx(image, cv2.MORPH_OPEN, 
                            element,iterations=3)

    plt.figure(figsize=[15,15])
    plt.subplot(121);plt.imshow(image);plt.title("Original Image")
    plt.subplot(122);plt.imshow(imageMorphOpened);plt.title("After Opening Operation")
    plt.show()

def method1Closing(image):
    """
    Closing : Method 1 - Using combination of Dilation and Erosion
    """
    # Specify Kernel Size
    kernelSize = 10

    # Create Kernel
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*kernelSize+1, 2*kernelSize+1),\
        (kernelSize, kernelSize))

    # Perform Dilation
    imDilated = cv2.dilate(image, element)
    # Perform Erosion
    imClose = cv2.erode(imDilated, element)

    plt.figure(figsize=[15,15])
    plt.subplot(131);plt.imshow(image);plt.title("Original Image")
    plt.subplot(132);plt.imshow(imDilated,cmap='gray');plt.title("After Dilation Operation")
    plt.subplot(133);plt.imshow(imClose,cmap='gray');plt.title("After Erosion Operation")
    plt.show()

def method2Closing(image):
    """
    Closing : Method 2 - Using MorphologyEx function with MORPH_CLOSE
    """

    # Get structuring element/kernel 
    # which will be used for closing operation
    closingSize = 10

    # Selecting an elliptical kernel 
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                (2 * closingSize + 1, 2 * closingSize + 1),
                (closingSize,closingSize))

    imageMorphClosed = cv2.morphologyEx(image,\
        cv2.MORPH_CLOSE, element)

    plt.figure(figsize=[15,15])
    plt.subplot(121);plt.imshow(image);plt.title("Original Image")
    plt.subplot(122);plt.imshow(imageMorphClosed,cmap='gray');plt.title("After Closing Operation")
    plt.show()

if __name__ == "__main__":

    # Objective: We want to remove the small white blobs while keeping the the bigger blobs intact
    # image = loadImageOpening()
    # method1Opening(image)
    # method2Opening(image)

    # Objective: We want to remove the small black spots while keeping the the bigger black hole intact
    image = loadImageClosing()
    method1Closing(image)
    method2Closing(image)
