import cv2 as cv
import numpy as np


def draw_contours():
    """
    apply threshold, and draw contours of remaining objects
    """

    img = np.zeros((480, 640, 3), dtype=np.uint8)
    cv.circle(img, (200, 150), 80, (255, 255, 0), -1)
    cv.circle(img, (500, 150), 50, (255, 0, 0), -1)
    cv.rectangle(img, (300, 300), (500, 400), (0, 255, 255), -1)

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, thresh_img = cv.threshold(gray_img, 150, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thresh_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    for c in contours:
        print(c.shape, cv.contourArea(c))

    # for i in range(contours[0].shape[0]):
    #     cv.circle(img, (contours[0][i, 0, 0], contours[0][i, 0, 1]), 3, (0, 255, 0), -1)

    cv.drawContours(img, contours, -1, (0, 0, 255), 3)

    cv.imshow('img', img)
    cv.imshow('gray_img', gray_img)
    cv.imshow('thresh_img', thresh_img)
    cv.waitKey(0)


if __name__ == '__main__':
    draw_contours()
