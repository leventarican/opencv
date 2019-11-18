import cv2
import matplotlib.pyplot as plt

# https://en.wikipedia.org/wiki/QR_code
# https://en.wikipedia.org/wiki/File:Qr-1.png

def read():
    filename = '../qr-1.png'
    img = cv2.imread(filename)

    # print(img.shape)

    return img

# https://docs.opencv.org/4.1.0/de/dc3/classcv_1_1QRCodeDetector.html
def qrcode(img):
    detector = cv2.QRCodeDetector()

    # img: grayscale or color (BGR) image containing QR code
    # points: vertices of the detected quadrangle
    # straight_qrcode: binarized qr code image; a numpy array
    retval, points, straight_qrcode = detector.detectAndDecode(img)
    if retval:
        img = straight_qrcode
        plt.imshow(straight_qrcode)

        rows, cols = straight_qrcode.shape
        for x in range(0, rows):
            for y in range(0, cols):
                value = straight_qrcode[x][y]
                # print(value)
                if value == 0.: # black pixel
                    print(f'x: {x}; y: {y}')

def show(img):
    # plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    img = read()
    qrcode(img)
    show(img)