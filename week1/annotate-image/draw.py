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

def draw_ellipse(img):
    center = (200, 200)
    axes = (40, 20) # radius of the ellipse major and minor axes
    angle = 0   # rotate ellipse
    start_angle = 0
    end_angle = 360
    cv2.ellipse(img, center, axes, angle, start_angle, end_angle, color=(0, 0, 255), thickness=4)
    # rotate the next ellipse (=90°), end angle = 180, half fill (just a negativ thickness)
    cv2.ellipse(img, (200, 250), axes, 90, start_angle, 180, color=(0, 255, 255), thickness=-2)

def draw_rectangle(img):
    top_left_vertex = (250, 250)
    bottom_right_vertex = (300, 300)
    cv2.rectangle(img, top_left_vertex, bottom_right_vertex, color=(200, 0, 0), thickness=-1)

def draw_text(img):
    text = 'hello lion'
    bottom_left_corner = (100, 400)
    font_face = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1.5
    cv2.putText(img, text, bottom_left_corner, font_face, font_scale, color=(0,255,0), thickness=2)

    # calculate the font_scale for the desired pixel height
    pixel_height = 20
    font_scale = cv2.getFontScaleFromHeight(font_face, pixel_height, thickness=2)
    print(f'desired font_scale: {font_scale}')

    cv2.putText(img, text, bottom_left_corner, font_face, font_scale, color=(255,0,0), thickness=2)

    # now center the text
    print(f"# {img.shape}") # (480, 440, 3)
    img_height, img_width = img.shape[:2]  # start, stop, step: [0:2:0] or [:2]
    print(f"img height: {img_height}; img width: {img_width}")
    text_size, base_line = cv2.getTextSize(text, font_face, font_scale, thickness=2)
    text_width, text_height = text_size
    print(f'text width: {text_width}; text height: {text_height}; base line: {base_line}')
    x_center = (img_width - text_width) // 2
    y_position = (img_height - base_line - 10)  # 10 pixel above bottom
    cv2.putText(img, text, (x_center, y_position), font_face, font_scale, color=(0,0,255), thickness=2)

if __name__ == "__main__":
    path = 'lion.jpg'
    img = load_image(path)
    draw_line(img)
    draw_circle(img)
    draw_ellipse(img)
    draw_rectangle(img)
    draw_text(img)

    display_image(img)