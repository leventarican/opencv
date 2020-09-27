# ##############################################################################
# access and modify pixels
# ##############################################################################

# check also fundamentals.py

# NumPy arrays store matrix in row column format
# means if you want to access location(x,y) you need to access pixel image(y,x) instead

import cv2
import matplotlib
import matplotlib.pyplot as plt

imagePath = 'number_zero.jpg'

# cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
# cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
testImage = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

# access y=0, x=0
print(testImage[0,0])

# manipulate
testImage[0,0]=200
print(testImage)

# manipulating group of pixel, ROI (Region Of Interest)
test_roi = testImage[0:2,0:4]
print(f"Original Matrix\n {testImage}")
print(f"Selected Region\n {test_roi}")

testImage[0:2,0:4] = 111
print(f"Manipulated Region\n {testImage}")

# [[111 111 111 111   3   0   3   2   4   2   0]
# [111 111 111 111   3 253 253   0   0   2   1]
# [  0   0   8   0 249 255 255 253  71   1   5]
# [  3   0   2 251 255   2   0 253 254   0   2]
# [  1   5   0 252   4   0   3   0 255   4   0]
# [  0   0   2 255   0   0   0   3 253   0   4]
# [  0   5   4 249   4   2   0   0 255   1   0]
# [  2   0   0 255   3   0   5   0 254   0   4]
# [  0   0   0 255   1   0   0   3 255   0   0]
# [  1   5   0 252   2   2   2  76 250   7   0]
# [  0   0   5   0 254   0   0 255 254   0   1]
# [  0   8   0   3 253 253 255 250   1   2   1]
# [  2   0   0   0   5   0   4   1   3   0   0]]
