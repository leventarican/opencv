import cv2

# OpenCV HighGUI window example

# capture from webcam
cap = cv2.VideoCapture(0)

k=0
while(True):
    ret,frame = cap.read()

    # k in ASCII code. ex. ESC = 27

    # check draw.py for how to put text on screen
    # cv2.putText(img, text, (x_center, y_position), font_face, font_scale, color=(0,0,255), thickness=2)

    # Identify if 'ESC' is pressed or not
    if(k==27):
        break
    
    # Identify if 'e' or 'E' is pressed
    if(k==101 or k==69):
        cv2.putText(frame, "E is pressed, press Z or ESC", (100,180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3);

    # Identify if 'z' or 'Z' is pressed
    if(k==90 or k==122):
        cv2.putText(frame, "Z is pressed", (100,180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

    cv2.imshow("Image",frame)
    
    # waitKey: delay in ms
    # https://docs.opencv.org/4.1.0/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7

    # cv2.waitKey() returns a 32 Bit integer value for ASCII we need 256 (8bit) --> 0xFF
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
    k= cv2.waitKey(10000) & 0xFF

cap.release()
cv2.destroyAllWindows()
