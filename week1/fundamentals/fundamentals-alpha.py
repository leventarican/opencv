import cv2
import matplotlib.pyplot as plt

# #############################################################################
# images with alpha channel

# this image has a 4. channel (= alpha channel)
imagepath = 'panther.png'

# flag: -1 for unchanged
img = cv2.imread(imagepath, -1)

# print("image Dimension ={}".format(img.shape))
# output: image Dimension =(608, 640, 4)
print(f"image dimension {img.shape}")

# now extract the -channel and the alpha channel
rgb = img[:,:,0:3]
mask = img[:,:,3]

plt.figure(figsize=[20,20])
plt.subplot(121);plt.imshow(rgb[:,:,::-1]);plt.title('Color channels')
plt.subplot(122);plt.imshow(mask,cmap='gray');plt.title('Alpha channel')

# remark: 
# boundaries at alpha channel is from 0 - 255 
# in order to have a smooth overlap

plt.show()