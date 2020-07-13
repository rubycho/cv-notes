import cv2 as cv
import numpy as np


def draw():
    """
    functions that draw...
    """

    img = np.zeros([480, 640, 3], dtype=np.uint8)
    cv.line(img, (20, 20), (620, 460), (0, 255, 0), 5)
    cv.rectangle(img, (100, 100), (400, 400), (0, 0, 255), 5)
    cv.rectangle(img, (500, 100), (600, 200), (255, 0, 0), -1)
    cv.circle(img, (320, 240), 100, (255, 255, 0), 3)
    cv.ellipse(img, (320, 240), (300, 200), 10, 0, 360, (0, 255, 255), 5)

    pts = np.array([[50, 150], [200, 80], [350, 120], [300, 200]], dtype=np.int32)
    cv.polylines(img, [pts.reshape((-1, 1, 2))], True, (255, 0, 255), 5)

    # use fillPoly to fill the polygon
    pts = np.array([[350, 350], [500, 280], [630, 320], [520, 320]], dtype=np.int32)
    cv.fillPoly(img, [pts.reshape((-1, 1, 2))], (0, 0, 255))

    cv.putText(img, 'Hello', (10, 450), cv.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 5)

    cv.imshow('img', img)
    cv.waitKey(0)


def draw_rectangle():
    """
    draw rectangles on a black canvas with mouse event
    """

    img = np.zeros([480, 640, 3], dtype=np.uint8)
    data = {'prev_x': 0, 'prev_y': 0, 'btn_down': False}

    def on_mouse(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            data['btn_down'] = True
            data['prev_x'] = x
            data['prev_y'] = y
        if data['btn_down'] and event == cv.EVENT_MOUSEMOVE:
            tmp = img.copy()
            cv.rectangle(tmp, (data['prev_x'], data['prev_y']), (x, y), (0, 255, 0), 5)
            cv.imshow('img', tmp)
        if event == cv.EVENT_LBUTTONUP:
            data['btn_down'] = False
            cv.rectangle(img, (data['prev_x'], data['prev_y']), (x, y), (0, 255, 0), 5)
            cv.imshow('img', img)

    cv.imshow('img', img)
    cv.setMouseCallback('img', on_mouse)
    cv.waitKey(0)


if __name__ == '__main__':
    # draw()
    draw_rectangle()
