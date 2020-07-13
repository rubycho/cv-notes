import cv2 as cv

from matplotlib import pyplot as plt


def version():
    """
    print version of opencv-python
    """
    print(cv.__version__)


def read_image():
    """
    read, show image
    """

    image = cv.imread('cat.jpg')
    print('image is type: ', type(image))
    print('dim of image: ', image.shape, image.dtype)
    print()

    grayscale = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
    print('image is type: ', type(grayscale))
    print('dim of image: ', grayscale.shape, grayscale.dtype)
    print()

    cv.imshow('cat', image)
    cv.imshow('grayscale cat', grayscale)

    cv.waitKey(0)
    cv.destroyAllWindows()


def show_image_esc():
    """
    read, show image and wait until ESC
    """

    image = cv.imread('cat.jpg')
    cv.imshow('cat', image)

    key = cv.waitKeyEx(0)
    while key != 27:
        print('got key: ', key)
        key = cv.waitKeyEx(0)
    cv.destroyAllWindows()


def show_image_plt():
    """
    read image and show with matplotlib plot
    note that opencv imread uses BGR, so we change the order of channels
    """
    image = cv.imread('cat.jpg', cv.IMREAD_COLOR)

    new_image = image.copy()
    new_image[:, :, 0] = image[:, :, 2]
    new_image[:, :, 2] = image[:, :, 0]

    plt.imshow(new_image, interpolation='bicubic')
    plt.xticks([]); plt.yticks([])
    plt.show()


if __name__ == '__main__':
    # version()
    # read_image()
    # show_image_esc()
    show_image_plt()
