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

# run code
* run code from root directory
* path to data (images) are not absolute. just file name. the images files are located usually in root directory.
```
python week3/threshold.py
```

## links
* https://courses.opencv.org/
* https://docs.opencv.org/4.1.0
* https://docs.opencv.org/4.1.0/de/d7a/tutorial_table_of_content_core.html
* http://szeliski.org/Book/
* https://www.learnopencv.com/
* https://github.com/spmallick/learnopencv
* https://vision.in.tum.de/
* https://dvl.in.tum.de/research/
* http://fivedots.coe.psu.ac.th/~ad/vbi/
* https://www.learnopencv.com/snake-game-with-opencv-python/

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

# AirSim
* https://github.com/Microsoft/AirSim/releases
* download an asset. ex. `SoccerField.zip`
* unzip, cd, run with: `SoccerField$ ./SoccerField.sh`
* manual drive with key arrow, F1 for help
* drive with API in phyton. see examples in folder `airsim`
