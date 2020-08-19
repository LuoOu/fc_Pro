# -*- coding: UTF-8 -*-
#.@FileName:ui_fcLoadTask
#.@Date:2020-06-22:15:55
#.@Aurhor:LuoOu

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_fcLoadTask(object):
    def setupUi(self, FcLoadTask):
        FcLoadTask.setObjectName("FcLoadTask")
        FcLoadTask.resize(720, 300)
        FcLoadTask.setMinimumSize(QtCore.QSize(720, 300))
        FcLoadTask.setStyleSheet("")
        self.layMain = QtWidgets.QHBoxLayout(FcLoadTask)
        self.layMain.setContentsMargins(-1, -1, -1, 4)
        self.layMain.setObjectName("layMain")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lstModule = QtWidgets.QListWidget(FcLoadTask)
        self.lstModule.setStyleSheet("color: rgb(230, 230, 230);")
        self.lstModule.setFrameShape(QtWidgets.QFrame.Box)
        self.lstModule.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstModule.setResizeMode(QtWidgets.QListView.Adjust)
        self.lstModule.setViewMode(QtWidgets.QListView.ListMode)
        self.lstModule.setUniformItemSizes(False)
        self.lstModule.setBatchSize(100)
        self.lstModule.setObjectName("lstModule")
        self.verticalLayout.addWidget(self.lstModule)
        self.lstClass = QtWidgets.QListWidget(FcLoadTask)
        self.lstClass.setMinimumSize(QtCore.QSize(150, 0))
        self.lstClass.setStyleSheet("color: rgb(230, 230, 230);")
        self.lstClass.setFrameShape(QtWidgets.QFrame.Box)
        self.lstClass.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstClass.setObjectName("lstClass")
        self.verticalLayout.addWidget(self.lstClass)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.layMain.addLayout(self.verticalLayout)
        self.lstEntity = QtWidgets.QListWidget(FcLoadTask)
        self.lstEntity.setMinimumSize(QtCore.QSize(120, 0))
        self.lstEntity.setStyleSheet("color: rgb(230, 230, 230);")
        self.lstEntity.setFrameShape(QtWidgets.QFrame.Box)
        self.lstEntity.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstEntity.setObjectName("lstEntity")
        self.layMain.addWidget(self.lstEntity)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstStep = QtWidgets.QListWidget(FcLoadTask)
        self.lstStep.setStyleSheet("color: rgb(230, 230, 230);")
        self.lstStep.setFrameShape(QtWidgets.QFrame.Box)
        self.lstStep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstStep.setObjectName("lstStep")
        self.verticalLayout_2.addWidget(self.lstStep)
        self.lstVariant = QtWidgets.QListWidget(FcLoadTask)
        self.lstVariant.setObjectName("lstVariant")
        self.verticalLayout_2.addWidget(self.lstVariant)
        self.lstTask = QtWidgets.QListWidget(FcLoadTask)
        self.lstTask.setMaximumSize(QtCore.QSize(16777215, 150))
        self.lstTask.setStyleSheet("color: rgb(230, 230, 230);")
        self.lstTask.setFrameShape(QtWidgets.QFrame.Box)
        self.lstTask.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstTask.setObjectName("lstTask")
        self.verticalLayout_2.addWidget(self.lstTask)
        self.layMain.addLayout(self.verticalLayout_2)
        self.listWidget = QtWidgets.QListWidget(FcLoadTask)
        self.listWidget.setObjectName("listWidget")
        self.layMain.addWidget(self.listWidget)
        self.layMeta = QtWidgets.QVBoxLayout()
        self.layMeta.setObjectName("layMeta")
        self.layMain.addLayout(self.layMeta)
        self.layMain.setStretch(0, 6)
        self.layMain.setStretch(2, 1)

        self.retranslateUi(FcLoadTask)
        QtCore.QMetaObject.connectSlotsByName(FcLoadTask)
        FcLoadTask.setTabOrder(self.lstModule, self.lstClass)
        FcLoadTask.setTabOrder(self.lstClass, self.lstStep)
        FcLoadTask.setTabOrder(self.lstStep, self.lstTask)

    def retranslateUi(self, FcLoadTask):
        _translate = QtCore.QCoreApplication.translate
        FcLoadTask.setWindowTitle(_translate("FcLoadTask", "LoadTask"))
