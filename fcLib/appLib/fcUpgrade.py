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
import Qt
print Qt.__binding__
from Qt.QtCore import *
from Qt.QtGui import *
from Qt.QtWidgets import *
from Qt import QtWidgets, QtCore, QtGui
from fcLib.appLib.ui import ui_fcUpgrade
from fcLib.tankLib.configLib import Tank

class FcUpgrade(QWidget, ui_fcUpgrade.Ui_FcUpgrade):

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
        self.setup()


    @Slot()
    def on_btnUpgrade_clicked(self):
        self.listWidget.clear()
        self.listWidget.show()
        self.progressBar.show()
        self.progressBar.reset()
        self.labtext.hide()
        self.lineUpgradePath.hide()

        self.listWidget.addItem('start the update.....')

        self.listWidget.addItem('Check to see if the update package exists......')
        UpgradePath = self.lineUpgradePath.text()
        if os.path.exists(UpgradePath):
            pass
        else:
            self.listWidget.addItem('The update pack does not exist:'+UpgradePath)




    def setup(self):
        self.listWidget.hide()
        self.progressBar.hide()
        from fcLib.tankLib.configLib import Tank
        tmp_path = Tank().data_pipeline['UPGRADE_PACKAGE']
        self.lineUpgradePath.setText(tmp_path)





def create():
    app = QtWidgets.QApplication(sys.argv)
    main_widget = FcUpgrade()
    sys.exit(app.exec_())


def start():
    global main_widget
    main_widget = FcUpgrade()
# create()
