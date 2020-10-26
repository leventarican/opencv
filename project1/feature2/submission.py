# Feature 2: Blemish Removal

# 1. This part will use OpenCV's highGUI module and thus, 
# you will have to first complete the assignments on your local system.

# 2. Once you have completed the assignments, 
# paste the Python code in submission.py file provided in the labs.

# 3. The required data files (images and videos) are present in the same 
# directory as the submission.py. Please download the files to test your code.

# ##############################################################################

# ex. radius 15

# ensure the boundary of the new patch should be close to the boundary of the old patch
# also ensure the new patch should be smooth. look the the neighborhood of the blemish.

# Here is the problem statement in steps
# 1. Display an image with blemishes on it.
# 2. The user clicks on the blemish and the blemish is magically gone!

# image patch:
# you have 100x100 pixel image (1000 pixels) and you divide it into 10x10 patches.
# then you have 100 patches. each patch has 100 pixels.

# a way how to solve it:
# 1. find a image patch in neighborhood
# 2. blend the patch over the blemish region

# fourier transformation:
# decompose image into sinus / cosinus components
# high / low frequency signals in images: edge, noise detection in images
# https://www.youtube.com/watch?v=OYKBiWEsi9w
# fourier transform is just used for analysis here , 
# you can either use that or detect the gradient to figure out the smoothest 
# neighborhood patch after which you can seamlessly clone the blemish. 

import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

windowName = "blemish-removal"
image = cv2.imread("blemish.png",  cv2.IMREAD_UNCHANGED)

# on 3x3 kernel scharr is more accurate then sobel
# https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#filter_depths
def sobel(patch):
    patch = cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY)

    sobelx64f = cv2.Sobel(patch, cv2.CV_64F, 1, 0, ksize=5)
    absSobelx64f = np.absolute(sobelx64f)
    sobelx8u = np.uint8(absSobelx64f)

    sobely64f = cv2.Sobel(patch, cv2.CV_64F, 0, 1, ksize=5)
    absSobely64f = np.absolute(sobely64f)
    sobely8u = np.uint8(absSobely64f)

    # get gradient from mean values: any high variation?
    gradient = np.mean(sobelx8u + sobely8u)
    # print(f"gradient: {gradient}")
    return gradient

def neighborhood(xy):
    patchList = []
    gradiantList = []
    neighbor = np.array([(-30, -30), (-30, 0), (-30, 30), (0, -30), (0, 30), (30, -30), (30, 0), (30, 30)])
    for n in neighbor:
        n_xy = xy + n
        if not n_xy[0] in range(0, image.shape[1]):
            continue
        if not n_xy[1] in range(0, image.shape[0]):
            continue
        patch = image[n_xy[1] - 15:n_xy[1] + 15, n_xy[0] - 15:n_xy[0] + 15]
        gradient = sobel(patch)
        patchList.append(patch)
        gradiantList.append(gradient)
    index = gradiantList.index(max(gradiantList))
    # print(index)
    # print(gradiantList[index])
    return patchList[index]

# edge detect: high frequency
# blur
# seemles copy
def callback(action, x, y, flags, userdata):
    if action==cv2.EVENT_LBUTTONDOWN:
        patch = neighborhood((x, y))
        patch = cv2.blur(patch,(30,30),(-1,-1))
        mask = np.ones_like(patch) * 255

        # blend	=	cv.seamlessClone(	src, dst, mask, p, flags[, blend]	)
        # https://docs.opencv.org/4.1.0/df/da0/group__photo__clone.html#ga2bf426e4c93a6b1f21705513dfeca49d
        cv2.seamlessClone(patch, image, mask, (x,y), cv2.NORMAL_CLONE, image)

cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, callback)
while True:
    cv2.imshow(windowName, image)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
