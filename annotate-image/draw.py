import cv2
import matplotlib.pyplot as plt

def load_image(path):
    img = cv2.imread(path)
    return img

def display_image(img):
    plt.imshow(img[:,:,::-1])
    plt.show()

def draw_line(img):
    pt1 = (0, 50)    # point 1
    pt2 = (300, 30)
    color = (255, 0, 0)  # color tuble of 3 numbers: BGR
    cv2.line(img, pt1, pt2, color, thickness=3)
    # with anti aliased
    cv2.line(img, (300, 30), (400, 100), (0, 255, 0), thickness=3, lineType=cv2.LINE_AA)

def draw_circle(img):
    center = (30, 30)
    radius = 10
    cv2.circle(img, center, radius, color=(255, 0, 0), thickness=3)
    # fill circle
    cv2.circle(img, (50, 200), radius=30, color=(0, 255, 0), thickness=-1)

if __name__ == "__main__":
    path = '../lion.jpg'
    img = load_image(path)
    draw_line(img)
    draw_circle(img)

    display_image(img)