# Connected Components Analysis - CCA
# connected components are simple blobs
# blobs: collection of white pixels connected each other.

# behind the scenes the _two pass algorithm_ is applied

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def loadImage():
    """
    Read image as grayscale
    """
    im = cv2.imread("truth.png", cv2.IMREAD_GRAYSCALE)
    # plt.imshow(im)
    # plt.show()

    return im

def findConnectedComponents(im):
    # Threshold Image
    th, imThresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)

    # Find connected components
    _, imLabels = cv2.connectedComponents(imThresh)
    # plt.imshow(imLabels)
    # plt.show()

    return imLabels

def displayEachLabel(imLabels):
    nComponents = imLabels.max()

    displayRows = np.ceil(nComponents/3.0)
    plt.figure(figsize=[20,12])
    for i in range(nComponents+1):
        plt.subplot(displayRows,3,i+1)
        plt.imshow(imLabels==i)
        if i == 0:
            plt.title(f"Background, Component ID : {i}")
        else:
            plt.title(f"Component ID : {i}")
        plt.show()

def applyColormap(imLabels):
    """
    OpenCV defines 12 colormaps that can be applied to a grayscale image 
    using the function applyColorMap to produce a pseudocolored image.
    """
    # The following line finds the min and max pixel values
    # and their locations on an image.
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imLabels)

    # Normalize the image so that the min value is 0 and max value is 255.
    imLabels = 255 * (imLabels - minVal)/(maxVal-minVal)

    # Convert image to 8-bits unsigned type
    imLabels = np.uint8(imLabels)

    # Apply a color map
    imColorMap = cv2.applyColorMap(imLabels, cv2.COLORMAP_JET)
    plt.imshow(imColorMap[:,:,::-1])
    plt.show()

if __name__ == "__main__":
    image = loadImage()
    imLabels = findConnectedComponents(image)
    # displayEachLabel(imLabels)
    applyColormap(imLabels)
