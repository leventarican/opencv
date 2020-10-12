# ##############################################################################
# brightness enhancement
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def brightness_enhancement(image):
    """
    to improve brightness: out_image = beta + in_image 
    """
    brightnessOffset = 50
    brightHigh = image + brightnessOffset

    # this result looks strange hmm!?
    # plt.figure(figsize=[20,20])
    # plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("original Image");
    # plt.subplot(122);plt.imshow(brightHigh[...,::-1]);plt.title("High brightness");

    print(f"Original Image Datatype : {image.dtype}")
    print(f"brightness Image Datatype : {brightHigh.dtype}")
    print(f"Original Image Highest Pixel Intensity : {image.max()}")
    print(f"brightness Image Highest Pixel Intensity : {brightHigh.max()}")

    # the problem is that we have an overflow:
    # since the value range is 0-255 (unsingned int 8) and we add 50 to each pixel 

def example():
    """
    understand overflow
    """
    a = np.array([[100, 110], [120, 130]], dtype='uint8')
    print(a)
    # [[100 110]
    # [120 130]]

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'
    
    image = cv2.imread('lion.jpg')

    # brightness_enhancement(image)
    example()

    plt.show()
