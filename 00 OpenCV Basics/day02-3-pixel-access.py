import cv2 as cv
import numpy as np


def access_pixels():
    """
    create np array, set BGR value and show it
    """

    image = np.zeros([480, 640, 3], dtype=np.uint8)
    image[235:240, 315:320] = (0, 255, 0)
    image[235:240, 325:330] = (0, 0, 255)

    cv.imshow('image', image)
    cv.waitKey(0)


def gradation():
    """
    create a gradation image (np array)
    """

    image = np.zeros([500, 500], dtype=np.uint8)
    for i in range(0, 500):
        for j in range(0, 500):
            image[i, j] = ((i+j)/1000) * 255
    cv.imshow('image', image)
    cv.waitKey(0)


def red_to_0():
    """
    read image and remove R channel value
    """

    image = cv.imread('cat.jpg')
    image[:, :, 2] = 0

    cv.imshow('image', image)
    cv.waitKey(0)


def split_channels():
    """
    split each channels, now it will be shown like grayscale
    """

    image = cv.imread('cat.jpg')
    b, g, r = cv.split(image)

    cv.imshow('image', image)
    cv.imshow('b', b)
    cv.imshow('g', g)
    cv.imshow('r', r)

    cv.waitKey(0)


if __name__ == '__main__':
    # access_pixels()
    # gradation()
    # red_to_0()
    split_channels()
