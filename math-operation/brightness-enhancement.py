import cv2
import matplotlib.pyplot as plt
import numpy as np

# #############################################################################
# general proceed: add intensity to each pixel

img = cv2.imread('lion.jpg')

brightnessOffset = 50
brightnessHigh = img + brightnessOffset

# datatype after addition operation the pixels are clipped

# plt.figure(figsize=[20,20])
# plt.subplot(121);plt.imshow(img[...,::-1]);plt.title("original")
# plt.subplot(122);plt.imshow(brightnessHigh[...,::-1]);plt.title("brightness high")
# plt.show()

# #############################################################################
# construct a simple image
a = np.array([[100, 110], [120, 130]], dtype='uint8')
print(a)
# [[100 110]
#  [120 130]]

a_offset = 130
print(a + a_offset)
# [[230 240]
#  [250   4]]
# a[1,1] is overflowed and rolled over because over 255

print(a - a_offset)
# [[226 236]
#  [246   0]]

print(a + (-a_offset))
# [[-30 -20]
#  [-10   0]]

# datatype is int16 (signed int) because of -a_offset
print((a + (-a_offset)).dtype)

# #############################################################################
# clip the value with opencv
print(cv2.add(a, a_offset))
# [[230 240]
#  [250 255]]

# convert to int32 with numpy
a_int32 = np.int32(a)
print(a_int32 + a_offset)
# [[230 240]
#  [250 260]]

print(np.clip(a_int32 + a_offset, 0, 255))
# [[230 240]
#  [250 255]]

b = a_int32 + a_offset
print(b.clip(0, 255))
# [[230 240]
#  [250 255]]

b_uint8 = np.uint8(b.clip(0, 255))
print(b_uint8)
# [[230 240]
#  [250 255]]

# #############################################################################
# convert to float: with scaling
a_float32 = np.float32(a) / 255
b = a_float32 + a_offset / 255
print(b)
# [[0.90196085 0.94117653]
#  [0.9803922  1.0196079 ]]

# back to uint8: with rescaling (clipping)
c = b * 255
b_uint8 = np.uint8(c.clip(0, 255))
print(b_uint8)
# [[230 240]
#  [250 255]]

# #############################################################################
brightnessHighOpenCV = cv2.add(img, np.ones(img.shape, dtype='uint8') * brightnessOffset)

brightnessHighInt32 = np.int32(img) + brightnessOffset
brightnessHighInt32Clipped = np.clip(brightnessHighInt32, 0, 255)

# plt.figure(figsize=[20,20])
# plt.subplot(131);plt.imshow(img[...,::-1]);plt.title("original")
# plt.subplot(132);plt.imshow(brightnessHighOpenCV[...,::-1]);plt.title("opencv")
# plt.subplot(133);plt.imshow(brightnessHighInt32Clipped[...,::-1]);plt.title("numpy int32 clipped")
# plt.show()

# #############################################################################
brightnessHighFloat32 = np.float32(img) + brightnessOffset
brightnessHighFloat32Clipped = np.clip(brightnessHighFloat32/255, 0, 1)

brightnessHighFloat32ClippedUInt8 = np.uint8(brightnessHighFloat32Clipped*255)

plt.figure(figsize=[20,20])
plt.subplot(131);plt.imshow(img[...,::-1]);plt.title("original")
plt.subplot(132);plt.imshow(brightnessHighOpenCV[...,::-1]);plt.title("opencv")
plt.subplot(133);plt.imshow(brightnessHighInt32Clipped[...,::-1]);plt.title("numpy int32 clipped")
plt.show()