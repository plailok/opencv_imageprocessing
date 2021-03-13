import cv2
import numpy as np
import os

DATE = '03.08.2021'
BACKGROUND = f'C:\\Users\\Student\\Desktop\\experiment_fishcolor\\{DATE}\\Background\\background.jpeg'
PATH_BG = os.path.normpath(BACKGROUND)
EXPERIMENTAL = f'C:\\Users\\Student\\Desktop\\experiment_fishcolor\\{DATE}\ControlGroup\\C-1(1).jpeg'
PATH_EXP = os.path.normpath(EXPERIMENTAL)

# open image
image = cv2.imread(PATH_BG)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
bg = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
out_gray = cv2.divide(image, bg, scale=255)
out_binary = cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU)[1]

cv2.imshow('binary', out_binary)
cv2.imshow('gray', out_gray)

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
