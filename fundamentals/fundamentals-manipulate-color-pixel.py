import cv2
import matplotlib.pyplot as plt

# #############################################################################
# modify a pixel

# we take a grayscale image
# convert it to a colored image

imagepath = 'number_zero.jpg'
img = cv2.imread(imagepath)
colored_img = cv2.cvtColor(img, 1)  # 1: colored channel. we have now 3 channels
# plt.imshow(colored_img)

plt.figure(figsize=[20,20])

# (R,G,B)
yellow = (0,255,255)
cyan = (255,255,0)
magenta = (255,0,255)

# now set colors to pixels and swap channels: BGR -> RGB
colored_img[0,0] = yellow
plt.subplot(141);plt.imshow(colored_img[:,:,::-1])

colored_img[1,1] = cyan
plt.subplot(142);plt.imshow(colored_img[:,:,::-1])

colored_img[2,2] = magenta
plt.subplot(143);plt.imshow(colored_img[:,:,::-1])

# #############################################################################
# modify a region of interest

green = (0,255,0)
blue = (255,0,0)
red = (0,0,255)

colored_img[0:4, 0:3] = green
colored_img[4:8, 0:3] = blue
colored_img[8:12, 0:3] = red

plt.subplot(144);plt.imshow(colored_img[:,:,::-1])

plt.show()