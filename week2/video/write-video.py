import cv2

# write video frame by frame
# use FourCC Code to specify the video codec (ex. MPEG, ...)
# use VideoWriter to write frames
# https://docs.opencv.org/4.1.0/dd/d9e/classcv_1_1VideoWriter.html#ac3478f6257454209fa99249cc03a5c59

cap = cv2.VideoCapture('chaplin.mp4')

# get resolution convert from float to int
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# create writer obj with fourcc code, fps=10 and frame size
# <VideoWriter object>    =   cv.VideoWriter( filename, fourcc, fps, frameSize[, isColor] )
out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(cap.isOpened()):
  # capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    out.write(frame)
    # wait for 25 ms before moving on to next frame
    cv2.waitKey(25)
  else: 
    break

cap.release()
out.release()
