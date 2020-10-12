# ##############################################################################
# create image mask
# ##############################################################################

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
    matplotlib.rcParams['image.cmap'] = 'gray'
    img = cv2.imread('lion.jpg')

    run(img)

    plt.show()
