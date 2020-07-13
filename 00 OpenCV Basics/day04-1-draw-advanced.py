import cv2 as cv
import numpy as np

LINE_MODE = 0
RECT_MODE = 1
CIRC_MODE = 2
FREE_MODE = 3


def handle_mode(img, mode, prev, curr):
    """
    helper function for draw()

    :param img: target image (np array)
    :param mode: mode (LINE_MODE, RECT_MODE, CIRC_MODE), int
    :param prev: previous (x, y) point, tuple
    :param curr: current (x, y) point, tuple
    """
    if mode == LINE_MODE:
        cv.line(img, prev, curr, (255, 0, 255), 5)
    if mode == RECT_MODE:
        cv.rectangle(img, prev, curr, (0, 255, 0), 5)
    if mode == CIRC_MODE:
        radius = (prev[0] - curr[0]) ** 2 + (prev[1] - curr[1]) ** 2
        radius = radius ** (1 / 2)
        cv.circle(img, prev, int(radius), (0, 255, 255), 5)


def draw():
    """
    ms-paint-like program that can draw straight line, rectangle, circle, free line
    """

    img = np.ndarray((480, 640, 3), dtype=np.uint8)
    data = {
        'prev_x': 0,
        'prev_y': 0,
        'clicked': False,
        'mode': LINE_MODE
    }

    def on_mouse(event, x, y, flags, param):
        prev = (data['prev_x'], data['prev_y'])
        curr = (x, y)

        if event == cv.EVENT_LBUTTONDOWN:
            data['clicked'] = True
            data['prev_x'] = x
            data['prev_y'] = y
        if data['clicked'] and event == cv.EVENT_MOUSEMOVE:
            if data['mode'] == FREE_MODE:
                cv.line(img, prev, curr, (255, 255, 255), 5)
                data['prev_x'] = x
                data['prev_y'] = y
                cv.imshow('img', img)
            else:
                tmp = img.copy()
                handle_mode(tmp, data['mode'], prev, curr)
                cv.imshow('img', tmp)
        if event == cv.EVENT_LBUTTONUP:
            data['clicked'] = False
            handle_mode(img, data['mode'], prev, curr)
            cv.imshow('img', img)

    cv.imshow('img', img)
    cv.setMouseCallback('img', on_mouse)
    while True:
        key = cv.waitKey(0)
        if key == 27:
            cv.imwrite('draw.png', img)
            break

        if 49 <= key <= 52:
            data['mode'] = key - 49


if __name__ == '__main__':
    draw()
