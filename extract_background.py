import cv2
import numpy as np
import os

DATE = '03.22.2021'
BACKGROUND = f'C:\\Users\\Student\\Desktop\\experiment_fishcolor\\{DATE}\\Background\\background.jpeg'
PATH_BG = os.path.normpath(BACKGROUND)
EXPERIMENTAL = f'C:\\Users\\Student\\Desktop\\experiment_fishcolor\\{DATE}\ControlGroup\\crop-C-1(2).jpeg'
PATH_EXP = os.path.normpath(EXPERIMENTAL)
size = 3
KERNEL = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
# open image
# image = cv2.imread(PATH_EXP, 0)
# se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
# bg = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
# out_gray = cv2.divide(image, bg, scale=255)
# out_binary = cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU)[1]
# contours, hierarchy = cv2.findContours(out_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
im = cv2.imread(PATH_EXP)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contour)
cv2.drawContours(im, contour, -1, (0, 255, 0), 3)
# mask = contour
# print(mask)
# mask3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
# res = cv2.bitwise_and(im, im, mask=mask)
# im_thresh_gray = cv2.bitwise_or(im, mask3)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('image', im)
cv2.imshow('thresh', thresh)
# cv2.imshow('contour', contour)
# cv2.imshow('withmask', res)

# cv2.imwrite('binary.png', out_binary)
# cv2.imwrite('gray.png', out_gray)

cv2.waitKey()

# for dirpath, dirnames, filenames in os.walk(PATH_BG):
#     for file in filenames:
#         file_name = f'{dirpath}/{file}'
#         bg_image = cv2.imread(os.path.normpath(file_name))
#         # gs_bg_image = cv2.cvtColor(bg_image, cv2.COLOR_BGR2GRAY)
#         hsv_bg_image = cv2.cvtColor(bg_image, cv2.COLOR_BGR2HSV)
#
# for dirpath, dirnames, filenames in os.walk(PATH_EXP):
#     for file in filenames:
#         file_name = f'{dirpath}/{file}'
#         image = cv2.imread(os.path.normpath(file_name))
#         # gs_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#         while True:
#             cv2.imshow(file, image)
#             key = cv2.waitKey(1) & 0xFF
#             if key == ord('q'):
#                 cv2.destroyAllWindows()
#                 break
#             # if the 'c' key is pressed, break from the loop
#             elif key == ord("c"):
#                 # new_image = gs_image - gs_bg_image
#                 new_image = hsv_image - hsv_bg_image
#                 # colored_image = cv2.cvtColor(new_image, cv2.COLOR_GRAY2BGR)
#                 cv2.imshow('Result', new_image)
