# for detecting blobs there are easier ways like
# example apply thresholding, then apply connected component analysis
# or find contours to find the blobs.

# but for finding a specific blob we can use simple blob detector

# OpenCV provides a convenient way to detect blobs 
# and filter them based on different characteristics. 



import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

def example():
    """
    basic example
    """
    # why convert image to grayscale?
    # 
    # better performance on calculations/operations 
    # 
    # you can either use cv2.IMREAD_GRAYSCALE (loaded as BGR) 
    # or cv2.cvtColor(img, cv2.COLOR_BGR2GRAY). there is no difference.
    im = cv2.imread("week3/blob_detection.jpg", cv2.IMREAD_GRAYSCALE)

    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create()
    keypoints = detector.detect(im)
    im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    
    # Mark blobs using image annotation concepts we have studied so far
    for k in keypoints:
        x,y = k.pt
        x=int(round(x))
        y=int(round(y))
        # Mark center in BLACK
        cv2.circle(im,(x,y),5,(0,0,0),-1)
        # Get radius of blob
        diameter = k.size
        radius = int(round(diameter/2))
        # Mark blob in RED
        cv2.circle(im,(x,y),radius,(0,0,255),2)

    plt.imshow(im[:,:,::-1])
    plt.show()

def exampleParameters():
    """
    https://docs.opencv.org/4.1.0/d0/d7a/classcv_1_1SimpleBlobDetector.html
    """

    print("example with parameters")

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    
    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 200
    
    # Filter by Area (in pixel)
    params.filterByArea = True
    # params.minArea = 500
    params.maxArea = 100

    # circularity of a square is 0.785
    # circle has a circularity of 1
    params.filterByCircularity = True
    params.minCircularity = 0.92
    params.maxCircularity = 1.0
    
    # # Filter by Convexity
    # params.filterByConvexity = True
    # params.minConvexity = 0.87
    
    # # Filter by Inertia
    # params.filterByInertia = True
    # params.minInertiaRatio = 0.01
    
    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    im = cv2.imread("week3/blob_detection.jpg", cv2.IMREAD_GRAYSCALE)
    keypoints = detector.detect(im)
    im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    
    print(keypoints)

    # Mark blobs using image annotation concepts we have studied so far
    for k in keypoints:
        x,y = k.pt
        x=int(round(x))
        y=int(round(y))

        print(f"keypoint x: {x}; y: {y}")

        # Mark center in BLACK
        cv2.circle(im,(x,y),1,(0,255,0),-1)
        # Get radius of blob
        diameter = k.size
        radius = int(round(diameter/2))
        # Mark blob in RED
        cv2.circle(im,(x,y),radius,(0,0,255),1)

    plt.imshow(im[:,:,::-1])
    plt.show()

# In the example covered in Week 3, we discussed about Simple Blob Detector. 
# If a simple blob detector is used on the following images with default parameters, 
# except filterByArea parameter set to False, what is the number of blobs detected for each image?
def exampleBlob(imagePath):
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = False
    detector = cv2.SimpleBlobDetector_create(params)

    im = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    keypoints = detector.detect(im)

    print(keypoints)

    im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)

    plt.imshow(im[:,:,::-1])
    plt.show()

if __name__ == "__main__":
    # example()
    # exampleParameters()
    exampleBlob("week3/blob-0.png")
    exampleBlob("week3/blob-1.png")
