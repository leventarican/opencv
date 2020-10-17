import cv2, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# thresholding: convert grayscale to binary image based on intensity of pixels
# example, when using text recognition algorithm

# binary thresholding
# inverse binary thresholding
# truncate thresholding; truncate: shorten something
# threshold to zero
# inverted threshold to zero

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

# Read an image in grayscale
imagePath = 'threshold.png'
src = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

# Set threshold and maximum value
thresh = 100
maxValue = 255

# threshold option 0: operation took ~1s
def thresholdUsingLoop(src, thresh, maxValue):
    # Create a output image
    dst = src.copy()
    height,width = src.shape[:2]

    # Loop over rows
    for i in range(height):
        # Loop over columns
        for j in range(width):
            if src[i,j] > thresh:
                dst[i,j] = maxValue
            else:
                dst[i,j] = 0
                
    return dst

# threshold option 1: use vectorized computation available in numpy to make it more efficient 
def thresholdUsingVectors(src, thresh, maxValue):
    # array of zeros: black output
    dst = np.zeros_like(src)
    
    # Find pixels which have values>threshold value
    thresholdedPixels = src>thresh
    
    # Assign those pixels maxValue
    dst[thresholdedPixels] = maxValue
    
    return dst

# threshold option 2: with opencv
# retval, dst = cv.threshold(src, thresh, maxval, type[, dst])
# https://docs.opencv.org/4.1.0/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
def thresholdUsingOpenCV(src, thresh, maxValue):
    th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
    return th, dst

# compute average time for 10 samples
def compareThresholdImplementations():
    time_opencv = 0
    time_loops = 0
    time_vector = 0
    n_samples = 10
    for i in range(n_samples):
        
        t = time.time()
        dst = thresholdUsingLoop(src, thresh, maxValue)
        time_loops += time.time() - t
        
        t = time.time()
        dst = thresholdUsingVectors(src, thresh, maxValue)
        time_vector += time.time() - t
        
        t = time.time()
        th, dst = thresholdUsingOpenCV(src, thresh, maxValue)
        time_opencv += time.time() - t

    print("Average time taken by For Loop Code = {} seconds".format(time_loops/n_samples))
    print("Average time taken by Vectorized Code = {} seconds".format(time_vector/n_samples))
    print("Average time taken by OpenCV Code = {} seconds".format(time_opencv/n_samples))
    # Average time taken by For Loop Code = 1.0107741117477418 seconds
    # Average time taken by Vectorized Code = 0.0002928733825683594 seconds
    # Average time taken by OpenCV Code = 0.00012979507446289062 seconds

def executeThresholdImplementation(impl):
    t = time.time()

    if impl == 0:
        dst = thresholdUsingLoop(src, thresh, maxValue)
    elif impl == 1:
        dst = thresholdUsingVectors(src, thresh, maxValue)
    elif impl == 2:
        dst = thresholdUsingOpenCV(src, thresh, maxValue)

    print("Time taken = {} seconds".format(time.time() - t))

    plt.figure(figsize=[15,15])
    plt.subplot(121);plt.imshow(src);plt.title("Original Image");
    plt.subplot(122);plt.imshow(dst);plt.title("Thresholded Image");
    plt.show()

def binaryThresholding(src, thresh, maxValue):
    """
    docstring
    """
    th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
    return dst

def inverseBinaryThresholding(src, thresh, maxValue):
    """
    docstring
    """
    th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY_INV)
    return dst

def truncateThresholding(src, thresh, maxValue):
    """
    docstring
    """
    th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TRUNC)
    return dst

def thresholdToZero(src, thresh, maxValue):
    """
    docstring
    """
    th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO)
    return dst

def invertedThresholdToZero(src, thresh, maxValue):
    """
    docstring
    """
    th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_TOZERO_INV)
    return dst

def displayAndCompare():
    """
    docstring
    """

    dst_bin = binaryThresholding(src, thresh, maxValue)
    dst_bin_inv = inverseBinaryThresholding(src, thresh, maxValue)
    dst_trunc = truncateThresholding(src, thresh, maxValue)
    dst_to_zero = thresholdToZero(src, thresh, maxValue)
    dst_to_zero_inv = invertedThresholdToZero(src, thresh, maxValue)

    print("Threshold Value = {}, Max Value = {}".format(thresh, maxValue))
    plt.figure(figsize=[20,12])
    plt.subplot(231);plt.imshow(src, cmap='gray', vmin=0, vmax=255);plt.title("Original Image");
    plt.subplot(232);plt.imshow(dst_bin, cmap='gray', vmin=0, vmax=255);plt.title("Threshold Binary");
    plt.subplot(233);plt.imshow(dst_bin_inv, cmap='gray', vmin=0, vmax=255);plt.title("Threshold Binary Inverse");
    plt.subplot(234);plt.imshow(dst_trunc, cmap='gray', vmin=0, vmax=255);plt.title("Threshold Truncate");
    plt.subplot(235);plt.imshow(dst_to_zero, cmap='gray', vmin=0, vmax=255);plt.title("Threshold To Zero");
    plt.subplot(236);plt.imshow(dst_to_zero_inv, cmap='gray', vmin=0, vmax=255);plt.title("Threshold To Zero Inverse");
    plt.show()

if __name__ == "__main__":
    # executeThresholdImplementation(2)
    # compareThresholdImplementations()
    displayAndCompare()
