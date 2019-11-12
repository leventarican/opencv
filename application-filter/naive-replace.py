import cv2
import matplotlib.pyplot as plt
import numpy as np

_jpeg_path = "../lion.jpg"
_jpeg = cv2.imread(_jpeg_path)
_jpeg = np.float32(_jpeg)/255

plt.imshow(_jpeg[:,:,::-1])
plt.title("lion")

_png_path = "../tree.png"
_png = cv2.imread(_png_path, -1) # -1: with alpha channel
_png = np.float32(_png)/255
_png = cv2.resize(_png, None, fx=0.05, fy=0.05)
_png_height, _png_width, _png_channels = _png.shape
print(f'tree dimension ={_png.shape}')

_png_bgr = _png[:,:,0:3]  # color channels
_png_mask = _png[:,:,3]    # alpha channel only

plt.figure(figsize=[15,15])
plt.subplot(121)
plt.imshow(_png_bgr[:,:,::-1])
plt.title('tree color channels')
plt.subplot(122)
plt.imshow(_png_mask, cmap='gray')
plt.title('tree alpha channel')

# Top left corner of the glasses
topLeftRow = 230
topLeftCol = 330

bottomRightRow = topLeftRow + _png_height
bottomRightCol = topLeftCol + _png_width

lion_with_tree_naive = _jpeg.copy()
lion_with_tree_naive[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]=_png_bgr

plt.imshow(lion_with_tree_naive[...,::-1])

plt.show()