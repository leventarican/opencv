# OpenCV: hands-on
* OpenCV is the most widely used computer vision library

## install prerequirements, environment
* we will use a virtual environment
* you can follow the instruction on `create-venv.sh`
* example for start and stop virtual env.
```
source venv/bin/activate
deactivate
```

## links
* https://courses.opencv.org/
* https://www.learnopencv.com/
* https://github.com/spmallick/learnopencv
* https://vision.in.tum.de/
* https://dvl.in.tum.de/research/

## cheatsheet
```
read image: lion = cv2.imread('lion.jpg')  # numpy array
copy image: lion.copy()
display type (uint8, uint16, ..., float32, ...): print(lion.dtype)
display shape: print(lion.shape)
resize image: cv2.resize(...)
get 3 channel BGR of an 4-channel image: lion[:,:,0:3]
get single channel (alpha channel): alhpa = lion[:,:,3]
merge single channel to 3 channel: cv2.merge(alhpa, alpha, alpha)
display matplotlib: plt.imshow(lion[:,:,::-1])  # -1 --> BGR to RGB
uint8 to float: lion = np.float32(lion)/255
```
