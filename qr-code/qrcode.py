import cv2
import matplotlib.pyplot as plt

# https://en.wikipedia.org/wiki/QR_code
# https://en.wikipedia.org/wiki/File:Qr-1.png
# https://docs.opencv.org/4.1.0/de/dc3/classcv_1_1QRCodeDetector.html

filename = '../qr-1.png'
img = cv2.imread(filename)

# print(img.shape)

detector = cv2.QRCodeDetector()

# img: grayscale or color (BGR) image containing QR code
# points: vertices of the detected quadrangle
# straight_qrcode: binarized qr code image; a numpy array
retval, points, straight_qrcode = detector.detectAndDecode(img)
if retval:
    rows, cols = straight_qrcode.shape
    for x in range(0, rows):
        for y in range(0, cols):
            value = straight_qrcode[x][y]
            # print(value)
            if value == 0.: # black pixel
                # print(f'x: {x}; y: {y}')
                pass

# draw boundary box
n = len(points)
for i in range(n):
    pt1 = tuple(points[i][0])
    pt2 = tuple(points[(i+1)%4][0])
    cv2.line(img, pt1, pt2, (0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

print(f'decoded qrcode value: {retval}')

plt.imshow(img)
plt.show()
