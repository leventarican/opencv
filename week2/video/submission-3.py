import cv2 

# like in mouse.py we will use callback function
# trackbar = slider

# https://docs.opencv.org/4.1.0/d7/dfc/group__highgui.html#gaf78d2155d30b728fc413803745b67a9b
# cv2.createTrackbar(trackbarName, windowName, value, count, onChange)

# see also resize-image.py example

img = cv2.imread("lion.jpg", 1)
windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"
scaleFactor = 1
scaleType = 0
maxScaleUp = 100
maxType = 1

def onChange(*args):
    value = args[0]
    print(value)

def scaleImage(*args):
    global scaleFactor
    global scaleType
    
    # Get the scale factor from the trackbar 
    if scaleType == 0:
        scaleFactor = 1 + args[0]/100.0
    else:
        scaleFactor = 1 - args[0]/100.0

    # Perform check if scaleFactor is zero
    if scaleFactor == 0:
        scaleFactor = 1
    
    # Resize the image
    scaledImage = cv2.resize(img, None, fx=scaleFactor, fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)

def scaleTypeImage(*args):
    global scaleType
    scaleType = args[0]

    # global scaleFactor
    # scaleType = args[0]
    # scaleFactor = 1 + scaleFactor/100.0
    # if scaleFactor ==0:
    #     scaleFactor = 1
    # scaledImage = cv2.resize(img, None, fx=scaleFactor,\
    #         fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    # cv2.imshow(windowName, scaledImage)

cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("debug", windowName, 0, 3, onChange)
cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)
cv2.imshow(windowName, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
