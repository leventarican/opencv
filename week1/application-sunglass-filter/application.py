# ##############################################################################
# put the a (png) glass image on top of the eye region (of another image)
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def naive_replace():
    """
    load images; png with 4. channel (= alpha), resize mask image, separate channels, ...
    """
    lion = cv2.imread('lion.jpg')
    lion = np.float32(lion)/255

    # cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
    # cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
    # cv2.IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
    glass = cv2.imread('sunglass.png', -1)
    # resize image; check resize-image.py
    glass = np.float32(glass)/255
    glass = cv2.resize(glass, None, fx=0.5, fy=0.5)

    # separate color and alpha channel
    glassBGR = glass[:,:,0:3]
    glassMASK = glass[:,:,3]

    # top left corner of the glasses
    topLeftRow = 30
    topLeftCol = 60
    bottomRightRow = topLeftRow + glassHeight
    bottomRightCol = topLeftCol + glassWidth

    glassHeight, glassWidth, nChannels = glass.shape
    print(f"glass dimension ={glass.shape}")

    # Replace the eye region with the sunglass image
    lionWithGlassesNaive = lion.copy()
    lionWithGlassesNaive[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]=glassBGR

    plt.figure(figsize=[20,20])
    plt.subplot(151);plt.imshow(lion[...,::-1]);
    plt.subplot(152);plt.imshow(glass[...,::-1]);
    plt.subplot(153);plt.imshow(glassBGR[...,::-1]);
    plt.subplot(154);plt.imshow(glassMASK, cmap='gray');
    plt.subplot(155);plt.imshow(lionWithGlassesNaive[:,:,::-1])

def artihmetic_replace():
    """
    1. Create an alpha mask with 3-channels using the single channel mask.
    2. Extract the eye region from the face image
    3. Multiply the Mask with the sunglass to get the masked sunglass
    4. Multiply the negative of Mask with the eye region to create a hole in the eye region for the sunglass to be placed.
    5. Add the masked sunglass and eye regions to get the combined eye region with the sunglass.
    6. Replace the eye region in the original image with that of the output we got in the previous step. This is the final output
    """
    lion = cv2.imread('lion.jpg')
    lion = np.float32(lion)/255

    glass = cv2.imread('sunglass.png', -1)
    glass = np.float32(glass)/255
    glass = cv2.resize(glass, None, fx=0.5, fy=0.5)

    glassBGR = glass[:,:,0:3]
    glassMASK1 = glass[:,:,3]

    topLeftRow = 30
    topLeftCol = 60
    bottomRightRow = topLeftRow + glassHeight
    bottomRightCol = topLeftCol + glassWidth

    # 1. Create an alpha mask with 3-channels using the single channel mask.
    # check split-merge.py
    glassMASK = cv2.merge((glassMASK1,glassMASK1,glassMASK1))

    # 2. Extract the eye region from the face image
    # we did that in copy-region.py
    lionWithGlasses = lion.copy()
    eyeROI = lionWithGlasses[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]

    # 3. Multiply the Mask with the sunglass to get the masked sunglass


    plt.figure(figsize=[20,20])
    plt.subplot(151);plt.imshow(lion[...,::-1]);
    plt.subplot(152);plt.imshow(glass[...,::-1]);
    plt.subplot(153);plt.imshow(glassBGR[...,::-1]);
    plt.subplot(154);plt.imshow(glassMASK, cmap='gray');
    # plt.subplot(155);plt.imshow(lionWithGlassesNaive[:,:,::-1])

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'
    matplotlib.rcParams['image.interpolation'] = 'bilinear'

    # naive_replace()
    artihmetic_replace()

    plt.show()
