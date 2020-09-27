# ##############################################################################
# save image
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt

imagePath = 'number_zero.jpg'
testImage = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

cv2.imwrite("save-image.jpg", testImage)
