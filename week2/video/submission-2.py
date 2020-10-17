import cv2
# import matplotlib.pyplot as plt

# Assignment 2: Create a Face Annotation Tool

source = None
topleft = []
bottomright = []

def drawBoundingBox(action, x, y, flags, userdata):
    """
    To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. 
    This time we will draw a green rectangle at the top-right corner of image.
    cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
    """
    global topleft, bottomright, source
    if action==cv2.EVENT_LBUTTONDOWN:
        topleft = [(x, y)]
        print(topleft)
    if action==cv2.EVENT_LBUTTONUP:
        bottomright = [(x, y)]
        print(bottomright)
        cv2.rectangle(source, topleft[0], bottomright[0], (0, 255, 0), 3)
        copy = source.copy()

        x = (bottomright[0][0], topleft[0][0])
        y = (bottomright[0][1], topleft[0][1])
        print(x)
        print(y)
        crop = copy[y[1]:y[0], x[1]:x[0]]
        print(crop.shape)
        # plt.imshow(crop[:,:,::-1])
        # plt.show()
        cv2.imwrite("output.jpg", crop)

def run():
    """
    program logic
    """
    global source
    source = cv2.imread("lion.jpg",1)
    dummy = source.copy()

    cv2.namedWindow("submission")
    cv2.setMouseCallback("submission", drawBoundingBox)

    k = 0
    while k!=27 :
        cv2.imshow("submission", source)
        cv2.putText(source,"drag from top left to bottom right. ESC to close.", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255), 1)
        k = cv2.waitKey(20) & 0xFF
    cv2.destroyAllWindows()

def hr():
    """
    just draw a console line
    """
    print('#' * 80)

# run with: python submission.py
# draw a bounding box and it will create a crop image
if __name__ == "__main__":
    hr()
    run()
    hr()
