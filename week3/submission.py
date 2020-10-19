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

def createADemoImage():
    """
    create an empty matrix.
    add some white blobs on to image.
    """
    global im

    im = np.zeros((10,10),dtype='uint8')
    print(im);
    # plt.imshow(im)
    # plt.show()

    im[0,1] = 1
    im[-1,0]= 1
    im[-2,-1]=1
    im[2,2] = 1
    im[5:8,5:8] = 1

    print(im)
    # plt.imshow(im); plt.show()

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

# instead of working with max value you work with the min value.
def erosionMethod2():
    """
    Implement erosion from scratch.
    """
    border = ksize//2
    paddedIm = np.zeros((height + border*2, width + border*2))
    paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
    paddedDilatedIm = paddedIm.copy()

    # plt.imshow(paddedIm);plt.show()

    # Create a VideoWriter object
    # Use frame size as 50x50
    ###
    ### YOUR CODE HERE
    ###
    # out = cv2.VideoWriter('week3/dilationScratch.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (50, 50))

    for h_i in range(border, height+border):
        for w_i in range(border,width+border):
            ###
            ### YOUR CODE HERE
            ###
            row = (h_i - border, h_i + border + 1)
            col = (w_i - border, w_i + border + 1)
            # print(row)
            # print(col)
            # tmp = paddedDilatedIm[row[0]:row[1], col[0]:col[1]]
            # tmp = paddedIm[row[0]:row[1], col[0]:col[1]]
            paddedDilatedIm[row[0]:row[1], col[0]:col[1]] =\
                cv2.bitwise_and(paddedIm[row[0]:row[1], col[0]:col[1]], element)
            # plt.imshow(paddedIm[row[0]:row[1], col[0]:col[1]]); plt.show()
            # plt.imshow(paddedDilatedIm); plt.show()
            # return
            # Resize output to 50x50 before writing it to the video
            ###
            ### YOUR CODE HERE
            ###

            # Convert resizedFrame to BGR before writing
            ###
            ### YOUR CODE HERE
            ###
            # imBGR = cv2.cvtColor(imResized, cv2.COLOR_RGB2BGR)
            # th, dst = cv2.threshold(imBGR, 1, 255, cv2.THRESH_BINARY)

    # Release the VideoWriter object
    ###
    ### YOUR CODE HERE
    ###
    # out.release()

    # Display final image (cropped)
    ###
    ### YOUR CODE HERE
    ###
    # paddedDilatedIm = paddedDilatedIm[1:10, 1:10]
    plt.imshow(paddedDilatedIm); plt.show()

    plt.figure(figsize=[20,20])
    plt.subplot(131);plt.imshow(im);plt.title("im");
    plt.subplot(132);plt.imshow(paddedIm);plt.title("padded");
    plt.subplot(133);plt.imshow(paddedDilatedIm);plt.title("padded dilated");
    plt.show()

def dilationMethod2():
    """
    the characteristic in this method 
    is the copying the maximium (pixel) value of the kernel 
    over to the middle pixel of the image
    """
    global ksize, height, width, element, im

    border = ksize//2   # // cast to integer
    print(f"copy image with border: {border}")
    # copy image with border: 1

    # Create a padded image with zeros padding
    # why are we doing this? to make space for the kernel

    # padded image method 2: with OpenCV copyMakeBorder function
    # The function copies the source image into the middle of the destination image. 
    # The areas to the left, to the right, above and below the copied source image will be filled with extrapolated pixels.
    # dst	=	cv.copyMakeBorder(	src, top, bottom, left, right, borderType[, dst[, value]]	)
    # https://docs.opencv.org/4.1.0/d2/de8/group__core__array.html#ga2ac1049c2c3dd25c2b41bffe17658a36
    paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
    # plt.imshow(paddedIm);plt.show()

    paddedHeight, paddedWidth = paddedIm.shape[:2]
    print(f"padded image height: {paddedHeight}; width: {paddedWidth}")
    # padded image height: 12; width: 12
    
    maxValue = np.max(element)
    print(f"maximum value: {maxValue}")
    # maximum value: 1

    out = cv2.VideoWriter('dilation.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (50, 50))

    # go through padded image pixel by pixel. from left to right (col). then next row.
    # our reference is im, but we move on paddedim
    for h_i in range(border, height+border):
        for w_i in range(border, width+border):
            # when you find a white pixel in neighborhood (ellipse): top, bottom, left, right
            if paddedIm[h_i-1, w_i]:
                im[h_i-1, w_i-1] = 255
            elif paddedIm[h_i+1, w_i]:
                im[h_i-1, w_i-1] = 255
            elif paddedIm[h_i, w_i-1]:
                im[h_i-1, w_i-1] = 255
            elif paddedIm[h_i, w_i+1]:
                im[h_i-1, w_i-1] = 255
            
            imResized = cv2.resize(im, (50, 50), interpolation=cv2.INTER_LINEAR)
            imBGR = cv2.cvtColor(imResized, cv2.COLOR_RGB2BGR)
            out.write(imBGR)
            result = paddedIm
            # plt.imshow(imBGR);plt.show()

    plt.imshow(im);plt.show()
    out.release()

if __name__ == "__main__":
    createADemoImage()
    createEllipseStructuringElement()
    erosionMethod2()
    # dilationMethod2()
