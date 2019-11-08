# try, learn, practice, test, ... do it all here.

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

if __name__ == "__main__":
    # chart()
    # slicing()
    create_image()
