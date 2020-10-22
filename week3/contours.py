# Binary Image Processing
# Contour Analysis

# what are contours? 
# contours are boundaries of objects. contours are different from edges.
# in case of contours we know the connectivity of the edge pixels.

# used algorithms: radial sweep, ...

# in OpenCV find contours is implemented in function findContours()
# input: image, mode, approximation algorithm
# - there are four modes: RETR_EXTERNAL, RETR_LIST, RETR_CCOMP, (retrieve connected component), RETR_TREE
# outout: array of countour pixels, hierarchy info: next, previous, first_child, parent

# OpenCV function approxPolyDP(): approximate polygon dynamic programming
# it takes a curve and creates an approximate polygon
# example: you have the contour of a DINA4 page and applying this function will return the four corner points

# Contours are simply the boundaries of an object or part of object in an image. 
# They are useful in shape analysis and object Detection/Recognition using traditional Computer Vision algorithms.

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def loadImage():
    imagePath = "week3/contour.png"
    image = cv2.imread(imagePath)
    imageCopy = image.copy()
    # Convert to grayscale
    imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    return image, imageGray

def displayImages(image, imageGray):
    plt.figure()
    plt.subplot(121)
    plt.imshow(image[:,:,::-1])
    plt.title("Original Image");
    plt.subplot(122)
    plt.imshow(imageGray)
    plt.title("Grayscale Image");
    plt.show()

# using OpenCV function findContours()
# mode - Contour retrieval mode, ( RETR_EXTERNAL, RETR_LIST, RETR_CCOMP, RETR_TREE )
# method - Contour approximation method. ( CHAIN_APPROX_NONE, CHAIN_APPROX_SIMPLE, CHAIN_APPROX_TC89_L1 etc )
# https://docs.opencv.org/4.1.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0
def findContour(imageGray):
    """
    Find all contours in the image
    """
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    print(f"Number of contours found = {len(contours)}")
    print(f"\nHierarchy : \n{hierarchy}")

    return contours, hierarchy

def drawContours(image, contours):
    """
    Contours are simply an array of pixel locations.
    """
    # Draw all the contours
    cv2.drawContours(image, contours, -1, (0,255,0), 3);
    plt.imshow(image[:,:,::-1])
    plt.show()

def drawOuterContour(image, imageGray):
    """
    Find external contours in the image.
    """
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    image1 = image.copy()
    image2 = image.copy()
    cv2.drawContours(image1, contours, -1, (0,255,0), 3);
    # Draw only the 3rd contour
    # Note that right now we do not know
    # the numbering of contour in terms of the shapes
    # present in the figure
    cv2.drawContours(image2, contours[2], -1, (0,0,255), 3)

    plt.figure()
    plt.subplot(121)
    plt.imshow(image1[:,:,::-1])
    plt.title(f"number of contours found: {len(contours)}")
    plt.subplot(122)
    plt.imshow(image2[:,:,::-1])
    plt.title("only the 3rd contour")
    plt.show()

def findCenterOfMass(image, imageGray):
    """
    1. find contours
    2. do analysis (find centroid) with contour properties
    """
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3);

    for cnt in contours:
        # We will use the contour moments
        # to find the centroid
        M = cv2.moments(cnt)
        x = int(round(M["m10"]/M["m00"]))
        y = int(round(M["m01"]/M["m00"]))
        
        # Mark the center
        cv2.circle(image, (x,y), 10, (255,0,0), -1);
    
    plt.imshow(image[:,:,::-1])
    plt.show()

def plotContours(image, imageGray):
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3);

    for index,cnt in enumerate(contours):
        # We will use the contour moments
        # to find the centroid
        M = cv2.moments(cnt)
        x = int(round(M["m10"]/M["m00"]))
        y = int(round(M["m01"]/M["m00"]))
        
        # Mark the center
        cv2.circle(image, (x,y), 10, (255,0,0), -1);
        
        # Mark the contour number
        cv2.putText(image, f"{index + 1}", (x+40, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2);

    # imageCopy = image.copy()
    plt.imshow(image[:,:,::-1])
    plt.show()

    # Area and Perimeter
    for index,cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        print(f"Contour #{index+1} has area = {area} and perimeter = {perimeter}")

def boundingBoxes(image, imageGray):
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3);

    for cnt in contours:
        # Vertical rectangle
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,255), 2)

    plt.imshow(image[:,:,::-1])
    plt.show()

def rotatedBoundingBoxes(image, imageGray):
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3);

    for cnt in contours:
        # Rotated bounding box
        box = cv2.minAreaRect(cnt)
        boxPts = np.int0(cv2.boxPoints(box))
        # Use drawContours function to draw 
        # rotated bounding box
        cv2.drawContours(image, [boxPts], -1, (0,255,255), 2)

    plt.imshow(image[:,:,::-1])
    plt.show()

def fitCircle(image, imageGray):
    """
    Fitting a bounding box (vertical or rotated) is the preferred choice in most cases.
    But, fitting a circle and/or an ellipse is a much better choice.
    """
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3);

    for cnt in contours:
        # Fit a circle
        ((x,y),radius) = cv2.minEnclosingCircle(cnt)
        cv2.circle(image, (int(x),int(y)), int(round(radius)), (125,125,125), 2)

    plt.imshow(image[:,:,::-1])
    plt.show()

def fitEllipse(image, imageGray):
    """
    Fitting a bounding box (vertical or rotated) is the preferred choice in most cases.
    But, fitting a circle and/or an ellipse is a much better choice.
    """
    contours, hierarchy = cv2.findContours(imageGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3);

    for cnt in contours:
        # Fit an ellipse
        # We can fit an ellipse only
        # when our contour has minimum
        # 5 points
        if len(cnt) < 5:
            continue
        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(image, ellipse, (255,0,125), 2)

    plt.imshow(image[:,:,::-1])
    plt.show()

if __name__ == "__main__":
    image, imageGray = loadImage()
    # displayImages(image, imageGray)

    # contours,_ = findContour(imageGray)
    # drawContours(image, contours)
    # drawOuterContour(image, imageGray)

    # after we found contours we can do further analysis with contour properties.

    # findCenterOfMass(image, imageGray)
    # plotContours(image, imageGray)
    # boundingBoxes(image, imageGray)
    # rotatedBoundingBoxes(image, imageGray)
    # fitCircle(image, imageGray)
    fitEllipse(image, imageGray)
