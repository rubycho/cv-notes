import cv2 as cv
import numpy as np

img1 = np.zeros([300, 300], dtype=np.uint8)
img2 = np.zeros([300, 300], dtype=np.uint8)
mask = np.zeros([300, 300], dtype=np.uint8)

cv.circle(img1, (150, 150), 100, 255, -1)
cv.rectangle(img2, (0, 0), (150, 300), 255, -1)
cv.rectangle(mask, (0, 0), (300, 150), 255, -1)


def bitwise_and():
    """
    try and bitwise operation with mask
    """

    img1_and_img2 = cv.bitwise_and(img1, img2)
    img1_and_img2_mask = cv.bitwise_and(img1, img2, mask=mask)

    dst_img = np.full([300, 300], 127, dtype=np.uint8)
    cv.bitwise_and(img1, img2, dst=dst_img, mask=mask)

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('mask', mask)
    cv.imshow('img1&img2', img1_and_img2)
    cv.imshow('img1&img2 mask', img1_and_img2_mask)
    cv.imshow('img1&img2 mask dst', dst_img)
    cv.waitKey(0)


def bitwise_oth():
    """
    try other bitwise operations with mask
    """

    img1_or_img2_mask = cv.bitwise_or(img1, img2, mask=mask)
    img1_xor_img2_mask = cv.bitwise_xor(img1, img2, mask=mask)
    img1_not = cv.bitwise_not(img1, mask=mask)

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('mask', mask)
    cv.imshow('img1|img2 mask', img1_or_img2_mask)
    cv.imshow('img1^img2 mask', img1_xor_img2_mask)
    cv.imshow('~img1', img1_not)
    cv.waitKey()


if __name__ == '__main__':
    # bitwise_and()
    bitwise_oth()
