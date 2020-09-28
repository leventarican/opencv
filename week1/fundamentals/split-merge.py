# ##############################################################################
# splitting and merging channels 
# ##############################################################################

import cv2
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imagepath = 'lion.jpg'

img = cv2.imread(imagepath)

# convert BGR to RGB
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.show()

# now split and merge

# split image into the B,G,R components
b,g,r = cv2.split(img)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(b);plt.title("Blue Channel");
plt.subplot(142);plt.imshow(g);plt.title("Green Channel");
plt.subplot(143);plt.imshow(r);plt.title("Red Channel");

# merge channels into a BGR image
imgMerged = cv2.merge((b,g,r))
plt.subplot(144);plt.imshow(imgMerged[:,:,::-1]);plt.title("Merged Output");

plt.show()