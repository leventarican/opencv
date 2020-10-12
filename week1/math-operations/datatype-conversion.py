# ##############################################################################
# datatype conversion
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def datatype_conversion(image):
    """
    an image is represented as a numpy array once it's read using cv2.imread function.
    default datatype of this object is unsigned integer (8 bits).

    for most Arithmentic operations like multiplication or division, 
    we need to convert the array type to floating point with each pixel having 
    16, 32 or 64 bits of data. This helps prevent overflow while working with the images.
    """
    print(image.dtype)
    # uint8

    # convert unsigned int to float
    image = np.float32(image)
    print(image.dtype)
    # float32

    scalingFactor = 1/255.0
    # scale the values so that they lie between [0,1]
    image = image * scalingFactor

    # convert back to unsigned int
    # range 0-1 to 0-255
    image = image * (1.0/scalingFactor)
    image = np.uint8(image)

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'
    
    image = cv2.imread('lion.jpg')

    datatype_conversion(image)

    plt.show()
