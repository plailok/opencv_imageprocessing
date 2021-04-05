# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step_by_step.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1014, 720)
        Dialog.setStyleSheet(u"QPushButton {\n"
                             "	color: red;\n"
                             "	font: bold, 14px;\n"
                             "}\n"
                             "QDialog{\n"
                             "	background-color:black}\n"
                             "QFrame {\n"
                             "	background-color: grey;}\n"
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
                             "QLabel {\n"
                             "	color: red;\n"
                             "	background-color: black;\n"
                             "	font: 14px, bold;\n"
                             "}\n"
                             "")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.NextStepBox = QGroupBox(Dialog)
        self.NextStepBox.setObjectName(u"NextStepBox")
        self.gridLayout_5 = QGridLayout(self.NextStepBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.nextStepLabel = QLabel(self.NextStepBox)
        self.nextStepLabel.setObjectName(u"nextStepLabel")

        self.gridLayout_5.addWidget(self.nextStepLabel, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.NextStepBox, 1, 0, 1, 1)

        self.ButtonsBox = QGroupBox(Dialog)
        self.ButtonsBox.setObjectName(u"ButtonsBox")
        self.ButtonsBox.setMinimumSize(QSize(0, 250))
        self.ButtonsBox.setStyleSheet(u"QPushButton {\n"
                                      "	min-width: 100px;\n"
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
        self.gridLayout_2 = QGridLayout(self.ButtonsBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.ButtonsBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.stepButton_1 = QPushButton(self.ButtonsBox)
        self.stepButton_1.setObjectName(u"stepButton_1")
        self.stepButton_1.setCheckable(True)
        self.stepButton_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.stepButton_1)

        self.stepButton_2 = QPushButton(self.ButtonsBox)
        self.stepButton_2.setObjectName(u"stepButton_2")
        self.stepButton_2.setCheckable(True)
        self.stepButton_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.stepButton_2)

        self.stepButton_3 = QPushButton(self.ButtonsBox)
        self.stepButton_3.setObjectName(u"stepButton_3")
        self.stepButton_3.setCheckable(True)
        self.stepButton_3.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.stepButton_3)

        self.exitButton = QPushButton(self.ButtonsBox)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout.addWidget(self.exitButton)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.ButtonsBox, 0, 1, 1, 1)

        self.currStepBox = QGroupBox(Dialog)
        self.currStepBox.setObjectName(u"currStepBox")
        self.gridLayout_3 = QGridLayout(self.currStepBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.currentStepLabel = QLabel(self.currStepBox)
        self.currentStepLabel.setObjectName(u"currentStepLabel")

        self.gridLayout_3.addWidget(self.currentStepLabel, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.currStepBox, 0, 0, 1, 1)

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 2, 2, 1)

        self.threshholderBox = QGroupBox(Dialog)
        self.threshholderBox.setObjectName(u"threshholderBox")
        self.threshholderBox.setMinimumSize(QSize(0, 250))
        self.threshholderBox.setStyleSheet(u"QSlider::groove:horizontal {\n"
                                           "    border: 1px solid #999999;\n"
                                           "    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                           "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                           "    margin: 2px 0;\n"
                                           "}\n"
                                           "\n"
                                           "QSlider::handle:vertical {\n"
                                           "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                           "    border: 1px solid #5c5c5c;\n"
                                           "    width: 18px;\n"
                                           "    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
                                           "    border-radius: 3px;\n"
                                           "}\n"
                                           "QLabel{\n"
                                           "	\n"
                                           "	font: 75 12pt \"Rockwell Nova\";\n"
                                           "}")
        self.gridLayout_4 = QGridLayout(self.threshholderBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(11, -1, -1, -1)
        self.minSlider = QSlider(self.threshholderBox)
        self.minSlider.setObjectName(u"minSlider")
        self.minSlider.setMinimumSize(QSize(0, 0))
        self.minSlider.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.minSlider, 0, 0, 1, 1, Qt.AlignHCenter)

        self.maxSlider = QSlider(self.threshholderBox)
        self.maxSlider.setObjectName(u"maxSlider")
        self.maxSlider.setMinimumSize(QSize(0, 0))
        self.maxSlider.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.maxSlider, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(self.threshholderBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.threshholderBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 1, 1, 1, 1)

        self.minvalueLabel = QLabel(self.threshholderBox)
        self.minvalueLabel.setObjectName(u"minvalueLabel")
        self.minvalueLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.minvalueLabel, 2, 0, 1, 1)

        self.maxvalueLabel = QLabel(self.threshholderBox)
        self.maxvalueLabel.setObjectName(u"maxvalueLabel")
        self.maxvalueLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.maxvalueLabel, 2, 1, 1, 1)

        self.gridLayout_4.setRowStretch(0, 5)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)

        self.gridLayout.addWidget(self.threshholderBox, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.NextStepBox.setTitle(QCoreApplication.translate("Dialog", u"Step's Result", None))
        self.nextStepLabel.setText(QCoreApplication.translate("Dialog", u"NextStep", None))
        self.ButtonsBox.setTitle(QCoreApplication.translate("Dialog", u"Steps Button", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"New", None))
        self.stepButton_1.setText(QCoreApplication.translate("Dialog", u"Step #1", None))
        self.stepButton_2.setText(QCoreApplication.translate("Dialog", u"Step #2", None))
        self.stepButton_3.setText(QCoreApplication.translate("Dialog", u"Step #3", None))
        self.exitButton.setText(QCoreApplication.translate("Dialog", u"Exit", None))
        self.currStepBox.setTitle(QCoreApplication.translate("Dialog", u"Current Image", None))
        self.currentStepLabel.setText(QCoreApplication.translate("Dialog", u"Current step", None))
        self.threshholderBox.setTitle(QCoreApplication.translate("Dialog", u"ThreshHolder", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"MINIMUM", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"MAXIMUM", None))
        self.minvalueLabel.setText(QCoreApplication.translate("Dialog", u"CURRENT", None))
        self.maxvalueLabel.setText(QCoreApplication.translate("Dialog", u"CURRENT", None))
    # retranslateUi
