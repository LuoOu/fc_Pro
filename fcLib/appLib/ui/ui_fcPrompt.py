# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fcPrompt.ui'
#
# Created: Fri Aug 21 17:34:01 2020
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FcPrompt(object):
    def setupUi(self, FcPrompt):
        FcPrompt.setObjectName("FcPrompt")
        FcPrompt.resize(300, 200)
        FcPrompt.setMinimumSize(QtCore.QSize(300, 200))
        FcPrompt.setAutoFillBackground(False)
        FcPrompt.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(FcPrompt)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalWidget_2 = QtWidgets.QWidget(FcPrompt)
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelText = QtWidgets.QLabel(self.verticalWidget_2)
        self.labelText.setMaximumSize(QtCore.QSize(16777215, 50))
        self.labelText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelText.setObjectName("labelText")
        self.verticalLayout_3.addWidget(self.labelText)
        self.verticalLayout_6.addWidget(self.verticalWidget_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.linPrint = QtWidgets.QLineEdit(FcPrompt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linPrint.sizePolicy().hasHeightForWidth())
        self.linPrint.setSizePolicy(sizePolicy)
        self.linPrint.setMinimumSize(QtCore.QSize(0, 100))
        self.linPrint.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.linPrint.setObjectName("linPrint")
        self.linPrint.setReadOnly(True)
        self.verticalLayout_4.addWidget(self.linPrint)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalWidget = QtWidgets.QWidget(FcPrompt)
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnClose = QtWidgets.QPushButton(self.verticalWidget)
        self.btnClose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout_2.addWidget(self.btnClose)
        self.verticalLayout_6.addWidget(self.verticalWidget)
        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.retranslateUi(FcPrompt)
        QtCore.QMetaObject.connectSlotsByName(FcPrompt)

    def retranslateUi(self, FcPrompt):
        _translate = QtCore.QCoreApplication.translate
        FcPrompt.setWindowTitle(_translate("FcPrompt", "Prompt"))
        self.labelText.setText(_translate("FcPrompt", "TextLabel"))
        self.linPrint.setText(_translate("FcPrompt", "test"))
        self.btnClose.setText(_translate("FcPrompt", "Close"))

