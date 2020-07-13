import cv2 as cv


def capture_video():
    """
    capture video and save
    """

    capture = cv.VideoCapture(0)
    width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(capture.get(cv.CAP_PROP_FPS))

    print('width, height, fps = ', width, height, fps)

    fourcc = cv.VideoWriter_fourcc(*'DX50')
    writer = cv.VideoWriter('capture.avi', fourcc, fps, (width, height))

    while cv.waitKey(30) < 0:
        valid, frame = capture.read()
        writer.write(frame)
        cv.imshow('img', frame)
    capture.release()
    writer.release()


def play_video():
    """
    play saved video
    """

    video = cv.VideoCapture('capture.avi')
    fps = video.get(cv.CAP_PROP_FPS)

    while cv.waitKey(int(1000/fps)) < 0:
        valid, frame = video.read()
        if valid:
            cv.imshow('frame', frame)


if __name__ == '__main__':
    capture_video()
    # play_video()
