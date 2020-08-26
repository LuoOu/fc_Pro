# -*- coding: UTF-8 -*-
#.@FileName:fcUpgrade
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
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtCore, QtGui
from fcLib.appLib.ui import ui_fcPrompt
from fcLib.tankLib.configLib import Tank

class FcUpgrade(QWidget, ui_fcPrompt.Ui_FcPrompt):

    def __init__(self, *args, **kwargs):
        super(FcUpgrade,self).__init__(*args, **kwargs)

        for entry in QtWidgets.QApplication.allWidgets():
            # print entry.objectName()
            try:
                if entry.objectName() == "FcUpgrade":
                    entry.close()
            except AttributeError:
                None
                None
                None
        self.setupUi(self)
        self.script_data = Tank().data_script
        self.setStyleSheet(self.script_data[TITLE]['style'])
        self.show()


    @Slot()
    def on_btnUpgrade_clicked(self):
        main_widget.close()

    # def setup(self,title, text, prompt):
    #     self.setWindowTitle(title)
    #     self.labelText.setText(text)
    #     self.linPrint.setText(prompt)
        # FILL COMBO BOX -------------------------------





def create():
    app = QtWidgets.QApplication(sys.argv)
    main_widget = FcUpgrade()
    sys.exit(app.exec_())


def start():
    global main_widget
    main_widget = FcUpgrade()
# create()
