import cv2
from datetime import datetime

date = datetime.now()
d_today = datetime.today()
d_current = datetime.year


# img = cv2.imread('gray.png')  # load a dummy image
# with open('chr-ord.txt', mode='a+', encoding='utf8') as file:
#     while True:
#         cv2.imshow('img', img)
#         k = cv2.waitKey(33)
#         if k == 27:  # Esc key to stop
#             file.write(f'End of TEST {date}')
#             break
#         elif k == -1:  # normally -1 returned,so don't print it
#             continue
#         else:
#             print(f"{chr(k)} = {k}\n")
#             file.write(f"{chr(k)} = {k}\n")
