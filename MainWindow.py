import sys
import os
from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
import numpy as np

from main_window import Ui_MainWindow as mwindow
from Dialog import StepByStep, CreateKernel
from scipy_snippet import *
from step_by_step import step_by_step


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.dir = os.getcwd()
        self.current_date = f'{datetime.year}.{datetime.month}.{datetime.day}'
        self.current_method = dilation
        self.kernels = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]
        self.image_bw = None
        self.dilation = None
        self.erosion = None
        self.opening = None
        self.closing = None
        self.grad = None
        self.tophat = None
        self.blackhat = None
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        self.ui = mwindow()
        self.ui.setupUi(self)
        self.__setup_ui()

    def __setup_ui(self):
        self.ui.choseimButton.clicked.connect(self.__chose_image)
        self.ui.dilationButton.clicked.connect(self.__dilation_clicked)
        self.ui.erosionButton.clicked.connect(self.__erosion_clicked)
        self.ui.openingButton.clicked.connect(self.__opening_clicked)
        self.ui.closingButton.clicked.connect(self.__closing_clicked)
        self.ui.morphButton.clicked.connect(self.__morph_gradient_clicked)
        self.ui.blackhatButton.clicked.connect(self.__black_hat_clicked)
        self.ui.tophatButton.clicked.connect(self.__top_hat_clicked)
        self.ui.chosekernelButton.clicked.connect(self.__change_kenrel_clicked)

    def __chose_image(self):
        dir = os.getcwd()
        path = QFileDialog.getOpenFileName(self, 'Open Image', dir, "Image Files (*.png *.jpg *.bmp *.jpeg)")
        self.image = path[0].split('/')[-1]
        im = cv2.imread(self.image, 0)
        ret, trash = cv2.threshold(im, 240, 255, cv2.THRESH_BINARY)
        self.image_bw = self.image.split('.')[0] + '_binary.jpg'
        cv2.imwrite(self.image_bw, trash)
        image = QPixmap(self.image_bw)
        new_image = image.scaled(540, 249, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.put_image(widget=self.ui.sourceLabel, image=new_image)

    def __dilation_clicked(self):
        self.current_method = dilation
        self.dilation = dilation(
            self.image_bw,
            self.kernel)
        self.put_image(widget=self.ui.resultLabel,
                       image=self.dilation)

    def __erosion_clicked(self):
        self.current_method = erosion
        self.erosion = erosion(
            self.image_bw,
            self.kernel)
        self.put_image(widget=self.ui.resultLabel,
                       image=self.erosion)

    def __opening_clicked(self):
        self.current_method = opening
        self.opening = opening(
            self.image_bw,
            self.kernel)
        self.put_image(widget=self.ui.resultLabel,
                       image=self.opening)

    def __closing_clicked(self):
        self.current_method = closing
        self.closing = closing(
            self.image_bw,
            self.kernel)
        self.put_image(widget=self.ui.resultLabel,
                       image=self.closing)

    def __morph_gradient_clicked(self):
        self.current_method = morph_gradient
        self.grad = morph_gradient(
            self.image_bw,
            self.kernel)
        self.put_image(widget=self.ui.resultLabel,
                       image=self.grad)

    def __black_hat_clicked(self):
        self.current_method = black_hat
        self.blackhat = black_hat(
            self.image_bw,
            self.kernel)
        self.put_image(widget=self.ui.resultLabel,
                       image=self.blackhat)

    def __top_hat_clicked(self):
        self.current_method = top_hat
        self.tophat = top_hat(
            self.image_bw,
            self.kernel)
        self.put_image(widget=self.ui.resultLabel,
                       image=self.tophat)

    def __change_kenrel_clicked(self):
        Dialog = CreateKernel()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.kernel = cv2.getStructuringElement(self.kernels[Dialog.current_index], (Dialog.x, Dialog.y))
            print(self.kernel)

    def clear_label(self):
        self.ui.sourceLabel.setText('Chose Your Image by pressing button bellow!')

    def __step_by_step_clicked(self):
        dialog = StepByStep(image=self.image, method=self.current_method)
        dialog.exec_()

    @staticmethod
    def put_image(widget, image):
        widget.setPixmap(image)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())
