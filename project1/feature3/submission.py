# Enter your code here

import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def callback(*args):
    pass

def video():
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

    file = "greenscreen-asteroid.mp4"
    cap = cv2.VideoCapture(file)
    ret, frame = cap.read()
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    print(f"frame read result: {ret}; width: {frame_width}; height: {frame_height}")

    out = cv2.VideoWriter("output.mp4", \
        cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

    background = cv2.imread("background.jpg", cv2.IMREAD_UNCHANGED)

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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

            cv2.imshow("debug", np.zeros([100, 100], np.uint8))
            cv2.imshow("blended", blended)

            out.write(blended)

            k = cv2.waitKey(25) & 0xFF
            if k == 27:
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# only a single frame
def frame():
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

    file = "greenscreen-asteroid.mp4"
    cap = cv2.VideoCapture(file)
    ret, frame = cap.read()
    frame_width = cap.get(3)
    frame_height = cap.get(4)
    print(f"frame read result: {ret}; width: {frame_width}; height: {frame_height}")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    background = cv2.imread("background.jpg", cv2.IMREAD_UNCHANGED)

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

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("foreground", fg)
        cv2.imshow("background", bg)
        cv2.imshow("debug", np.zeros([100, 100], np.uint8))
        cv2.imshow("blended", blended)

    cap.release()
    cv2.destroyAllWindows()

# 1. read video
# 2. process each frame: replace green with a background
# 3. write video: each frame
if __name__ == "__main__":
    # frame()
    video()