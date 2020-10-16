import cv2
import math

# detect mouse events: left-click, right-click and position
# we need a named window and assign a callback function to the window

# Lists to store the points
center=[]
circumference=[]

# img	=	cv.circle(	img, center, radius, color[, thickness[, lineType[, shift]]]	)
# a callback funciton. referenced in cv2.setMouseCallback(...)
def drawCircle(action, x, y, flags, userdata):
    global center, circumference

    # left button DOWN: draw a dot
    if action==cv2.EVENT_LBUTTONDOWN:
        center=[(x,y)]
        cv2.circle(source, center[0], 1, (255,255,0), 2, cv2.LINE_AA);

    # left button UP: on mouse release draw the circle
    elif action==cv2.EVENT_LBUTTONUP:
        circumference=[(x,y)]
        
        radius = math.sqrt(math.pow(center[0][0]-circumference[0][0],2)+
        math.pow(center[0][1]-circumference[0][1],2))

        cv2.circle(source, center[0], int(radius), (0,255,0),2, cv2.LINE_AA)
        cv2.imshow("mouse-events", source)

source = cv2.imread("lion.jpg",1)
dummy = source.copy()

cv2.namedWindow("mouse-events")
# highgui function called when mouse events occur
cv2.setMouseCallback("mouse-events", drawCircle)

# loop until ESC
k = 0
while k!=27 :
    cv2.imshow("mouse-events", source)
    cv2.putText(source,'''Choose center, and drag, 
    Press ESC to exit and c to clear''' , (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255), 1)
    k = cv2.waitKey(20) & 0xFF

    if k==99:
        print("clear screen")
        source= dummy.copy()

cv2.destroyAllWindows()
