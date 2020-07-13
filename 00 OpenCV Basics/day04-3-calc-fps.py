import cv2 as cv


def calc_fps():
    """
    calculate fps on every 10 frames
    """

    capture = cv.VideoCapture(0)
    cnt, fps, t0 = 0, 0, cv.getTickCount()

    while cv.waitKey(1) != 27:
        valid, frame = capture.read()
        cv.putText(frame, str(fps), (10, 60), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)
        cv.imshow('frame', frame)

        cnt += 1
        if cnt == 10:
            t1 = cv.getTickCount()
            dt = (t1 - t0) / cv.getTickFrequency()
            fps = int(cnt / dt)
            cnt, t0 = 0, t1


if __name__ == '__main__':
    calc_fps()
