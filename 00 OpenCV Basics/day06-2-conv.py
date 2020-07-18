import cv2 as cv
import numpy as np


def do_conv(img, kernel):
    """
    apply kernel to the target image

    :param img: target image
    :param kernel: kernel matrix
    :return: new kernel applied image
    """

    h_half, w_half = kernel.shape[0] // 2, kernel.shape[1] // 2

    padded_shape = list(img.shape)
    padded_shape[0] += h_half * 2
    padded_shape[1] += w_half * 2

    padded_img = np.zeros(padded_shape, dtype=img.dtype)
    np.copyto(padded_img[h_half:h_half+img.shape[0], w_half:w_half+img.shape[1]], img)

    dst = np.zeros(img.shape, dtype=img.dtype)
    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            roi = padded_img[i:i+1+(h_half*2), j:j+1+(w_half*2)]
            dst[i, j] = (roi * kernel).sum()
    return dst


def blur():
    """
    blur image using average filter
    """

    img = cv.imread('filter_blur.jpg', cv.IMREAD_GRAYSCALE)

    k = 9
    # average filter
    kernel = np.full((k, k), (1. / k**2))
    blurred_img = do_conv(img, kernel)

    cv.imshow('img', img)
    cv.imshow('blurred_img', blurred_img)
    cv.waitKey(0)


if __name__ == '__main__':
    blur()
