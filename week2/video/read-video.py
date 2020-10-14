# ##############################################################################
# read image sequences as video (e.g. a folder of images, webcam, video file)
# ##############################################################################

import cv2

file = 'chaplin.mp4'
# video = cv2.VideoCapture(0) # webcam: arg = 0
video = cv2.VideoCapture(file)

# check file opened successfullly
if (video.isOpened() == False):
    print('error opening video')

# read frame
# read() return a tuble
# ret: was frame read successfully?
ret, frame = video.read()
print(ret)
print(frame)

# now go through hole video
while (video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow('frame', frame)
        cv2.waitKey(25) # wait in ms before move to next frame
    else:
        break
