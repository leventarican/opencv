# Feature 3: Chroma Keying

# 1. This part will use OpenCV's highGUI module and thus, 
# you will have to first complete the assignments on your local system.

# 2. Once you have completed the assignments, paste the Python code 
# in submission.py file provided in the labs.

# 3. The required data files (images and videos) are present in the 
# same directory as the submission.py. Please download the files to test your code.

import cv2

global video

def read():
    global video

    file = "project1/feature3/greenscreen-asteroid.mp4"
    video = cv2.VideoCapture(file)

    ret, frame = video.read()
    print(f"frame read result: {ret}")

# some thoughts:
# - work in HSV color space to identify green saturation
def process():
    global video

    while (video.isOpened()):
        ret, frame = video.read()
        if ret == True:
            cv2.imshow('frame', frame)
            cv2.waitKey(25) # wait in ms before move to next frame
        else:
            break

def write():
    pass

# 1. read video
# 2. process each frame: replace green with a background
# 3. write video: each frame
if __name__ == "__main__":
    read()
    process()
    write()