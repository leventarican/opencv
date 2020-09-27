# ##############################################################################
# display image
# ##############################################################################

# check also fundamentals.py

# display function expect when image data type is float a range 0 to 1
# when data type is int a range 0 to 255

import cv2
import matplotlib
import matplotlib.pyplot as plt

imagePath = 'number_zero.jpg'
testImage = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

# with matplotlib imshow

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

plt.imshow(testImage)
plt.colorbar()
plt.show()

# with OpenCV's imshow
cv2.imshow("zero", testImage)
# wait: press any key in window!!!
cv2.waitKey(0)
cv2.destroyAllWindows()
