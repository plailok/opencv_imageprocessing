import numpy as np
import scipy.ndimage as snd
from PIL import Image
import cv2
import time


def empty(x):
    pass


def back():
    pass


def resize_image(image):
    return cv2.resize(src=image, dsize=(277, 199))


def step_by_step():
    cv2.namedWindow('TrackBar', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('Max', 'TrackBar', 0, 255, empty)
    cv2.createTrackbar('Min', 'TrackBar', 0, 255, empty)
    image = cv2.imread('3circles.png', 0)
    cv2.imshow('OriginalImage', image)
    img_b, img_z = step_1(image)
    result = np.concatenate((resize_image(image), resize_image(img_b), resize_image(img_z)), axis=0)
    cv2.imshow('Result of first step', result)
    cv2.imwrite('image_binary.png', img_b)
    time.sleep(2)
    print('STEP#2: creating KERNEL')
    kernel, size = step_2()
    print('STEP#3: Processing')
    step_3(img_b, int(size), kernel)


def coloring_pixes(kernel, point, image=None):
    for index_i, i in enumerate(kernel):
        for index_j, j in enumerate(i):
            if j == 1:
                pixel_coord = (point[1] + index_j, point[0] + index_i)
                image[pixel_coord[0], pixel_coord[1]] = 1
    return image


def step_3(image, size, kernel):
    '''Пройтись по картике'''
    height, width = image.shape
    delta = size // 2
    cv2.namedWindow('TrackBar', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('x_pos', 'TrackBar', 0, width, empty)
    cv2.createTrackbar('y_pos', 'TrackBar', 0, height, empty)
    while True:
        x = cv2.getTrackbarPos('x_pos', 'TrackBar')
        y = cv2.getTrackbarPos('y_pos', 'TrackBar')
        point_1 = (x - delta, y - delta)
        point_2 = (x + delta, y + delta)
        image = coloring_pixes(kernel, image=cv2.imread('image_binary.png'), point=point_1)
        cv2.imshow('Step3', image)
        if cv2.waitKey(1) == 27:
            break
        else:
            continue


def step_2():
    while True:
        print('IMPORTANT: size in format !"5 5"! ')
        line = input('Give me size of Kernel: ')
        splited = line.split(' ')
        if len(splited) == 2:
            cv2.destroyWindow('Result of first step')
            return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (int(splited[0]), int(splited[-1]))), splited[0]
        else:
            continue


def step_1(image):
    while True:
        maximum = cv2.getTrackbarPos('Max', 'TrackBar')
        minimum = cv2.getTrackbarPos('Min', 'TrackBar')
        ret, trash = cv2.threshold(image, minimum, maximum, cv2.THRESH_BINARY)
        ret, trash0 = cv2.threshold(image, minimum, maximum, cv2.THRESH_TOZERO)
        cv2.imshow('Binary', trash)
        cv2.imshow('Zero', trash0)
        if cv2.waitKey(1) == 27:
            break
        elif cv2.waitKey(1) == 110:
            print('Move to the next Step#2 Creation of Kernel')
            cv2.destroyWindow('Binary')
            cv2.destroyWindow('Zero')
            cv2.destroyWindow('TrackBar')
            cv2.destroyWindow('OriginalImage')
            return trash, trash0
        else:
            continue


if __name__ == '__main__':
    # kernel, size = step_2()
    # image = coloring_pixes(kernel, image=cv2.imread('3circles.png'), point=(100, 100))
    # cv2.imshow('result', image)
    step_by_step()
    cv2.waitKey(0)
