from PySide2 import QtCore, QtGui, QtWidgets
 
class Ui_MyFirstQt(object):
    def setupUi(self, MyFirstQt):
        MyFirstQt.setObjectName("MyFirstQt")
        MyFirstQt.resize(200, 200)
        self.printText = QtWidgets.QLineEdit(MyFirstQt)
        self.printText.setGeometry(QtCore.QRect(30, 20, 141, 20))
        self.printText.setObjectName("printText")
        self.btnPrint = QtWidgets.QPushButton(MyFirstQt)
        self.btnPrint.setGeometry(QtCore.QRect(60, 80, 75, 23))
        self.btnPrint.setObjectName("btnPrint")
 
        self.retranslateUi(MyFirstQt)
        QtCore.QMetaObject.connectSlotsByName(MyFirstQt)
 
    def retranslateUi(self, MyFirstQt):
        _translate = QtCore.QCoreApplication.translate
        MyFirstQt.setWindowTitle(_translate("MyFirstQt", "Form"))
        self.btnPrint.setText(_translate("MyFirstQt", "Print"))
