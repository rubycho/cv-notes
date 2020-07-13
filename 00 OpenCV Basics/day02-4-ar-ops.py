import cv2 as cv
import numpy as np


def add_sub_ops():
    """
    simple add, sub operations between np arrays
    """

    mat0 = np.uint8([[130, 140], [150, 160]])
    mat1 = np.uint8([[100, 100], [100, 100]])
    mat2 = np.uint8([[145, 145], [145, 145]])

    print('mat0:\n', mat0)
    print('mat1:\n', mat1)
    print('mat2:\n', mat2)

    print('mat0 + mat1:\n', mat0+mat1)
    print('cv.add(mat0, mat1):\n', cv.add(mat0, mat1))

    print('mat0 - mat2:\n', mat0-mat2)
    print('cv.subtract(mat0, mat2):\n', cv.subtract(mat0, mat2))

    print('cv.addWeighted(mat0, mat1):\n',
          cv.addWeighted(mat0, 0.7, mat1, 0.3, 0))


def image_ops():
    """
    compare between np + and cv add
    """

    img1 = cv.imread('add1.jpg')
    img2 = cv.imread('add2.jpg')

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)

    cv.imshow('img1+img2', img1+img2)
    cv.imshow('cv.add(img1, img2)', cv.add(img1, img2))

    cv.waitKey(0)


def blend_image_ops():
    """
    blend two images, automatically changing alpha
    """

    alpha = 0

    img1 = cv.imread('add1.jpg')
    img2 = cv.imread('add2.jpg')

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)

    reverse = False
    while cv.waitKey(30) < 0:
        if reverse:
            alpha -= 0.01
        else:
            alpha += 0.01
        if alpha <= 0:
            reverse = False
        if alpha >= 1:
            reverse = True

        blended = cv.addWeighted(img1, alpha, img2, 1-alpha, 0)
        cv.imshow('blended', blended)


if __name__ == '__main__':
    # add_sub_ops()
    # image_ops()
    blend_image_ops()
