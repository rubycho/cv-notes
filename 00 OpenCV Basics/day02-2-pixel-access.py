import cv2 as cv
import numpy as np


def create_image():
    """
    create np array and show it
    """

    image = np.zeros([480, 640, 3], dtype=np.uint8)
    cv.imshow('image', image)
    cv.waitKey(0)


def pattern_image():
    """
    create np array and change (pixel) values
    """

    image = np.zeros([480, 640, 3], dtype=np.uint8)
    image[0:160, :, 0] = 255
    image[160:320, :, 1] = 255
    image[320:480, :, 2] = 255

    cv.imshow('image', image)
    cv.waitKey(0)


def rectangle_image():
    """
    create np array and make a green rectangle
    """

    image = np.zeros([480, 640, 3], dtype=np.uint8)
    image[120:360, 200:440, 1] = 255

    cv.imshow('image', image)
    cv.waitKey(0)


def save_image():
    """
    create np array and save as file
    """

    image = np.zeros([480, 640, 3], dtype=np.uint8)
    image[:, ::3, 0] = 255
    image[:, 1::3, 1] = 255
    image[:, 2::3, 2] = 255

    cv.imwrite('file.png', image)


def save_gray_image():
    """
    read and save as gray scale
    """

    image = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)

    cv.imwrite('gray_cat.png', image)


if __name__ == '__main__':
    # create_image()
    # pattern_image()
    # rectangle_image()
    # save_image()
    save_gray_image()
