import cv2 as cv


def contrast():
    """
    what will be better to increase contrast?
    alpha(mul) or gamma(add)?
    """

    img0 = cv.imread('cat.jpg')
    img1 = cv.addWeighted(img0, 1.2, img0, 0, 0)
    img2 = cv.addWeighted(img0, 1, img0, 0, 100)

    cv.imshow('img0', img0)
    cv.imshow('img1', img1)
    cv.imshow('img2', img2)

    cv.waitKey(0)


if __name__ == '__main__':
    contrast()
