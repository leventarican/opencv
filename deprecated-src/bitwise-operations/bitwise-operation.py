import cv2
import matplotlib.pyplot as plt
import numpy as np

# INFO: 
# code is nearly same as arithmetic-operation.py
# except the part of cv2.multiply (arithmetic operations)
# instead we use bitwise operations cv2.bitwise_and, ...

_jpeg_path = "lion.jpg"
_jpeg = cv2.imread(_jpeg_path)
_jpeg = np.float32(_jpeg)/255

_png_path = "tree.png"
_png = cv2.imread(_png_path, -1) # -1: with alpha channel
_png = np.float32(_png)/255
_png = cv2.resize(_png, None, fx=0.05, fy=0.05)
_png_height, _png_width, _png_channels = _png.shape

_png_bgr = _png[:,:,0:3]  # color channels
_png_mask = _png[:,:,3]    # alpha channel only

topLeftRow = 300
topLeftCol = 100

bottomRightRow = topLeftRow + _png_height
bottomRightCol = topLeftCol + _png_width

tree_mask = cv2.merge((_png_mask, _png_mask, _png_mask))

roi = _jpeg[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]

# ##############################################################################
# INFO:
# here are used bitwise function instead of arithmetic

# take only pixels that match region of interest AND inverse alpha channel of tree 
masked_region = cv2.bitwise_and(roi, cv2.bitwise_not(tree_mask))

# take only pixels that match where color channel AND alpha channel
# we will have a more precise tree (the boundary pixels)
masked_tree = cv2.bitwise_and(_png_bgr, tree_mask)

roi_final = cv2.bitwise_or(masked_region, masked_tree)

# ##############################################################################

plt.figure(figsize=[20,20])
plt.subplot(131);plt.imshow(masked_region[...,::-1]);plt.title("mask lion")
plt.subplot(132);plt.imshow(masked_tree[...,::-1]);plt.title("mask tree")
plt.subplot(133);plt.imshow(roi_final[...,::-1]);plt.title("Augmented lion and tree")
plt.show()