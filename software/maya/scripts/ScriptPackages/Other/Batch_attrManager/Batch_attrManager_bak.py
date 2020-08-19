# -*- coding: utf-8 -*-

"""
Module implementing Form_Main.
"""
import sys
from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_Batch_attrManager
from shiboken2 import wrapInstance 


mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QMainWindow) 


class Form_Main(QMainWindow, Ui_Batch_attrManager.Ui_Form_Main):
   
    def __init__(self, *args, **kwargs):

        super(Form_Main, self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)#将新窗口设置为maya的子级
        self.setWindowFlags(Qt.Window)
        self.setupUi(self)#运行父类初始化方法
        self.connectSignals()

    
    

    
    @pyqtSlot()
    def on_radioButton_FromScene_clicked(self):
        """
        Slot documentation goes here.
        """
        pass
    
    @pyqtSlot()
    def on_radioButton_FromProxy_clicked(self):
        """
        Slot documentation goes here.
        """
        pass
        
  
    @pyqtSlot(bool)
    def on_radioButton_PreviewMesh_clicked(self):
        """
        Slot documentation goes here.
        """
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        # cmds.PickWalkDown()
        xuanzedestandin = cmds.ls(sl=1)
        for esy in xuanzedestandin:
	        cmds.setAttr((str(esy) + ".displayMode"), 1)
	        # cmds.select(cl=1)
        print  ("PreviewMesh")
        cmds.select(xuanzedestandin)
        
    @pyqtSlot(bool)
    def on_radioButton_BoundingBox_clicked(self):
        """
        Slot documentation goes here.
        """
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        # cmds.PickWalkDown()
        xuanzedestandin = cmds.ls(sl=1)
        for esy in xuanzedestandin:
	        cmds.setAttr((str(esy) + ".displayMode"), 0)
	        # cmds.select(cl=1)
        print  ("BoundingBox")
        print xuanzedestandin
        cmds.select(xuanzedestandin)
    

        
def main():
    ui = MainWindow()
    ui.show()
    print 'run MyFirstQtNext'
    return ui
if __name__ == '__main__':
 
    main()
    # name = "customUI"
    # try: 
    #     cmds.deleteUI(name)#如果UI存在将会被删除
    # except:
    #     pass
    # cmds.workspaceControl(name,tabToControl=["AttributeEditor", -1],initialWidth=100,widthProperty="preferred", minimumWidth=True,label="coustomUI", uiScript="customUI()")
 
    
