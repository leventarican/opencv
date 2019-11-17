import cv2
import matplotlib.pyplot as plt

# https://en.wikipedia.org/wiki/QR_code
# https://en.wikipedia.org/wiki/File:Qr-1.png

def read():
    filename = '../qr-1.png'
    img = cv2.imread(filename)

    print(img.shape)

    return img

def qrcode(img):
    detector = cv2.QRCodeDetector()

    # img: grayscale or color (BGR) image containing QR code
    retval, points, straight_qrcode = detector.detectAndDecode(img)
    if retval:
        print(points)

def show(img):
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    img = read()
    qrcode(img)
    show(img)