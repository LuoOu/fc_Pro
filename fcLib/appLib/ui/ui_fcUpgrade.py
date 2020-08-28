# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fcUpgrade.ui'
#
# Created: Wed Aug 26 12:49:23 2020
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!
import Qt
print Qt.__binding__
from Qt import QtCore, QtGui, QtWidgets

class Ui_FcUpgrade(object):
    def setupUi(self, FcUpgrade):
        FcUpgrade.setObjectName("FcUpgrade")
        FcUpgrade.resize(300, 200)
        FcUpgrade.setMinimumSize(QtCore.QSize(300, 200))
        FcUpgrade.setAutoFillBackground(False)
        FcUpgrade.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(FcUpgrade)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labtext = QtWidgets.QLabel(FcUpgrade)
        self.labtext.setMinimumSize(QtCore.QSize(0, 80))
        self.labtext.setAlignment(QtCore.Qt.AlignCenter)
        self.labtext.setObjectName("labtext")
        self.verticalLayout_4.addWidget(self.labtext)
        self.listWidget = QtWidgets.QListWidget(FcUpgrade)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_4.addWidget(self.listWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.lineUpgradePath = QtWidgets.QLineEdit(FcUpgrade)
        self.lineUpgradePath.setObjectName("lineUpgradePath")
        self.lineUpgradePath.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_6.addWidget(self.lineUpgradePath)
        self.verticalWidget = QtWidgets.QWidget(FcUpgrade)
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 25))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.verticalWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_6.addWidget(self.verticalWidget)
        self.verticalWidget1 = QtWidgets.QWidget(FcUpgrade)
        self.verticalWidget1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalWidget1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(100, 0, 100, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnUpgrade = QtWidgets.QPushButton(self.verticalWidget1)
        self.btnUpgrade.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnUpgrade.setObjectName("btnUpgrade")
        self.horizontalLayout.addWidget(self.btnUpgrade)
        self.verticalLayout_6.addWidget(self.verticalWidget1)
        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.retranslateUi(FcUpgrade)
        self.btnUpgrade.clicked['bool'].connect(self.lineUpgradePath.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(FcUpgrade)

    def retranslateUi(self, FcUpgrade):
        _translate = QtCore.QCoreApplication.translate
        FcUpgrade.setWindowTitle(_translate("FcUpgrade", "Upgrade"))
        self.labtext.setText(_translate("FcUpgrade", "Please set the update package path"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("FcUpgrade", "新建项目"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.btnUpgrade.setText(_translate("FcUpgrade", "Upgrade"))

