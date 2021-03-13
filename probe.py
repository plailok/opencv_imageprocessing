import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

DATE = '03.08.2021'
BACKGROUND = f'C:\\Users\\Student\\Desktop\\experiment_fishcolor\\{DATE}\\Background\\background.jpeg'
PATH_BG = os.path.normpath(BACKGROUND)
EXPERIMENTAL = f'C:\\Users\\Student\\Desktop\\experiment_fishcolor\\{DATE}\ControlGroup\\C-1(1).jpeg'
PATH_EXP = os.path.normpath(EXPERIMENTAL)

# open image
image = cv2.imread(PATH_EXP)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
bg = cv2.morphologyEx(img, cv2.MORPH_DILATE, se)
out_gray = cv2.divide(img, bg, scale=255)
out_binary = cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU)[1]
cv2.imshow('binary', out_gray)
cv2.imshow('gray', out_gray)
# cv2.imwrite('binary.png', out_binary)
# cv2.imwrite('gray.png', out_gray)


cv2.waitKey()
