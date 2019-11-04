import matplotlib.pyplot as plt
import cv2

# ################################################
# split and merging channels

channels = 3
color_imagepath = 'lion.jpg'
img = cv2.imread(color_imagepath)

b, g, r = cv2.split(img)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(b,cmap="gray");plt.title("Blue Channel")
plt.subplot(142);plt.imshow(g,cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(r,cmap="gray");plt.title("Red Channel")

imgMerged = cv2.merge((b,g,r))
plt.subplot(144);plt.imshow(imgMerged[:,:,::-1]);plt.title("Merged Output")

plt.show()