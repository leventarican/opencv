import cv2

file = 'chaplin.mp4'
cap = cv2.VideoCapture(file)
# cap = cv2.VideoCapture(0)

# set width, height
cap.set(3, 2000)
cap.set(4, 2000)

# read one frame
ret, frame = cap.read()

# read width, height
frame_width = cap.get(3)
frame_height = cap.get(4)
print(f"frame width, height: {frame_width}, {frame_height}")

# show the one frame
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
plt.imshow(frame[...,::-1])
plt.show()

# play video
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow('frame', frame)
#         cv2.waitKey(25) # wait in ms before move to next frame
#     else:
#         break
