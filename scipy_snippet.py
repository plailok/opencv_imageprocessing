import numpy as np
import scipy.ndimage as snd
from PIL import Image
import cv2


def read_and_save(image):
    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, img_bw) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('gray', img_gray)
    cv2.imshow('binary', img_bw)
    # img_bw - binary version of original image
    im_name = image.split('.')[0]
    cv2.imwrite(f'{im_name}_binary.jpeg', img_bw)
    cv2.waitKey()


def dilation(img, kernel):
    dilation_image = cv2.dilate(img, kernel, iterations=3)
    cv2.imshow('dilate', dilation_image)


def erosion(img, kernel):
    erosion_image = cv2.erode(img, kernel, iterations=3)
    cv2.imshow('erosive', erosion_image)


def opening(img, kernel):
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('opening', opening)


def closing(img, kernel):
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closing', closing)


def morph_fradient(img, kernel):
    grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('gradient', grad)


def top_hat(img, kernel):
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow('top hat', tophat)


def black_hat(img, kernel):
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    cv2.imshow('black hat', blackhat)


def kernel_rect(size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))


def kernel_elipse(size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))


if __name__ == '__main__':
    image = 'two_circle_binary.jpeg'
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.imread(image)
    dilation(img=img, kernel=kernel)
    erosion(img=img, kernel=kernel)
    cv2.waitKey()
