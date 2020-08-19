# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\Python\Projects\FCmayabatch\FCmayabatch.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FCmbMainWindow(object):
    def setupUi(self, FCmbMainWindow):
        FCmbMainWindow.setObjectName("FCmbMainWindow")
        FCmbMainWindow.resize(400, 600)
        FCmbMainWindow.setMaximumSize(QtCore.QSize(400, 600))
        self.centralWidget = QtWidgets.QWidget(FCmbMainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.allWidget = QtWidgets.QWidget(self.centralWidget)
        self.allWidget.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.allWidget.setMinimumSize(QtCore.QSize(400, 600))
        self.allWidget.setObjectName("allWidget")
        self.allLayout = QtWidgets.QVBoxLayout(self.allWidget)
        self.allLayout.setContentsMargins(0, 0, 0, 0)
        self.allLayout.setObjectName("allLayout")

        self.aWidget = QtWidgets.QWidget(self.allWidget)
        self.aWidget.setMaximumSize(QtCore.QSize(400, 50))
        self.aWidget.setObjectName("aWidget")
        self.aLayout = QtWidgets.QHBoxLayout(self.aWidget)
        self.aLayout.setObjectName("aLayout")
        self.outlabel = QtWidgets.QLabel(self.aWidget)
        self.outlabel.setObjectName("outlabel")
        self.aLayout.addWidget(self.outlabel)
        self.pathlineEdit = QtWidgets.QLineEdit(self.aWidget)
        self.pathlineEdit.setObjectName("pathlineEdit")
        self.pathlineEdit.setDragEnabled(True)
        self.aLayout.addWidget(self.pathlineEdit)
        self.lookpushButton = QtWidgets.QPushButton(self.aWidget)
        self.lookpushButton.setObjectName("lookpushButton")
        self.aLayout.addWidget(self.lookpushButton)
        self.allLayout.addWidget(self.aWidget)
        self.bWidget = QtWidgets.QWidget(self.allWidget)
        self.bWidget.setMaximumSize(QtCore.QSize(400, 40))
        self.bWidget.setObjectName("bWidget")
        self.bLayout = QtWidgets.QHBoxLayout(self.bWidget)
        self.bLayout.setObjectName("bLayout")
        self.filelabel = QtWidgets.QLabel(self.bWidget)
        self.filelabel.setObjectName("filelabel")
        self.bLayout.addWidget(self.filelabel)
        self.cleanpushButton = QtWidgets.QPushButton(self.bWidget)
        self.cleanpushButton.setObjectName("cleanpushButton")
        self.bLayout.addWidget(self.cleanpushButton)
        self.allLayout.addWidget(self.bWidget)
        self.cWidget = QtWidgets.QWidget(self.allWidget)
        self.cWidget.setMaximumSize(QtCore.QSize(400, 450))
        self.cWidget.setObjectName("cWidget")
        self.cLayout = QtWidgets.QVBoxLayout(self.cWidget)
        self.cLayout.setObjectName("cLayout")
        self.malistWidget = MyListWidget(self.cWidget)
        self.malistWidget.setMaximumSize(QtCore.QSize(400, 450))
        self.malistWidget.setObjectName("malistWidget")
        self.malistWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.malistWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # self.malistWidget.setAcceptDrops(True)
        # self.malistWidget.setDragEnabled(True)

        self.cLayout.addWidget(self.malistWidget)
        self.allLayout.addWidget(self.cWidget)
        self.dWidget = QtWidgets.QWidget(self.allWidget)
        self.dWidget.setMaximumSize(QtCore.QSize(400, 150))
        self.dWidget.setObjectName("dWidget")
        self.dLayout = QtWidgets.QVBoxLayout(self.dWidget)
        self.dLayout.setObjectName("dLayout")

        self.comboBox = QtWidgets.QComboBox(self.dWidget)
        self.comboBox.setObjectName("comboBox")

        self.dLayout.addWidget(self.comboBox)

        self.staBrowser = QtWidgets.QTextBrowser(self.dWidget)
        self.staBrowser.setMaximumSize(QtCore.QSize(400, 100))
        self.staBrowser.setObjectName("staBrowser")
        self.dLayout.addWidget(self.staBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.dWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.dLayout.addWidget(self.progressBar)
        self.extpushButton = QtWidgets.QPushButton(self.dWidget)
        self.extpushButton.setObjectName("extpushButton")
        self.dLayout.addWidget(self.extpushButton)
        self.allLayout.addWidget(self.dWidget)
        FCmbMainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(FCmbMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FCmbMainWindow)

    def retranslateUi(self, FCmbMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FCmbMainWindow.setWindowTitle(_translate("FCmbMainWindow", "FCmaya后台批量处理工具"))
        self.outlabel.setText(_translate("FCmbMainWindow", "输出路径"))
        self.lookpushButton.setText(_translate("FCmbMainWindow", "浏览"))
        self.filelabel.setText(_translate("FCmbMainWindow", "将需要处理的文件拖入"))
        self.cleanpushButton.setText(_translate("FCmbMainWindow", "清除"))
        self.extpushButton.setText(_translate("FCmbMainWindow", "开始"))
        actionlist = self.addpy()
        for a in actionlist:
            self.comboBox.addItem(a)

    def addline(self,data):
        self.malistWidget.addItem(data)

    def addpy(self):
        """
        查询当前文件路径

        """
        script = os.path.realpath(__file__)
        scripts_dir = os.path.dirname(script)
        path = scripts_dir + "/action"
        list = os.listdir(path)
        actionlist = []
        for a in list:
            if a.split(".")[1] == "py":
                actionlist.append(a)
        return actionlist





class MyListWidget(QtWidgets.QListWidget):
    def __init__(self, parent):
        super(MyListWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

    # def addItem(self, *args, **kwargs):
    #     pass

    def dragEnterEvent(self, e):

        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        file = e.mimeData().text()
        path = file.replace("file:///","")
        fileList = []
        if not self.count() == 0:
            for i in list(range(1,self.count()+1)):
                fileList.append(self.item(i-1).text())

        if path.split(".")[1] == "ma" and path not in fileList:
            self.addItem(path)
        # ui = Ui_FCmbMainWindow()
        # ui.addline(e.mimeData().text())
        # self.setText(e.mimeData().text())



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     FCmbMainWindow = QtWidgets.QMainWindow()
#     ui = Ui_FCmbMainWindow()
#     ui.setupUi(FCmbMainWindow)
#     FCmbMainWindow.show()
#     sys.exit(app.exec_())

