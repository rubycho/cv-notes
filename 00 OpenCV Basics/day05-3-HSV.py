import cv2 as cv


def split_color_space():
    """
    split as HSV and save each channel
    """

    bgr = cv.imread('cat.jpg')
    hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)

    H, S, V = cv.split(hsv)
    cv.imshow('bgr', bgr)
    cv.imshow('H', H)
    cv.imshow('S', S)
    cv.imshow('V', V)

    cv.waitKey()
    cv.imwrite('cat-h.png', H)
    cv.imwrite('cat-s.png', S)
    cv.imwrite('cat-v.png', V)


def merge_color_space():
    """
    read splitted H, S, V image files and merge it
    """

    H = cv.imread('cat-h.png', cv.IMREAD_GRAYSCALE)
    S = cv.imread('cat-s.png', cv.IMREAD_GRAYSCALE)
    V = cv.imread('cat-v.png', cv.IMREAD_GRAYSCALE)

    hsv = cv.merge((H, S, V))
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    cv.imshow('hsv', hsv)
    cv.imshow('bgr', bgr)
    cv.waitKey(0)


def change_hsv():
    """
    alter H, S, V value of image and check the reults
    """

    bgr = cv.imread('cat.jpg')
    hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)

    H, S, V = cv.split(hsv)
    S1 = cv.addWeighted(S, 0.5, S, 0, 0)
    hsv1 = cv.merge((H, S1, V))
    bgr1 = cv.cvtColor(hsv1, cv.COLOR_HSV2BGR)

    S2 = cv.addWeighted(S, 2, S, 0, 0)
    hsv2 = cv.merge((H, S2, V))
    bgr2 = cv.cvtColor(hsv2, cv.COLOR_HSV2BGR)

    H1 = cv.addWeighted(H, 1, H, 0, 90)
    hsv3 = cv.merge((H1, S, V))
    bgr3 = cv.cvtColor(hsv3, cv.COLOR_HSV2BGR)

    cv.imshow('bgr1', bgr1)
    cv.imshow('bgr2', bgr2)
    cv.imshow('bgr3', bgr3)
    cv.waitKey(0)


if __name__ == '__main__':
    # split_color_space()
    # merge_color_space()
    change_hsv()
