# -*- coding: utf-8 -*-

"""
Module implementing FCmbMainWindow.
"""
import os
import sys
# from PySide2.QtCore import pyqtSlot

from PySide2 import QtWidgets,QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from maya import OpenMayaUI as omui
import subprocess
from shiboken2 import wrapInstance
from Ui_FCmayabatch import Ui_FCmbMainWindow
# sys.path.append(r"C:\Program Files\Autodesk\Maya2017\Python")
# sys.path.append(r"D:\Program Files\Autodesk\Maya2017\Python\Lib\site-packages")

maya_location = os.path.normpath('C:/Program Files/Autodesk/Maya2017')
python_maya_location = os.path.normpath("C:/Program Files/Autodesk/Maya2017/Python")
maya_bin_location = os.path.normpath('C:/Program Files/Autodesk/Maya2017/bin')



os.environ['MAYA_LOCATION'] = maya_location  # add maya location as a environment variable
os.environ["PYTHONHOME"] = python_maya_location
os.environ["PATH"] = maya_bin_location + ';' + os.environ["PATH"]

# import maya.standalone as sta
# import maya.cmds as cmds
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)


class FCmbMainWindow(QMainWindow, Ui_FCmbMainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self,*args, **kwargs):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        # super(FCmbMainWindow, self).__init__(*args, **kwargs)
        # self.setParent(mayaMainWindow)  # ���´�������Ϊmaya���Ӽ�
        # self.setWindowFlags(Qt.Window)
        # self.setupUi(self)  # ���и����ʼ������
        # self.connectSignals()


        super(FCmbMainWindow, self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Window)
        self.setupUi(self)

    @Slot()
    def on_lookpushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.openFile()

    @Slot()
    def on_cleanpushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # item = self.malistWidget.currentItem()
        # print item
        self.malistWidget.takeItem(self.malistWidget.currentRow())

    def openFile(self):
        filename=QtWidgets.QFileDialog.getExistingDirectory(self,"choose directory",r"C:")
        self.pathlineEdit.setText(str(filename))

    # @Slot()
    # def on_malistWidget_customContextMenuRequested(self):
    #     popMenu = QtWidgets.QMenu()
    #     popMenu.addAction(QtWidgets.QAction('删除',self))

    @Slot()
    def on_extpushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.progressBar.setValue(0)
        py = self.file_path()
        outpath = self.pathlineEdit.text()
        fileList = []
        if not self.malistWidget.count() ==0:
            for i in list(range(1, self.malistWidget.count() + 1)):
                fileList.append(self.malistWidget.item(i - 1).text())

            self.progressBar.setMaximum(len(fileList))
            self.staBrowser.setText(u'获取'+str(len(fileList))+u'个文件')

            for f in fileList:
                cmd = 'mayapy "{}" "{}" "{}"'.format(py, f, outpath)
                os.chdir("C:/Program Files/Autodesk/Maya2017/bin")
                print cmd
                pro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = pro.communicate()
                print out
                print err
            # import exportABC


                self.staBrowser.setText(u'正在输出 ' + f)

                # # exportABC.expabc(f,outpath)
                self.progressBar.setValue(fileList.index(f)+1)
            self.staBrowser.setText(f+u'完成')
            self.staBrowser.setText(u'输出完成')


    def file_path(self):
        """
        查询当前文件路径

        """
        action = self.comboBox.currentText()
        script = os.path.realpath(__file__)
        scripts_dir = os.path.dirname(script)
        path = scripts_dir + '/action/{}'.format(action)
        return path


def main():
    import sys

    # app = QtWidgets.QApplication(sys.argv)
    ui = FCmbMainWindow()

    ui.show()
    # sys.exit(app.exec_())
    return ui
if __name__ == '__main__':

    main()

