import cv2 as cv


def calc_fps():
    """
    advanced calc fps by moving window 10,
    and play video as intended fps
    """

    capture = cv.VideoCapture('capture.avi')
    fps = capture.get(cv.CAP_PROP_FPS)

    # so, this will be the T for every frame
    T = 1. / fps

    freq = cv.getTickFrequency()

    # will use buff like a circular queue
    buff_size = 10
    buff_idx = 0
    buff = [0] * buff_size

    cnt = 0
    start_time = cv.getTickCount() / freq

    while True:
        valid, frame = capture.read()
        if not valid:
            break

        tick = cv.getTickCount()
        dt = (tick - buff[buff_idx]) / freq  # delta t of 10 frames
        fps_e = int(buff_size / dt)  # fps estimated

        buff[buff_idx] = tick
        buff_idx = (buff_idx + 1) % buff_size

        cv.putText(frame, str(fps_e), (10, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv.imshow('frame', frame)

        cnt += 1
        curr_time = cv.getTickCount() / freq

        # remaining time = start_time + T * frame_cnt - current_time
        delay = start_time + T * cnt - curr_time
        if cv.waitKey(max(int(delay*1000), 1)) == 27:
            break
    capture.release()


if __name__ == '__main__':
    calc_fps()
