# -*- coding: UTF-8 -*-
#.@FileName:fcUpVersion
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
from fcLib.appLib.ui import ui_fcUpVersion
from fcLib.tankLib.configLib import Tank

class FcUpVersion(QWidget, ui_fcUpVersion.Ui_FcUpVersion):

    def __init__(self, *args, **kwargs):
        super(FcUpVersion,self).__init__(*args, **kwargs)

        for entry in QtWidgets.QApplication.allWidgets():
            # print entry.objectName()
            try:
                if entry.objectName() == "FcUpVersion":
                    entry.close()
            except AttributeError:
                None
                None
                None
        self.setupUi(self)
        self.script_data = Tank().data_script
        self.setStyleSheet(self.script_data[TITLE]['style'])
        self.show()


        self.setup()



    def setup(self):
        # FILL COMBO BOX -------------------------------
        pass





def create():
    app = QtWidgets.QApplication(sys.argv)
    main_widget = FcUpVersion()
    sys.exit(app.exec_())


def start():
    global main_widget
    if os.environ['SOFTWARE'] =='maya':
        from fcLib.dccLib.maya_dcc import Maya
        judge = Maya().scene_judge()
        if judge:
            main_widget = FcUpVersion()
        else:
            pass
# create()
