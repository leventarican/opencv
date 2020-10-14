import cv2

def display():
    windows_id = 'imageviewer'
    cv2.imshow(windows_id, img)
    pressed_key = cv2.waitKey(0)
    cv2.destroyWindow(windows_id)

imagepath = 'number_zero.jpg'
img = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
# print(img)

# [[  1   0   3   0   3   0   3   2   4   2   0]
#  [  0   1   0   3   3 253 253   0   0   2   1]
#  [  0   0   8   0 249 255 255 253  71   1   5]
#  [  3   0   2 251 255   2   0 253 254   0   2]
#  [  1   5   0 252   4   0   3   0 255   4   0]
#  [  0   0   2 255   0   0   0   3 253   0   4]
#  [  0   5   4 249   4   2   0   0 255   1   0]
#  [  2   0   0 255   3   0   5   0 254   0   4]
#  [  0   0   0 255   1   0   0   3 255   0   0]
#  [  1   5   0 252   2   2   2  76 250   7   0]
#  [  0   0   5   0 254   0   0 255 254   0   1]
#  [  0   8   0   3 253 253 255 250   1   2   1]
#  [  2   0   0   0   5   0   4   1   3   0   0]]

# ################################################
print(f"data type {img.dtype}")
print(f"object type {type(img)}")
print(f"image dimension {img.shape}")

# ################################################
print('access a pixel')

y = 0   # row
x = 0   # column
print(img[y,x])

# manipulate an image / modify a pixel
img[y,x] = 255
print(img)

# region of interest
# print(img[0:2,2])
# print(img[1:2,5:7])
# print(img[1,5:7])

img[1,5:7] = 100
print(img)

# ################################################
# display image with opencv

windows_id = 'imageviewer'
cv2.imshow(windows_id, img)

# wait infinitely or give some ms
# returns ascii code of the key
pressed_key = cv2.waitKey(0)

# cv2.destroyAllWindows()
cv2.destroyWindow(windows_id)

# or with matlab
# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.colorbar()

# ################################################
# write an image

# imwrite: filename, image, params (extention, quality, ...)
cv2.imwrite('zero_cv2.jpg', img)
display()