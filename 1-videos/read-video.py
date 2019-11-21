
# read image sequences as video (e.g. a folder of images)

import cv2

file = 'chaplin.mp4'
video = cv2.VideoCapture(file)

# check file opened successfullly
if (video.isOpened() == False):
    print('error opening video')

# ret:was frame read successfully?
ret, frame = video.read()
print(ret)
print(frame)

# now go through hole video
while (video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow('frame', frame)
        cv2.waitKey(500) # wait 25ms
    else:
        break
