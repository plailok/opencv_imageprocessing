import numpy as np
import scipy.ndimage as snd
from PIL import Image
import cv2


def read_and_save(image):
    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, img_bw) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # img_bw - binary version of original image
    im_name = image.split('.')[0]
    cv2.imwrite(f'{im_name}_binary.jpeg', img_bw)
    return f'{im_name}_binary.jpeg'


def dilation(img, kernel):
    image = cv2.imread(img)
    dilation_image = cv2.dilate(image, kernel, iterations=3)
    save_image(f'{img.split(".")[0]}_dilation.jpeg', dilation_image)
    return f'{img.split(".")[0]}_dilation.jpeg'


def erosion(img, kernel):
    image = cv2.imread(img)
    erosion_image = cv2.erode(image, kernel, iterations=3)
    save_image(f'{img.split(".")[0]}_erode.jpeg', erosion_image)
    return f'{img.split(".")[0]}_erode.jpeg'


def opening(img, kernel):
    image = cv2.imread(img)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    save_image(f'{img.split(".")[0]}_opened.jpeg', opening)
    return f'{img.split(".")[0]}_opened.jpeg'


def closing(img, kernel):
    image = cv2.imread(img)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    save_image(f'{img.split(".")[0]}_closed.jpeg', closing)
    return f'{img.split(".")[0]}_closed.jpeg'


def morph_gradient(img, kernel):
    image = cv2.imread(img)
    grad = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    save_image(f'{img.split(".")[0]}_grad.jpeg', grad)
    return f'{img.split(".")[0]}_grad.jpeg'


def top_hat(img, kernel):
    image = cv2.imread(img)
    tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    save_image(f'{img.split(".")[0]}_tophat.jpeg', tophat)
    return f'{img.split(".")[0]}_tophat.jpeg'


def black_hat(img, kernel):
    image = cv2.imread(img)
    blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    save_image(f'{img.split(".")[0]}_tophat.jpeg', blackhat)
    return f'{img.split(".")[0]}_tophat.jpeg'


def kernel_rect(size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))


def kernel_ellipse(size):
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))


def save_image(name, image):
    cv2.imwrite(name, image)


if __name__ == '__main__':
    image = 'two_circle_binary.jpeg'
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.imread(image)
    dilation(img=img, kernel=kernel)
    erosion(img=img, kernel=kernel)
    opening(img=img, kernel=kernel)
    closing(img=img, kernel=kernel)
    morph_gradient(img=img, kernel=kernel)
    top_hat(img=img, kernel=kernel)
    cv2.waitKey()
