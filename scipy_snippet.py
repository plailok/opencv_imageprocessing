import numpy as np

from datetime import datetime
import cv2


def read_and_save(img):
    print(img)
    image = cv2.imread(img, 0)
    ret, trash = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)
    # img_bw - binary version of original image
    im_name = '\\Result_image\\' + img.split('.')[0]
    print(im_name)
    cv2.imwrite(f'{im_name}_binary.jpeg', trash)
    return f'{im_name}_binary.jpeg'


def dilation(img, kernel, iter=3):
    image = cv2.imread(img)
    dilation_image = cv2.dilate(image, kernel, iterations=iter)
    im_name = 'Result_image/' + img.split('.')[0]
    save_image(f'{im_name}_dilate.jpeg', dilation_image)
    return f'{im_name}_dilate.jpeg'


def erosion(img, kernel, iter=3):
    image = cv2.imread(img)
    erosion_image = cv2.erode(image, kernel, iterations=iter)
    im_name = 'Result_image/' + img.split('.')[0]
    save_image(f'{im_name}_erode.jpeg', erosion_image)
    return f'{im_name}_erode.jpeg'


def opening(img, kernel, iter=3):
    image = cv2.imread(img)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=iter)
    im_name = 'Result_image/' + img.split('.')[0]
    save_image(f'{im_name}_open.jpeg', opening)
    return f'{im_name}_open.jpeg'


def closing(img, kernel, iter=3):
    image = cv2.imread(img)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=iter)
    im_name = 'Result_image/' + img.split('.')[0]
    save_image(f'{im_name}_close.jpeg', closing)
    return f'{im_name}_close.jpeg'


def morph_gradient(img, kernel, iter=3):
    image = cv2.imread(img)
    grad = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel, iterations=iter)
    im_name = 'Result_image/' + img.split('.')[0]
    save_image(f'{im_name}_grad.jpeg', grad)
    return f'{im_name}_grad.jpeg'


def top_hat(img, kernel, iter=3):
    image = cv2.imread(img)
    tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel, iterations=iter)
    im_name = 'Result_image/' + img.split('.')[0]
    save_image(f'{im_name}_tophat.jpeg', tophat)
    return f'{im_name}_tophat.jpeg'


def black_hat(img, kernel, iter=3):
    image = cv2.imread(img)
    blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel, iterations=iter)
    im_name = 'Result_image/' + img.split('.')[0]
    save_image(f'{im_name}_blackhat.jpeg', blackhat)
    return f'{im_name}_blackhat.jpeg'


def kernel_rect(size):
    return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))


def kernel_ellipse(size):
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))


def save_image(name, image):
    cv2.imwrite(name, image)


if __name__ == '__main__':
    img = 'two_circle.jpeg'
    kernel = np.ones((5, 5), np.uint8)
    d = dilation(img=img, kernel=kernel)
    e = erosion(img=img, kernel=kernel)
    o = opening(img=img, kernel=kernel)
    c = closing(img=img, kernel=kernel)
    m = morph_gradient(img=img, kernel=kernel)
    t = top_hat(img=img, kernel=kernel)
    b = black_hat(img=img, kernel=kernel)
