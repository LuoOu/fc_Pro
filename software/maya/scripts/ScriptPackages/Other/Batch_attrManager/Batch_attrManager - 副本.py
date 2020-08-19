#-*-coding:utf-8-*-
 
from maya import OpenMayaUI as omui
import maya.cmds as cmds
import maya.mel as mel
from PySide2.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
 
import Ui_Batch_attrManager #���ر����Py��.ui�ļ�
 
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)#���Maya������
 
class Form_Main(QMainWindow,Ui_Batch_attrManager.Ui_Form_Main):#�̳б���õ�.py��
    def __init__(self,*args, **kwargs):
        super(Form_Main, self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)#���´�������Ϊmaya���Ӽ�
        self.setWindowFlags(Qt.Window)
        self.setupUi(self)#���и����ʼ������
        # self.connectSignals()
 
    @Slot()
    def on_radioButton_FromScene_clicked(self):
        """
        Slot documentation goes here.
        """
        print  'ok'
    
    @Slot()
    def on_radioButton_FromProxy_clicked(self):
        """
        Slot documentation goes here.
        """
        print  ("FromProxy")
        
  
    @Slot()
    def on_radioButton_PreviewMesh_clicked(self):
        """
        Slot documentation goes here.
        """
        # xyl_rs_xfobjlist = cmds.ls(dag=1, type='RedshiftProxyMesh', sl=1)
        # xyl_rs_xf_onesp = ""
        # for xyl_rs_xf_onesp in xyl_rs_xfobjlist:
        #     print str(xyl_rs_xf_onesp) + "\n"
        #     cmds.setAttr((str(xyl_rs_xf_onesp) + ".displayMode"), 1)
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        cmds.PickWalkDown()
        ALLProxyMeshLIST = cmds.ls(sl=1)
        for esy in ALLProxyMeshLIST:
            cmds.setAttr((str(esy) + ".displayMode"), 1)
        print  ("PreviewMesh")
        cmds.select(ALLProxyMeshLIST)
        
    @Slot()
    def on_radioButton_BoundingBox_clicked(self):
        """
        Slot documentation goes here.
        """
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        ALLProxyMeshLIST = cmds.ls(sl=1)
        for esy in ALLProxyMeshLIST:
	        cmds.setAttr((str(esy) + ".displayMode"), 0)
        print  ("BoundingBox")
        cmds.select(ALLProxyMeshLIST)
 
def main():
    ui = Form_Main()
    ui.show()
    print 'run OK'
    return ui
if __name__ == '__main__':

    main()