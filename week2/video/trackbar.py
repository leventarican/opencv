import cv2 

# like in mouse.py we will use callback function
# trackbar = slider
# https://docs.opencv.org/4.1.0/d7/dfc/group__highgui.html#gaf78d2155d30b728fc413803745b67a9b
# cv2.createTrackbar(trackbarName, windowName, value, count, onChange)

def onChange(*args):
    print(args)
    pass

source = cv2.imread("lion.jpg", 1)
cv2.namedWindow("trackbar", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("trackbarName", "trackbar", 0, 3, onChange)

k = 0
while k!=27 :
    k = cv2.waitKey(20) & 0xFF
    cv2.imshow("trackbar", source)
cv2.destroyAllWindows()
