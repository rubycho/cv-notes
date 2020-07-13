import cv2 as cv
import numpy as np


# 전체 밝기 유지, 대비 높이기
# 1.5 * img0 - 0.5 * mean
def contrast_safe():
    """
    keep mean brightness, but increase contrast:
    (img - mean) * 1.5 + mean
    = img * 1.5 - mean * 0.5
    """

    img0 = cv.imread('cat.jpg')
    mean = np.zeros(img0.shape, dtype=np.uint8)

    mean[:, :] = np.mean(img0, (0, 1))

    scale = 1.5
    img1 = cv.addWeighted(img0, scale, mean, 1 - scale, 0)

    cv.imshow('img0', img0)
    cv.imshow('mean', mean)
    cv.imshow('img1', img1)
    cv.waitKey(0)


if __name__ == '__main__':
    contrast_safe()
