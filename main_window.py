# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 663)
        MainWindow.setMinimumSize(QSize(856, 650))
        MainWindow.setStyleSheet(u"QPushButton {\n"
"	color: red;\n"
"	font: bold, 14px;\n"
"}\n"
"QFrame {\n"
"	background-color: grey;}\n"
"QMainWindow{\n"
"	background-color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"	min-width: 200px;\n"
"	min-height: 50px;\n"
"	border-style:inset;\n"
"	border-radius: 10px;\n"
"	border-width: 2px;\n"
"	background-color: rgb(20,20,20)	;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: blue;\n"
"}\n"
"QPushButton:checked {\n"
"	border-color: green;}")
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dilationButton = QPushButton(self.frame_2)
        self.dilationButton.setObjectName(u"dilationButton")
        self.dilationButton.setMinimumSize(QSize(204, 54))
        self.dilationButton.setCheckable(True)
        self.dilationButton.setChecked(True)
        self.dilationButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dilationButton)

        self.erosionButton = QPushButton(self.frame_2)
        self.erosionButton.setObjectName(u"erosionButton")
        self.erosionButton.setCheckable(True)
        self.erosionButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.erosionButton)

        self.openingButton = QPushButton(self.frame_2)
        self.openingButton.setObjectName(u"openingButton")
        self.openingButton.setCheckable(True)
        self.openingButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.openingButton)

        self.closingButton = QPushButton(self.frame_2)
        self.closingButton.setObjectName(u"closingButton")
        self.closingButton.setCheckable(True)
        self.closingButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.closingButton)

        self.morphButton = QPushButton(self.frame_2)
        self.morphButton.setObjectName(u"morphButton")
        self.morphButton.setCheckable(True)
        self.morphButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.morphButton)

        self.blackhatButton = QPushButton(self.frame_2)
        self.blackhatButton.setObjectName(u"blackhatButton")
        self.blackhatButton.setCheckable(True)
        self.blackhatButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.blackhatButton)

        self.tophatButton = QPushButton(self.frame_2)
        self.tophatButton.setObjectName(u"tophatButton")
        self.tophatButton.setCheckable(True)
        self.tophatButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.tophatButton)

        self.chosekernelButton = QPushButton(self.frame_2)
        self.chosekernelButton.setObjectName(u"chosekernelButton")
        self.chosekernelButton.setCheckable(True)
        self.chosekernelButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.chosekernelButton)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 2, 1)

        self.sourceBox = QGroupBox(self.frame)
        self.sourceBox.setObjectName(u"sourceBox")
        self.sourceBox.setStyleSheet(u"QPushButton {\n"
"	min-width: 150px;\n"
"	min-height: 25px;\n"
"	border-style: outset;\n"
"	border-radius: 10px;\n"
"	border-color: green;\n"
"	border-width: 3px;\n"
"	background-color: rbg(20,20,20);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: blue;\n"
"}\n"
"QGroupBox{\n"
"	background-color: gray;	\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"	subcontrol-position: top-center;\n"
"    padding: 2 10px;\n"
"	border-radius: 10px;\n"
"	color: red;\n"
"	font: 75 12pt \"Arial\";\n"
"    background-color: rgb(20,20,20);\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.sourceBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sourceLabel = QLabel(self.sourceBox)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.sourceLabel.setScaledContents(True)
        self.sourceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.sourceLabel)

        self.choseimButton = QPushButton(self.sourceBox)
        self.choseimButton.setObjectName(u"choseimButton")
        self.choseimButton.setMaximumSize(QSize(100, 16777215))
        self.choseimButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.choseimButton)


        self.gridLayout_2.addWidget(self.sourceBox, 0, 1, 1, 1)

        self.resultBox = QGroupBox(self.frame)
        self.resultBox.setObjectName(u"resultBox")
        self.resultBox.setStyleSheet(u"QPushButton {\n"
"	min-width: 150px;\n"
"	min-height: 25px;\n"
"	border-style: outset;\n"
"	border-radius: 10px;\n"
"	border-color: red;\n"
"	border-width: 3px;\n"
"	background-color: rbg(20,20,20);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: blue;\n"
"}\n"
"QGroupBox{\n"
"	background-color: gray;	\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"	subcontrol-position: top-center;\n"
"    padding: 2 10px;\n"
"	border-radius: 10px;\n"
"	color: red;\n"
"	font: bold, 12pt;\n"
"    background-color: rgb(20,20,20);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.resultBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.resultLabel = QLabel(self.resultBox)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setScaledContents(True)
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel.setMargin(10)

        self.verticalLayout_2.addWidget(self.resultLabel)

        self.stepButton = QPushButton(self.resultBox)
        self.stepButton.setObjectName(u"stepButton")
        self.stepButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_2.addWidget(self.stepButton)


        self.gridLayout_2.addWidget(self.resultBox, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 5)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.choseimButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dilationButton.setText(QCoreApplication.translate("MainWindow", u"DILATION", None))
        self.erosionButton.setText(QCoreApplication.translate("MainWindow", u"EROSION", None))
        self.openingButton.setText(QCoreApplication.translate("MainWindow", u"OPENING", None))
        self.closingButton.setText(QCoreApplication.translate("MainWindow", u"CLOSING", None))
        self.morphButton.setText(QCoreApplication.translate("MainWindow", u"MORPH GRADIENT", None))
        self.blackhatButton.setText(QCoreApplication.translate("MainWindow", u"BLACK HAT", None))
        self.tophatButton.setText(QCoreApplication.translate("MainWindow", u"TOP HAT", None))
        self.chosekernelButton.setText(QCoreApplication.translate("MainWindow", u"CHOSE KERNEL", None))
        self.sourceBox.setTitle(QCoreApplication.translate("MainWindow", u"Soucre Image", None))
        self.sourceLabel.setText(QCoreApplication.translate("MainWindow", u"Choose your image by using button below", None))
        self.choseimButton.setText(QCoreApplication.translate("MainWindow", u"Chose Image", None))
        self.resultBox.setTitle(QCoreApplication.translate("MainWindow", u"Result Image", None))
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"Here will be the result of method you'we chose.", None))
        self.stepButton.setText(QCoreApplication.translate("MainWindow", u"Step by Step", None))
    # retranslateUi

