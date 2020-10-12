# ##############################################################################
# contrast enhancement
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def contrast_enhancement(image):
    """
    to improve contrast: out_image = alpha * in_image 
    """
    contrastPercentage = 50.0

    # Multiply with scaling factor to increase contrast
    contrastHigh = image * (1+contrastPercentage/100)

    # plt.figure(figsize=[20,20])
    # plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("original Image");
    # plt.subplot(122);plt.imshow(contrastHigh[...,::-1]);plt.title("High Contrast");

    print(f"Original Image Datatype : {image.dtype}")
    print(f"Contrast Image Datatype : {contrastHigh.dtype}")
    print(f"Original Image Highest Pixel Intensity : {image.max()}")
    print(f"Contrast Image Highest Pixel Intensity : {contrastHigh.max()}")

    # Original Image Datatype : uint8
    # Contrast Image Datatype : float64
    # Original Image Highest Pixel Intensity : 255
    # Contrast Image Highest Pixel Intensity : 382.5

    # because of contrastHigh image is in float format anything above 255 is considered as white.
    # If the image is in float datatype, then the range should be [0,1]
    # If the image is in int datatype, then the range should be [0,255]

    # Clip the values to [0,255] and change it back to uint8 for display
    clippedContrastImage = np.clip(contrastHigh, 0, 255)
    contrastHighClippedUint8 = np.uint8(clippedContrastImage)

    # Convert the range to [0,1] and keep it in float format (=Normalize the instensity values)
    contrastHighNormalized = (image * (1+contrastPercentage/100))/255
    contrastHighNormalized01Clipped = np.clip(contrastHighNormalized,0,1)

    plt.figure(figsize=[20,20])
    plt.subplot(131);plt.imshow(image[...,::-1]);plt.title("original Image");
    plt.subplot(132);plt.imshow(contrastHighClippedUint8[...,::-1]);plt.title("converted back to uint8");
    plt.subplot(133);plt.imshow(contrastHighNormalized01Clipped[...,::-1]);plt.title("Normalized float to [0, 1]");

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'
    
    image = cv2.imread('lion.jpg')

    contrast_enhancement(image)

    plt.show()
