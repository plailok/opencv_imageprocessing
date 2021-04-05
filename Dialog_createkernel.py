# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chose_kernel_dialog.ui'
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
        Dialog.resize(801, 237)
        Dialog.setStyleSheet(u"QFrame {\n"
"	background-color:rgb(100,100,100);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton {\n"
"	color: red;\n"
"	min-width: 200px;\n"
"	min-height: 50px;\n"
"	border-style:inset;\n"
"	border-radius: 10px;\n"
"	border-width: 2px;\n"
"	background-color: rgb(20,20,20)	;\n"
"}\n"
"QLabel {\n"
"	color:red;\n"
"	background-color: black;\n"
"	border-radius: 10px;\n"
"	font: bold, 14px\n"
"}\n"
"QSpinBox {\n"
"    padding-right: 15px; /* make room for the arrows */\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    border-width: 3;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    border-image: url(:/images/spinup.png) 1;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"    border-image: url(:/images/spinup_hover.png) 1;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    border-imag"
                        "e: url(:/images/spinup_pressed.png) 1;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/images/up_arrow.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max */\n"
"   image: url(:/images/up_arrow_disabled.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    border-image: url(:/images/spindown.png) 1;\n"
"    border-width: 1px;\n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"    border-image: url(:/images/spindown_hover.png) 1;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    border-image: url(:/images/spindown_pressed.png) 1;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/images/down_arrow.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off { /* off state"
                        " when value in min */\n"
"   image: url(:/images/down_arrow_disabled.png);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.xLabel = QLabel(self.frame)
        self.xLabel.setObjectName(u"xLabel")
        self.xLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.xLabel, 0, 0, 1, 1)

        self.xSpinBox = QSpinBox(self.frame)
        self.xSpinBox.setObjectName(u"xSpinBox")
        self.xSpinBox.setStyleSheet(u"color: red;")
        self.xSpinBox.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.xSpinBox, 0, 1, 1, 1)

        self.ySpinBox = QSpinBox(self.frame)
        self.ySpinBox.setObjectName(u"ySpinBox")
        self.ySpinBox.setStyleSheet(u"color:red;")
        self.ySpinBox.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ySpinBox, 1, 1, 1, 1)

        self.typeButton = QPushButton(self.frame)
        self.typeButton.setObjectName(u"typeButton")
        self.typeButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.typeButton, 2, 0, 1, 2)

        self.yLabel = QLabel(self.frame)
        self.yLabel.setObjectName(u"yLabel")
        self.yLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.yLabel, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color:white;\n"
"background-radius:15px;")

        self.gridLayout.addWidget(self.textBrowser, 0, 2, 3, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 6)
        self.gridLayout.setRowMinimumHeight(0, 30)
        self.gridLayout.setRowMinimumHeight(1, 30)
        self.gridLayout.setRowMinimumHeight(2, 50)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.OKButton = QPushButton(self.frame)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setStyleSheet(u"max-width:200px;\n"
"")

        self.horizontalLayout_2.addWidget(self.OKButton)

        self.CancelButton = QPushButton(self.frame)
        self.CancelButton.setObjectName(u"CancelButton")

        self.horizontalLayout_2.addWidget(self.CancelButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.xLabel.setText(QCoreApplication.translate("Dialog", u"\u0425", None))
        self.typeButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.yLabel.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">In this window, you can create your own pixel layout for the methods from the previous window. Several parameters are available to you: settings for the size </span><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#00ff00;\">(x, y)</span><span style=\" font-size:10pt; color:#ff0000;\"> of the matrix and the type of the kernel. In the future, it will be possible to manually select the pixel arrangement.</span></p></body></html>", None))
        self.OKButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

