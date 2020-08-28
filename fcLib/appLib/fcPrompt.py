# -*- coding: UTF-8 -*-
#.@FileName:fcLoadTask
#.@Date:2020-06-22:15:55
#.@Aurhor:LuoOu

import os
import sys

import datetime

# from Qt import QtWidgets, QtGui, QtCore, QtCompat

# from fcLib.fileLib import folder
# import arNotice
#
# from fcLib.tankLib import Tank
# from arUtil import ArUtil


#*********************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
# LOG   = Tank().log.init(script=TITLE)


#*********************************************************************
# CLASS
import Qt
print Qt.__binding__
from Qt.QtCore import *
from Qt.QtGui import *
from Qt.QtWidgets import *
from Qt import QtWidgets, QtCore, QtGui
from fcLib.appLib.ui import ui_fcPrompt
from fcLib.tankLib.configLib import Tank

class FcPrompt(QWidget, ui_fcPrompt.Ui_FcPrompt):

    def __init__(self, *args, **kwargs):
        super(FcPrompt,self).__init__(*args, **kwargs)

        for entry in QtWidgets.QApplication.allWidgets():
            # print entry.objectName()
            try:
                if entry.objectName() == "FcPrompt":
                    entry.close()
            except AttributeError:
                None
                None
                None
        self.setupUi(self)
        self.script_data = Tank().data_script
        self.setStyleSheet(self.script_data[TITLE]['style'])
        self.show()

        #
        # # parent = getMainWindow()
        # #
        # #
        # #
        # #
        # self.parent = None
        # self.setParent(self.parent)
        # #
        # self.setWindowFlags(Qt.Window)
        #
        # self.setupUi(self)

        # parent = getMainWindow()
        #
        #
        #
        #
        #
        # self.setParent(parent)
        #
        # self.setWindowFlags(Qt.Window)
        #
        # self.setupUi(self, BoilerDict['Environment'])

        # path_ui     = ("/").join([os.path.dirname(__file__), "ui", TITLE + ".ui"])
        # self.wgLoad = QtCompat.loadUi(path_ui)
        #
        # self.load_dir  = ''
        # self.load_file = ''
        #
        # self.software_format = {y:x.upper() for x, y in self.data['project']['EXTENSION'].items()}
        # self.software_keys   = list(self.software_format.keys())
        #
        # self.wgLoad.lstScene.itemSelectionChanged.connect(self.change_lstScene)
        # self.wgLoad.lstSet.itemSelectionChanged.connect(self.change_lstSet)
        # self.wgLoad.lstAsset.itemSelectionChanged.connect(self.change_lstAsset)
        # self.wgLoad.lstTask.itemSelectionChanged.connect(self.change_lstTask)
        # self.wgLoad.lstStatus.itemSelectionChanged.connect(self.change_lstStatus)
        # self.wgLoad.lstFiles.itemSelectionChanged.connect(self.change_lstFiles)
        #
        # self.wgHeader.btnOption.clicked.connect(self.press_menuItemAddFolder)
        # self.wgLoad.lstFiles.itemDoubleClicked.connect(self.press_btnAccept)
        #
        # self.wgLoad.lstScene.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.wgLoad.lstScene.customContextMenuRequested.connect(lambda: self.press_openMenu(self.wgLoad.lstScene))
        # self.wgLoad.lstSet.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.wgLoad.lstSet.customContextMenuRequested.connect(lambda: self.press_openMenu(self.wgLoad.lstSet))
        # self.wgLoad.lstAsset.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.wgLoad.lstAsset.customContextMenuRequested.connect(lambda: self.press_openMenu(self.wgLoad.lstAsset))
        # self.wgLoad.lstTask.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.wgLoad.lstTask.customContextMenuRequested.connect( lambda: self.press_openMenu(self.wgLoad.lstTask))
        # self.wgLoad.lstFiles.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.wgLoad.lstFiles.customContextMenuRequested.connect(lambda: self.press_openMenu(self.wgLoad.lstFiles))
        #
        # self.wgLoad.lstAsset.hide()
        # self.wgHeader.cbxAdd.hide()
        #
        # self.add_preview(self.wgLoad.layMeta)
        # self.wgHeader.layMain.addWidget(self.wgLoad, 0, 0)
        #
        # self.wgPreview.wgSnapshot.hide()
        # self.wgHeader.setWindowTitle(TITLE)
        # self.wgHeader.btnAccept.setText('Load')
        # self.wgHeader.btnOption.setText('Create')
        # self.wgHeader.setWindowIcon(QtGui.QIcon(Tank().get_img_path("btn/btn_load")))
        #
        # self.setup()
        # print main_widget
        #
        # self.resize_widget(self.wgLoad)
        # self.wgLoad.show()
        # LOG.info('START : ArLoad')
    @Slot()
    def on_btnClose_clicked(self):
        main_widget.close()

    def setup(self,title, text, prompt):
        self.setWindowTitle(title)
        self.labelText.setText(text)
        self.linPrint.setText(prompt)
        # FILL COMBO BOX -------------------------------





def create():
    app = QtWidgets.QApplication(sys.argv)
    main_widget = FcPrompt()
    sys.exit(app.exec_())


def start(title='',text='',prompt=''):
    global main_widget
    main_widget = FcPrompt()
    main_widget.setup(title, text, prompt)
# create()
