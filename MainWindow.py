import sys
import os

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
import numpy as np

from main_window import Ui_MainWindow as mwindow
from scipy_snippet import *
from step_by_step import step_by_step


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.kernel = np.ones((5, 5), np.uint8)
        self.image_bw = None
        self.dilation = None
        self.erosion = None
        self.opening = None
        self.closing = None
        self.grad = None
        self.tophat = None
        self.blackhat = None
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

        self.ui.stepButton.clicked.connect(self.__step_by_step_clicked)

    def __chose_image(self):
        if not self.dilation:
            dir = os.getcwd()
            path = QFileDialog.getOpenFileName(self, 'Open Image', dir, "Image Files (*.png *.jpg *.bmp *.jpeg)")
            self.image_bw = read_and_save(path[0])
            image = QPixmap(self.image_bw)
            new_image = image.scaled(540, 249, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.put_image(widget=self.ui.sourceLabel, image=self.image_bw)

    def __dilation_clicked(self):
        self.put_image(widget=self.ui.resultLabel,
                       image=self.dilation) if self.dilation is not None else self.put_image(widget=self.ui.resultLabel,
                                                                                             image=dilation(
                                                                                                 self.image_bw,
                                                                                                 self.kernel))

    def __erosion_clicked(self):
        self.put_image(widget=self.ui.resultLabel,
                       image=self.erosion) if self.erosion is not None else self.put_image(widget=self.ui.resultLabel,
                                                                                           image=erosion(
                                                                                               self.image_bw,
                                                                                               self.kernel))

    def __opening_clicked(self):
        self.put_image(widget=self.ui.resultLabel,
                       image=self.opening) if self.opening is not None else self.put_image(widget=self.ui.resultLabel,
                                                                                           image=opening(
                                                                                               self.image_bw,
                                                                                               self.kernel))

    def __closing_clicked(self):
        self.put_image(widget=self.ui.resultLabel,
                       image=self.closing) if self.closing is not None else self.put_image(widget=self.ui.resultLabel,
                                                                                           image=closing(
                                                                                               self.image_bw,
                                                                                               self.kernel))

    def __morph_gradient_clicked(self):
        self.put_image(widget=self.ui.resultLabel,
                       image=self.grad) if self.grad is not None else self.put_image(widget=self.ui.resultLabel,
                                                                                     image=morph_gradient(
                                                                                         self.image_bw,
                                                                                         self.kernel))

    def __black_hat_clicked(self):
        self.put_image(widget=self.ui.resultLabel,
                       image=self.blackhat) if self.blackhat is not None else self.put_image(widget=self.ui.resultLabel,
                                                                                             image=black_hat(
                                                                                                 self.image_bw,
                                                                                                 self.kernel))

    def __top_hat_clicked(self):
        self.put_image(widget=self.ui.resultLabel,
                       image=self.tophat) if self.tophat is not None else self.put_image(widget=self.ui.resultLabel,
                                                                                         image=top_hat(
                                                                                             self.image_bw,
                                                                                             self.kernel))

    def clear_label(self):
        pass

    def __step_by_step_clicked(self):
        step_by_step()

    @staticmethod
    def put_image(widget, image):
        widget.setPixmap(image)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())
