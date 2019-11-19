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

if __name__ == "__main__":
    # chart()
    # slicing()
    # create_image()
    # image_channels()
    # arrays()
    test_case0()
