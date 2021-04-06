import os
import cv2

refPt = []
cropping = False


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        # cv2.rectangle(image, refPt[0], refPt[1], (0, 0, 0), 2)
        # cv2.imshow("image", image)


names = ['ControlGroup', 'ExperimentalGroup']
DATE = '04.05.2021'
PATH = f'C:\\Users\\Student\\Desktop\\experiment_fishcolor\\{DATE}\\ExperimentalGroup\\'
SIZE = (100, 150)  # input size in format (x/2,y/2)
path1 = os.path.normpath(PATH)
for dirpath, dirnames, filenames in os.walk(path1):
    for file in filenames:
        file_name = f'{dirpath}/{file}'
        image = cv2.imread(os.path.normpath(file_name))
        clone = image.copy()
        cv2.namedWindow(file)
        cv2.setMouseCallback(file, click_and_crop)
        while True:
            # display the image and wait for a keypress
            cv2.imshow(file, image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                cv2.destroyAllWindows()
                break
            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                image = clone.copy()
            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                cv2.destroyWindow(file)
                if len(refPt) == 2:
                    roi = clone[refPt[0][1] - SIZE[0]:refPt[0][1] + SIZE[0],
                          refPt[0][0] - SIZE[1]:refPt[1][0] + SIZE[1]]
                    if file[-3:] == 'png':
                        crop_image_name = os.path.normpath(f'{dirpath}/crop-{file[:-3]}jpeg')
                    else:
                        crop_image_name = os.path.normpath(f'{dirpath}/crop-{file[:-4]}jpeg')
                    try:
                        cv2.imwrite(crop_image_name, roi)
                        cv2.imshow("ROI", roi)
                    except Exception as exc:
                        print(f'WE have an error {exc}')
                        print('You click to close to the border try another point, or change the size of image')
                        continue
                    else:
                        cv2.waitKey(5)
                        break
                # close all open windows
                cv2.destroyAllWindows()
                cv2.waitKey()
