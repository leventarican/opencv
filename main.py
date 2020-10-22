# try, learn, practice, test, ... do it all here.

def image_channels():
    import cv2

    img_jpeg = cv2.imread('lion.jpg')
    rows, cols, channels = img_jpeg.shape
    print(channels)

def chart():
    import matplotlib.pyplot as plt

    # Data to plot
    labels = 'Python', 'C++', 'Ruby', 'Java'
    sizes = [215, 130, 245, 210]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

def slicing():
    tuble = (1, 2, 3)

    print(tuble[0])
    print(tuble[2])

    for t in tuble:
        print(f'tuble: {t}')

    # python slice
    print(tuble[::-1])
    print(tuble[:-1])
    print(tuble[1:])

def create_image():
    import numpy as np
    import matplotlib.pyplot as plt
    import random

    image = np.zeros(shape=(10, 10, 3), dtype='uint8')
    # image[5][5] = 255
    # image[4,4] = 255

    for row in range(0,10):
        for column in range(3,7):
            if row == column:
                print( f'row: {row}; column: {column}' )    
                image[row, column] = random.randint(0,255)

    print(image.dtype)

    plt.imshow(image)
    plt.show()

def arrays():
    import numpy

    example = numpy.array([
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [0, 0, 0]
    ])

    print(example)
    print(len(example))
    print(example.shape)

    rows, cols = example.shape

    for x in range(0, rows):
        for y in range(0, cols):
            print(f'x: {x}; y: {y}')

def test_case0():
    print(f'modulo: {5%4}')
    print(f'display the type: {type(2)}')

def reflection_introspection():
    # getattr(__doc__, "test_case0")
    attr = dir(__doc__)
    print(attr)

def debug():
    import numpy as np
    import matplotlib.pyplot as plt
    import cv2

    im = np.zeros((10,10),dtype='uint8')
    im[0,1] = 1
    im[-1,0]= 1
    im[-2,-1]=1
    im[2,2] = 1
    im[5:8,5:8] = 1
    # plt.imshow(im, cmap="gray"); plt.show()

    # https://docs.opencv.org/master/da/d6e/tutorial_py_geometric_transformations.html
    cubic = cv2.resize(im, (50,50), interpolation=cv2.INTER_CUBIC)
    linear = cv2.resize(im, (50,50), interpolation=cv2.INTER_LINEAR)

    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    dilated = cv2.dilate(im, element)
    dilated_cubic = cv2.resize(dilated, (50,50), interpolation=cv2.INTER_CUBIC)
    dilated_linear = cv2.resize(dilated, (50,50), interpolation=cv2.INTER_LINEAR)

    plt.figure(figsize=[20,20])
    plt.subplot(161);plt.imshow(im, cmap="gray");plt.title("im");
    plt.subplot(162);plt.imshow(cubic, cmap="gray");plt.title("cubic");
    plt.subplot(163);plt.imshow(linear, cmap="gray");plt.title("linear");
    plt.subplot(164);plt.imshow(dilated, cmap="gray");plt.title("dilated");
    plt.subplot(165);plt.imshow(dilated_cubic, cmap="gray");plt.title("dilated_cubic");
    plt.subplot(166);plt.imshow(dilated_linear, cmap="gray");plt.title("dilated_linear");
    plt.show()

def waitkey_demo():
    """
    the function waitKey() waits for a key event for a "delay"
    """
    import cv2 
    
    img = cv2.imread("lion.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("waitkey_demo", img)
    k = cv2.waitKey(2000)
    print(k)

def imread_demo():
    import cv2 

    # img_path = "lion.jpg"
    # img_path = "sunglass.png"
    img_path = "threshold.png"

    img = cv2.imread(img_path)
    img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_unchanged = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # cv2.imshow("imread_demo", img)
    # cv2.waitKey(0)

    print(img.shape)
    print(img_grayscale.shape)
    print(img_color.shape)
    print(img_unchanged.shape)

    # (480, 440, 3)
    # (480, 440)
    # (480, 440, 3)
    # (480, 440, 3)

    # (273, 627, 3)
    # (273, 627)
    # (273, 627, 3)
    # (273, 627, 4)

    # grayscale image channel number: 1
    # color image channel number: 3
    # unchanged image channel number: 1, 3 or 4 (when image has alpha channel)

def overflow():
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np

    image = cv2.imread("debug.png",1)
    # Convert to RGB
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(np.unique(imageRGB))
    print(imageRGB[10])

    # Add 200 to image
    imageRGB = cv2.add(imageRGB,200)
    print(np.unique(imageRGB))
    print(imageRGB[10])

    plt.imshow(imageRGB)
    plt.show()

if __name__ == "__main__":
    # chart()
    # slicing()
    # create_image()
    # image_channels()
    # arrays()
    # test_case0()
    # reflection_introspection()
    # debug()
    # waitkey_demo()
    # imread_demo()
    overflow()
