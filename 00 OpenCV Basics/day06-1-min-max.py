import cv2 as cv
import numpy as np

MIN = 0
MAX = 1


def min_max():
    """
    get min, max value and its location on image(array)
    """

    img = np.array([[2, 1, 3],
                    [7, 5, 4]], dtype=np.uint8)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img)

    print('img:')
    print(img)

    print('min val (x, y): ', min_val, min_loc)
    print('max val (x, y): ', max_val, max_loc)

    mask = np.array([[0, 1, 1],
                     [0, 1, 1]], dtype=np.uint8)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img, mask)

    print('mask:')
    print(mask)

    print('min val (x, y): ', min_val, min_loc)
    print('max val (x, y): ', max_val, max_loc)


def min_max_filter_2d(img, kernel_size=3, flag=MIN):
    """
    apply min or max filter on one 2d image (H, W)

    :param img: target image
    :param kernel_size: kernel size (odd)
    :param flag: MIN or MAX
    :return: new filter applied image
    """

    h_half = w_half = kernel_size // 2

    dst = np.zeros(img.shape, dtype=img.dtype)
    dst_shape = dst.shape
    for i in range(dst_shape[0]):
        for j in range(dst_shape[1]):
            roi = img[max(0, i - h_half):min(dst_shape[0] - 1, i + h_half),
                        max(0, j - w_half):min(dst_shape[1] - 1, j + w_half)]
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(roi)
            dst[i][j] = min_val if flag == MIN else max_val
    return dst


def min_max_filter_3d(img, kernel_size=3, flag=MIN):
    """
    apply min or max filter on one 3d image (multiple channels)

    :param img: target image
    :param kernel_size: kernel size (odd)
    :param flag: MIN or MAX
    :return: new filter applied image
    """

    dst = np.zeros(img.shape, dtype=img.dtype)

    for i in range(dst.shape[2]):
        dst[:, :, i] = min_max_filter_2d(
            img[:, :, i],
            kernel_size,
            flag
        )
    return dst


def min_max2():
    """
    apply min or max filter on grayscale image
    """

    img = cv.imread('min_max.jpg', cv.IMREAD_GRAYSCALE)
    min_filtered = min_max_filter_2d(img, 7, MIN)
    max_filtered = min_max_filter_2d(img, 7, MAX)

    cv.imshow('img', img)
    cv.imshow('min', min_filtered)
    cv.imshow('max', max_filtered)
    cv.waitKey(0)


def min_max3():
    """
    apply min or max filter on color image, try also on V channel of HSV
    """

    img = cv.imread('min_max.jpg')

    min_filtered = min_max_filter_3d(img, 7, MIN)
    max_filtered = min_max_filter_3d(img, 7, MAX)

    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    v_min_filtered = min_max_filter_2d(hsv_img[:, :, 2], 7, MIN)
    v_max_filtered = min_max_filter_2d(hsv_img[:, :, 2], 7, MAX)

    hsv_min_filtered = hsv_img.copy()
    hsv_max_filtered = hsv_img.copy()

    hsv_min_filtered[:, :, 2] = v_min_filtered
    hsv_max_filtered[:, :, 2] = v_max_filtered

    hsv_min_filtered = cv.cvtColor(hsv_min_filtered, cv.COLOR_HSV2BGR)
    hsv_max_filtered = cv.cvtColor(hsv_max_filtered, cv.COLOR_HSV2BGR)

    cv.imshow('img', img)
    cv.imshow('min', min_filtered)
    cv.imshow('max', max_filtered)
    cv.imshow('hsv_min', hsv_min_filtered)
    cv.imshow('hsv_max', hsv_max_filtered)
    cv.waitKey(0)


if __name__ == '__main__':
    # min_max()
    # min_max2()
    min_max3()
