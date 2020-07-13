import cv2 as cv


def print_mouse_event():
    """
    set mouse callback and see what's doing
    """

    def on_mouse(event, x, y, flags, param):
        print(event, x, y, flags, param)

    image = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

    cv.namedWindow('image')
    cv.setMouseCallback('image', on_mouse)

    cv.imshow('image', image)
    cv.waitKey(0)


def click_and_wheel():
    """
    set mouse callback, print on specific events,
    note that flags > 0 on event == MOUSEWHEEL means up wheel
    """

    def on_mouse(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            print('left btn down at ', x, y)
        if event == cv.EVENT_LBUTTONUP:
            print('left btn up at ', x, y)
        if event == cv.EVENT_RBUTTONDOWN:
            print('right btn down at ', x, y)
        if event == cv.EVENT_RBUTTONUP:
            print('right btn up at ', x, y)
        if event == cv.EVENT_LBUTTONDBLCLK:
            print('left btn dbclk at ', x, y)
        if event == cv.EVENT_RBUTTONDBLCLK:
            print('right btn dbclk at ', x, y)
        if event == cv.EVENT_MOUSEWHEEL:
            if flags > 0:
                print('wheel up at ', x, y)
            else:
                print('wheel down at ', x, y)

    image = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

    cv.namedWindow('image')
    cv.setMouseCallback('image', on_mouse)

    cv.imshow('image', image)
    cv.waitKey(0)


if __name__ == '__main__':
    # print_mouse_event()
    click_and_wheel()
