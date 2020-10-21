# In this assignment, you will implement erosion and dilation from scratch using Method 2

# Method 2:
# Scan through the image and superimpose the kernel on the neighborhood of each pixel.
# Perform an AND operation of the neighborhood with the kernel.
# Replace the pixel value with the maximum value in the neighborhood given by the kernel.

# This means that you check every pixel and its neighborhood with respect to the kernel 
# and change the pixel to white if any of the pixel in this neighborhood is white. 
# OpenCV implements an optimized version of this method. 
# This will work even if the image is not a binary image.

# You will implement this method for both Dilation and Erosion in the assignment. 
# We will provide hints along with the assignment.

# this method is applied also in OpenCV function
# and works not only for binary images. also for greyscale images.

# Grading Rubric
# 1. Implement erosion from scratch - 8 marks
# 2. Display the final (correct) image - 2 marks
# 3. Create a video of intermediate steps of erosion using VideoWriter - 5 marks

# 4. Implement dilation from scratch - 8 marks
# 5. Display the final (correct) image - 2 marks
# 6. Create a video of intermediate steps of dilation using VideoWriter - 5 marks

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def createBinaryImage():
    """
    create an empty matrix.
    add some white blobs on to image.
    """
    im = np.zeros((10,10),dtype='uint8')
    im[0,1] = 1
    im[-1,0]= 1
    im[-2,-1]=1
    im[2,2] = 1
    im[5:8,5:8] = 1

    print(im)
    # plt.imshow(im); plt.show()

    return im

def createEllipseStructuringElement():
    """
    create a 3x3 ellipse structuring element.
    """
    global im, ksize, height, width, element

    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    print(element)
    # [[0 1 0]
    # [1 1 1]
    # [0 1 0]]
    print(element.shape)
    # (3, 3)
    
    ksize = element.shape[0]
    print(f"kernel size: {ksize}")
    # kernel size: 3

    height,width = im.shape[:2]
    print(f"image height: {height}; width: {width}")
    # image height: 10; width: 10

def erosionWithOpenCV(im):
    ErodedEllipseKernel = cv2.erode(im, element)

    # print(ErodedEllipseKernel)
    # plt.imshow(ErodedEllipseKernel);
    # plt.show()

# instead of working with max value you work with the min value.
def erosionMethod2(im):
    border = ksize//2
    paddedIm = np.zeros((height + border*2, width + border*2))
    # fill border with value = 1
    paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 1)
    paddedErodedIm = paddedIm.copy()

    print(im)
    print(paddedErodedIm)

    # Create a VideoWriter object
    # Use frame size as 50x50
    ###
    ### YOUR CODE HERE
    ###
    out = cv2.VideoWriter('week3/erosionScratch.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (50, 50))

    for h_i in range(border, height+border):
        for w_i in range(border,width+border):
            ###
            ### YOUR CODE HERE
            ###
            row = (h_i - border, (h_i + border)+1)
            col = (w_i - border, (w_i + border)+1)
            dst = cv2.bitwise_and(src1=paddedIm[row[0]:row[1], col[0]:col[1]], src2=element)
            # dst = cv2.bitwise_and(src1=paddedIm[6:9, 6:9], src2=element)
            # on im[6:9, 6:9] we have only 1 values. the min of these are 1
            # 1 1 1     0 1 0
            # 1 1 1 ->  1 1 1
            # 1 1 1     0 1 0
            values = [dst[1][1], dst[0][1], dst[1][2], dst[2][1], dst[1][0]]
            minPixelValue = min(values)
            paddedErodedIm[row[0]+1:row[1]-1, col[0]+1:col[1]-1] = minPixelValue

            # Resize output to 50x50 before writing it to the video
            ###
            ### YOUR CODE HERE
            ###
            resized = cv2.resize(paddedErodedIm, dsize=(50,50), interpolation=cv2.INTER_LINEAR)

            # Convert resizedFrame to BGR before writing
            ###
            ### YOUR CODE HERE
            ###
            retval, dst = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY)
            imBGR = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
            out.write(imBGR)

    # Release the VideoWriter object
    ###
    ### YOUR CODE HERE
    ###
    # out.release()

    # Display final image (cropped)
    ###
    ### YOUR CODE HERE
    ###
    paddedErodedIm = paddedErodedIm[1:11, 1:11]
    print(paddedErodedIm)
    plt.imshow(paddedErodedIm); plt.show()

# ~ maximize
def dilationMethod2(im):
    """
    Implement erosion from scratch.
    """
    border = ksize//2
    paddedIm = np.zeros((height + border*2, width + border*2))
    paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
    paddedDilatedIm = paddedIm.copy()

    # Create a VideoWriter object
    # Use frame size as 50x50
    ###
    ### YOUR CODE HERE
    ###
    out = cv2.VideoWriter('week3/dilationScratch.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (50, 50))

    for h_i in range(border, height+border):
        for w_i in range(border,width+border):
            ###
            ### YOUR CODE HERE
            ###
            # 3x3
            row = (h_i - border, (h_i + border)+1)
            col = (w_i - border, (w_i + border)+1)
            dst = cv2.bitwise_and(src1=paddedIm[row[0]:row[1], col[0]:col[1]], src2=element)
            values = [dst[1][1], dst[0][1], dst[1][2], dst[2][1], dst[1][0]]
            maxPixelValue = max(values)
            paddedDilatedIm[row[0]+1:row[1]-1, col[0]+1:col[1]-1] = maxPixelValue

            # Resize output to 50x50 before writing it to the video
            ###
            ### YOUR CODE HERE
            ###
            resized = cv2.resize(paddedDilatedIm, dsize=(50,50), interpolation=cv2.INTER_LINEAR)

            # Convert resizedFrame to BGR before writing
            ###
            ### YOUR CODE HERE
            ###
            retval, dst = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY)
            # paddedDilatedIm = 255 * paddedDilatedIm
            # cv2.add(paddedDilatedIm,254))
            imBGR = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
            
            out.write(imBGR)

    # Release the VideoWriter object
    ###
    ### YOUR CODE HERE
    ###
    out.release()

    # Display final image (cropped)
    ###
    ### YOUR CODE HERE
    ###
    paddedDilatedIm = paddedDilatedIm[1:11, 1:11]
    plt.imshow(paddedDilatedIm); plt.show()

if __name__ == "__main__":
    im = createBinaryImage()
    createEllipseStructuringElement()
    # erosionWithOpenCV(im)
    erosionMethod2(im)
    dilationMethod2(im)
