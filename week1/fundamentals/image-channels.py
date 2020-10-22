# ##############################################################################
# image channels
# ##############################################################################

import matplotlib.pyplot as plt
import cv2

channels = 3
channels_transparency = 4

color_imagepath = 'lion.jpg'

img = cv2.imread(color_imagepath)
print(f'image shape/dimension; without alpha channel (number of ch=3): {img.shape}')
# output: image shape/dimension: (480, 440, 3)

# opencv thinks in BGR colorspace
# we need to convert that if we want to display image with matplotlib
# no need to convert when using cv2.imshow

# option 1:
# We can also use the following - It will reverse the order of the 3rd dimension i.e. channels
plt.imshow(img[:,:,::-1])

# option 2:
# convert BGR to RGB colorspace
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img)

plt.figure(figsize=[20,5])

# image matrix: last dimension is for BGR channel
plt.subplot(131);plt.imshow(img[:,:,0],cmap="gray");plt.title("Blue Channel")
plt.subplot(132);plt.imshow(img[:,:,1],cmap="gray");plt.title("Green Channel")
plt.subplot(133);plt.imshow(img[:,:,2],cmap="gray");plt.title("Red Channel")

plt.show()

b, g, r = cv2.split(img)
print(b)

def channels():
    # img_path = "lion.jpg"
    # img_path = "sunglass.png"
    img_path = "threshold.png"

    img = cv2.imread(img_path)
    img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_unchanged = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # cv2.imshow("imread_demo", img)
    # cv2.waitKey(0)

    print(img.shape)
    print(img_grayscale.shape)
    print(img_color.shape)
    print(img_unchanged.shape)

    # (480, 440, 3)
    # (480, 440)
    # (480, 440, 3)
    # (480, 440, 3)

    # (273, 627, 3)
    # (273, 627)
    # (273, 627, 3)
    # (273, 627, 4)

    # grayscale image channel number: 1
    # color image channel number: 3
    # unchanged image channel number: 1, 3 or 4 (when image has alpha channel)

if __name__ == "__main__":
    channels()