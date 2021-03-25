import sys
from PIL import Image as im
import os

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PySide6.QtGui import QPixmap
import numpy as np
import cv2

from Dialog_steps import Ui_Dialog as StepDialog


class StepByStep(QDialog):

    def __init__(self, image, method):
        super(StepByStep, self).__init__()
        self.ui = StepDialog()
        self.ui.setupUi(self)

        self.info = {'STEP#0': image,
                     'STEP#1': None,
                     'STEP#2': None,
                     'STEP#3': None,
                     'kernel': None,
                     'method': method}
        self.kernels = ['Rectangle', 'Ellipse', 'Cross']
        self.kernels_code = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]
        self.sizes = [(x, x) for x in range(31) if x % 2 == 1 and x >= 3]
        self.current_step = 'STEP#0'
        self.__setup_ui()

    def __setup_ui(self):
        self.ui.nextStepLabel.setText('The result of next step will be showen here')
        self.ui.stepButton_1.clicked.connect(self._step_1)
        self.ui.stepButton_2.clicked.connect(self._step_2)
        self.ui.stepButton_3.clicked.connect(self._step_3)
        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.pushButton.clicked.connect(self.clear)
        self.ui.stepButton_2.setEnabled(False)
        self.ui.stepButton_3.setEnabled(False)

        self.ui.minSlider.setEnabled(False)
        self.ui.minSlider.setEnabled(False)
        self.put_image_current(image=self.info[self.current_step])

    def _step_1(self):
        self.current_step = 'STEP#1'
        self.ui.stepButton_2.setEnabled(True)
        self.ui.stepButton_1.setEnabled(False)
        self.ui.maxSlider.sliderMoved.connect(self.renew_max)
        self.ui.minSlider.sliderMoved.connect(self.renew_min)
        self.ui.minvalueLabel.setText('0')
        self.ui.maxvalueLabel.setText('0')
        self.ui.maxSlider.setEnabled(True)
        self.ui.minSlider.setEnabled(True)
        self.ui.maxSlider.setMaximum(255)
        self.ui.minSlider.setMaximum(255)

    def _step_2(self):
        self.put_image_current(image=self.info[self.current_step])
        self.current_step = 'STEP#2'
        self.ui.stepButton_2.setEnabled(False)
        self.ui.stepButton_3.setEnabled(True)
        self.ui.nextStepLabel.setText('Wait for Kernel')
        self.ui.label_3.setText('Type')
        self.ui.label_4.setText('Size')

        self.ui.minSlider.setMaximum(len(self.kernels) - 1)
        self.ui.minSlider.setSliderPosition(0)

        self.ui.maxSlider.setMaximum(len(self.sizes) - 1)
        self.ui.maxSlider.setSliderPosition(0)

    def _step_3(self):
        self.put_image_current(self.info['STEP#0'])
        self.current_step = 'STEP#3'
        self.ui.stepButton_3.setEnabled(False)
        self.ui.nextStepLabel.setText('Wait for number of iteration you want')
        self.ui.label_4.setText('Iterations')
        self.ui.maxSlider.setMaximum(10)
        self.ui.maxSlider.setMinimum(1)
        self.ui.maxSlider.setSliderPosition(5)

    def __step_1(self):
        '''
        Операция которая выполнится в случае, если
        кнопка STEP 1 pressed
        '''
        image = cv2.imread(self.info['STEP#0'], 0)
        minimum = self.ui.minSlider.sliderPosition()
        maximum = self.ui.maxSlider.sliderPosition()
        ret, trash = cv2.threshold(image, minimum, maximum, cv2.THRESH_BINARY)
        name = 'STEP1_BINARY.jpeg'
        cv2.imwrite(name, trash)
        self.info[self.current_step] = name
        self.put_image_next(image=name)

    def __step_2(self, size):
        '''
        Операция которая выполнится в случае, если
        кнопка STEP 2 pressed
        '''
        image = cv2.imread(self.info['STEP#1'])
        s1, s2 = size.split('x')
        self.size = (int(s1), int(s2))
        point1 = (50, 50)
        self.info['kernel'] = cv2.getStructuringElement(self.kernels_code[self.ui.minSlider.sliderPosition()],
                                                        self.size)
        im = self.coloring_pixes(image=image, point=point1, kernel=self.info['kernel'])
        name = 'STEP2_KERNEL.jpeg'
        self.info[self.current_step] = name
        cv2.imwrite(name, im)
        self.put_image_next(image=name)

    def __step_3(self, iteration):
        '''
        Автоматически применяем выставленные настройки
        и показываем результат в зависимости от количества итераций
        '''
        image = cv2.imread(self.info['STEP#0'], 0)
        kern = self.kernels_code[self.ui.minSlider.sliderPosition()]
        self.info['kernel'] = cv2.getStructuringElement(kern, ksize=self.size)
        processed_image = self.info['method'](src=image, kernel=self.info['kernel'], iterations=iteration)
        name = f'STEP3_RESULT.jpeg'
        cv2.imwrite(name, processed_image)
        self.put_image_next(image=name)

    def renew_max(self, x):
        '''
        Операция которая выполняеться при
        изменении позиции слайдера
        '''
        self.ui.maxvalueLabel.setText(str(x))
        if self.current_step == 'STEP#1':
            self.__step_1()
        elif self.current_step == 'STEP#2':
            size = f'{self.sizes[x][0]}x{self.sizes[x][1]}'
            self.ui.maxvalueLabel.setText(size)
            self.__step_2(size)
        elif self.current_step == 'STEP#3':
            self.__step_3(iteration=x)

    def renew_min(self, y):
        '''
        Операция которая выполняеться при
        изменении позиции слайдера
        '''
        self.ui.minvalueLabel.setText(str(y))
        if self.current_step == 'STEP#1':
            self.__step_1()
        elif self.current_step == 'STEP#2':
            text = self.kernels[y]
            self.ui.minvalueLabel.setText(text)
            size = f'{self.sizes[self.ui.maxSlider.sliderPosition()][0]}x{self.sizes[self.ui.maxSlider.sliderPosition()][1]}'
            self.__step_2(size)
        elif self.current_step == 'STEP#3':
            text = self.kernels[y]
            self.ui.minvalueLabel.setText(text)
            iteration = self.ui.maxSlider.sliderPosition()
            self.__step_3(iteration)

    # Put an image to one of frame (current/next)
    def put_image_current(self, image):
        im = QPixmap(image)
        cur_image = im.scaled(540, 249, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.currentStepLabel.setPixmap(cur_image)

    def put_image_next(self, image):
        im = QPixmap(image)
        next_image = im.scaled(540, 249, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.nextStepLabel.setPixmap(next_image)

    def exit(self):
        pass

    def clear(self):
        image = self.info['STEP#0']
        method = self.info['method']
        self.info = {'STEP#0': image,
                     'STEP#1': None,
                     'STEP#2': None,
                     'STEP#3': None,
                     'kernel': None,
                     'method': method}
        self.current_step = 'STEP#0'
        self.ui.nextStepLabel.setText('The result of next step will be showen here')
        self.ui.stepButton_1.setEnabled(True)
        self.ui.stepButton_2.setEnabled(False)
        self.ui.stepButton_3.setEnabled(False)
        self.ui.stepButton_1.setChecked(False)
        self.ui.stepButton_2.setChecked(False)
        self.ui.stepButton_3.setChecked(False)

    @staticmethod
    def coloring_pixes(kernel, point, image=None):
        '''
        Красим пиксели внутри квадрата,
        согласно значения в кернеле
        '''
        for index_i, i in enumerate(kernel):
            for index_j, j in enumerate(i):
                if j == 1:
                    pixel_coord = (point[1] + index_j, point[0] + index_i)
                    image[pixel_coord[0], pixel_coord[1]] = (0, 0, 255) if index_j == len(i) // 2 and index_i == len(
                        i) // 2 and index_i == index_j else (200, 50, 150)
        return image


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = StepByStep(image='two_circle.jpeg', method=cv2.dilate)
    dialog.show()

    sys.exit(app.exec_())
