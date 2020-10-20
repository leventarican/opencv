import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# bitwise example
# https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
# https://docs.opencv.org/master/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14

def run():
    """
    same application as in application-sunglass-filter/application.py.
    same steps, but instead of arithmetic operations like MULTIPLY & ADD, 
    we will use bitwise operations like AND, NOT and OR.
    """
    lion = cv2.imread('lion.jpg')
    # lion = np.float32(lion)/255
    lionBitwise = lion.copy()
    glass = cv2.imread('sunglass.png', -1)
    # glass = np.float32(glass)/255

    print(lionBitwise.dtype)
    print(glass.dtype)

    # check also resize-image.py
    # dst	=	cv.resize(	src, dsize[, dst[, fx[, fy[, interpolation]]]]	)
    # https://docs.opencv.org/4.1.0/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d
    dsize = (300, 100)
    glass = cv2.resize(glass, dsize)
    print(f"image Dimension = {glass.shape}")
    # image Dimension = (300, 300, 4)

    glassBGR = glass[:,:,0:3]
    glassMask1 = glass[:,:,3]
    print(f"image Dimension = {glassBGR.shape}")
    print(f"image Dimension = {glassMask1.shape}")
    print(f"image Dimension = {lionBitwise.shape}")

    # plt.figure(figsize=[15,15])
    # plt.subplot(121);plt.imshow(glassBGR[:,:,::-1]);plt.title('Color channels');
    # plt.subplot(122);plt.imshow(glassMask1,cmap='gray');plt.title('Alpha channel');
    
    # our dsize is (300,100)
    # our ROI has to match -> row: 200-100=100; col: 370-70=300
    eyeROI = lionBitwise[100:200, 70:370]
    glassMask = cv2.merge((glassMask1,glassMask1,glassMask1))

    # bitwise operation: AND, NOT
    eye = cv2.bitwise_and(eyeROI,cv2.bitwise_not(glassMask))
    # bitwise operation: AND
    sunglass = cv2.bitwise_and(glassBGR,glassMask)
    # bitwise operation: OR
    eyeRoiFinal = cv2.bitwise_or(eye, sunglass)

    # Replace the eye ROI with the output from the previous section
    lionBitwise[100:200,70:370] = eyeRoiFinal

    plt.figure(figsize=[20,20])
    plt.subplot(151);plt.imshow(eye[:,:,::-1]);plt.title("Masked Eye Region");
    plt.subplot(152);plt.imshow(sunglass[:,:,::-1]);plt.title("Masked Sunglass");
    plt.subplot(153);plt.imshow(np.uint8(eyeRoiFinal)[:,:,::-1]);plt.title("Combined Eye Region");
    plt.subplot(154);plt.imshow(lion[:,:,::-1]); plt.title("Original Image");
    plt.subplot(155);plt.imshow(lionBitwise[:,:,::-1]);plt.title("With Sunglasses");

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'

    run()

    plt.show()