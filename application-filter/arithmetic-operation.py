import cv2
import matplotlib.pyplot as plt
import numpy as np

_jpeg_path = "../lion.jpg"
_jpeg = cv2.imread(_jpeg_path)
_jpeg = np.float32(_jpeg)/255

# plt.imshow(_jpeg[:,:,::-1])
# plt.title("lion")

_png_path = "tree.png"
_png = cv2.imread(_png_path, -1) # -1: with alpha channel
_png = np.float32(_png)/255
_png = cv2.resize(_png, None, fx=0.05, fy=0.05)
_png_height, _png_width, _png_channels = _png.shape
print(f'tree dimension ={_png.shape}')

_png_bgr = _png[:,:,0:3]  # color channels
_png_mask = _png[:,:,3]    # alpha channel only

# plt.figure(figsize=[15,15])
# plt.subplot(121)
# plt.imshow(_png_bgr[:,:,::-1])
# plt.title('tree color channels')
# plt.subplot(122)
# plt.imshow(_png_mask, cmap='gray')
# plt.title('tree alpha channel')

# Top left corner of the glasses
topLeftRow = 300
topLeftCol = 100

bottomRightRow = topLeftRow + _png_height
bottomRightCol = topLeftCol + _png_width

lion_with_tree_naive = _jpeg.copy()
lion_with_tree_naive[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]=_png_bgr

# plt.imshow(lion_with_tree_naive[...,::-1])

# ##############################################################################

# jpeg image has 3 channels
# mask is 1 channel (= the alpha channel); make it also 3 channel
tree_mask = cv2.merge((_png_mask, _png_mask, _png_mask))

lion_with_tree_arithmetic = _jpeg.copy()

# region of interest; location to place the tree on lion image
roi = lion_with_tree_arithmetic[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]

masked_region = cv2.multiply(roi, (1 - tree_mask))
masked_tree = cv2.multiply(_png_bgr, tree_mask)
roi_final = cv2.add(masked_region, masked_tree)

# plt.figure(figsize=[20,20])
# plt.subplot(131);plt.imshow(masked_region[...,::-1]);plt.title("Masked lion Region")
# plt.subplot(132);plt.imshow(masked_tree[...,::-1]);plt.title("Masked tree Region")
# plt.subplot(133);plt.imshow(roi_final[...,::-1]);plt.title("Augmented lion and tree")

# replace the roi
lion_with_tree_arithmetic[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol] = roi_final

plt.figure(figsize=[20,20])
plt.subplot(121)
plt.imshow(_jpeg[:,:,::-1])
plt.title("Original Image")
plt.subplot(122)
plt.imshow(lion_with_tree_arithmetic[:,:,::-1])
plt.title("With Sunglasses")

plt.show()