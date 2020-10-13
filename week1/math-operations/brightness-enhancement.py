# ##############################################################################
# brightness enhancement
# ##############################################################################

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def brightness_enhancement(image):
    """
    to improve brightness: out_image = beta + in_image 
    """
    brightnessOffset = 50
    brightHigh = image + brightnessOffset

    # this result looks strange hmm!?
    # plt.figure(figsize=[20,20])
    # plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("original Image");
    # plt.subplot(122);plt.imshow(brightHigh[...,::-1]);plt.title("High brightness");

    print(f"Original Image Datatype : {image.dtype}")
    print(f"brightness Image Datatype : {brightHigh.dtype}")
    print(f"Original Image Highest Pixel Intensity : {image.max()}")
    print(f"brightness Image Highest Pixel Intensity : {brightHigh.max()}")

    # the problem is that we have an overflow:
    # since the value range is 0-255 (unsingned int 8) and we add 50 to each pixel 

def understand_overflow():
    """
    understand overflow: what happens in brightness_enhancement()?
    """
    a = np.array([[100, 110], [120, 130]], dtype='uint8')
    print(a)
    # [[100 110]
    # [120 130]]

    # add 150 will lead to overflow on unsigned integer 8: range is 0 - 255
    print(a + 130)
    # [[230 240]
    # [250   4]]

    # in this case we have a uin8 underflow
    print(a - 130)
    # [[226 236]
    # [246   0]]

    # -130 is uint16
    print(a + (-130))
    # [[-30 -20]
    # [-10   0]]

def opencv_arithmetic():
    """
    use opencv to handle uint8 arithmetic in order to prevent over/underflow
    """
    
    a = np.array([[100, 110], [120, 130]], dtype='uint8')

    print(cv2.add(a,130))
    # [[230 240]
    #  [250 255]]

def int_arithmetic():
    """
    or convert to int32/int64 and float32/float64, do arithmetic operation, 
    and convert back to uint8.
    """

    a = np.array([[100, 110], [120, 130]], dtype='uint8')

    a_int32 = np.int32(a)
    b = a_int32+130
    print(b)
    # [[230 240]
    # [250 260]]

    # back to uint8
    print(b.clip(0,255))
    # [[230 240]
    # [250 255]]

    b_uint8 = np.uint8(b)
    print(b_uint8)
    # [[230 240]
    # [250   4]]

def float_arithmetic():
    """
    It is a good practice to convert the uint8 to float and normalize the range to [0,1] 
    and change it back to [0,255] after doing all arithmetic operations
    """

    a = np.array([[100, 110], [120, 130]], dtype='uint8')

    # convert normalized float32/float64
    a_float32 = np.float32(a)/255
    b = a_float32 + 130/255
    print(b)
    # [[0.90196085 0.94117653]
    # [0.9803922  1.0196079 ]]
      
    c = b*255
    print(f"Output = \n{c}")
    print(f"Clipped output= \n{c.clip(0,255)}")
    b_uint8 = np.uint8(c.clip(0,255))
    print(f"uint8 output = \n{b_uint8}")  

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'
    
    image = cv2.imread('lion.jpg')

    # brightness_enhancement(image)
    # understand_overflow()
    # opencv_arithmetic()
    # int_arithmetic()
    # float_arithmetic()

    plt.show()
