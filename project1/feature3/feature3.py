# Feature 3: Chroma Keying

# 1. This part will use OpenCV's highGUI module and thus, 
# you will have to first complete the assignments on your local system.

# 2. Once you have completed the assignments, paste the Python code 
# in submission.py file provided in the labs.

# 3. The required data files (images and videos) are present in the 
# same directory as the submission.py. Please download the files to test your code.

import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
# matplotlib.rcParams['image.cmap'] = 'gray'

global cap

def callback(*args):
    value = args[0]
    # print(value)

def read():
    global cap

    file = "project1/feature3/greenscreen-asteroid.mp4"
    cap = cv2.VideoCapture(file)

    ret, frame = cap.read()
    frame_width = cap.get(3)
    frame_height = cap.get(4)
    print(f"frame read result: {ret}")

# some thoughts:
# - work in HSV color space to identify green saturation
def processFrame():
    global cap

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerb = np.array([0, 0, 0])
    upperb = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lowerb=lowerb, upperb=upperb)

    plt.imshow("frame", frame)
    plt.imshow("mask", mask)

    # windowName = "debug"
    # cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
    # cv2.createTrackbar("debug", windowName, 0, 3, callback)
    # debug = np.zeros([100, 100], np.uint8)
    # cv2.imshow("debug", debug)

    # plt.show()
    _ = cv2.waitKey(0)

    # while True:
    #     k = cv2.waitKey(1000) & 0xFF
    #     if k == 27:
    #         break

    cap.release()
    cv2.destroyAllWindows()

def process():
    global cap

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame', frame)
            cv2.waitKey(25) # wait in ms before move to next frame
        else:
            break

def write():
    pass

def close():
    global cap

    cap.release()
    cv2.destroyAllWindows()

def debug():
    lowerHue = 0
    upperHue = 179
    lowerSaturation = 0
    upperSaturation = 255
    lowerValue = 0
    upperValue = 255

    windowName = "debug"
    cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("lower hue", windowName, 0, 179, callback)
    cv2.createTrackbar("upper hue", windowName, 179, 179, callback)
    cv2.createTrackbar("lower saturation", windowName, 0, 255, callback)
    cv2.createTrackbar("upper saturation", windowName, 255, 255, callback)
    cv2.createTrackbar("lower value", windowName, 200, 255, callback)
    cv2.createTrackbar("upper value", windowName, 255, 255, callback)

    # video frame
    file = "project1/feature3/greenscreen-asteroid.mp4"
    cap = cv2.VideoCapture(file)
    ret, frame = cap.read()
    frame_width = cap.get(3)
    frame_height = cap.get(4)
    print(f"frame read result: {ret}; width: {frame_width}; height: {frame_height}")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    background = cv2.imread("project1/feature3/background.jpg", cv2.IMREAD_UNCHANGED)

    while True:
        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break

        lowerHue = cv2.getTrackbarPos("lower hue", windowName)
        upperHue = cv2.getTrackbarPos("upper hue", windowName)
        lowerSaturation = cv2.getTrackbarPos("lower saturation", windowName)
        upperSaturation = cv2.getTrackbarPos("upper saturation", windowName)
        lowerValue = cv2.getTrackbarPos("lower value", windowName)
        upperValue = cv2.getTrackbarPos("upper value", windowName)

        mask = cv2.inRange(hsv, lowerb=(lowerHue, lowerSaturation, lowerValue),\
            upperb=(upperHue, upperSaturation, upperValue))
        mask = cv2.bitwise_not(mask)
        mask = cv2.merge((mask, mask, mask))     
        fg = cv2.bitwise_and(mask, frame)
        bg = cv2.subtract(background, mask)
        blended = cv2.add(fg, bg)

        # cv2.imshow("frame", frame)
        # cv2.imshow("mask", mask)
        # cv2.imshow("foreground", fg)
        # cv2.imshow("background", bg)
        cv2.imshow("debug", np.zeros([100, 100], np.uint8))
        cv2.imshow("blended", blended)

    cap.release()
    cv2.destroyAllWindows()

# 1. read video
# 2. process each frame: replace green with a background
# 3. write video: each frame
if __name__ == "__main__":
    debug()
    # debug_()

    # read()
    # createWindow()
    # processFrame()
    # process()
    # write()
    # close()