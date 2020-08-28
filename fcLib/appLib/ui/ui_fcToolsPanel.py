# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FC_ToolsPanel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!=[]
import os
import sys
import json
import codecs
import importlib

import Qt
print Qt.__binding__
from Qt import QtCore, QtGui, QtWidgets

from fcLib.tankLib.configLib import Tank



class Ui_ToolsPanel_Win(object):
    def setupUi(self, FC_ToolsPanel_Win,DDC):

        setDict = Tank().data_software['SCRIPTS']

        FC_ToolsPanel_Win.setObjectName("FC_ToolsPanel_Win")
        FC_ToolsPanel_Win.setWindowModality(QtCore.Qt.NonModal)
        FC_ToolsPanel_Win.setEnabled(True)
        FC_ToolsPanel_Win.resize(250, 300)
        FC_ToolsPanel_Win.setWindowTitle("ToolsPanel")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FC_ToolsPanel_Win.sizePolicy().hasHeightForWidth())
        FC_ToolsPanel_Win.setSizePolicy(sizePolicy)
        FC_ToolsPanel_Win.setMinimumSize(QtCore.QSize(250, 300))
        FC_ToolsPanel_Win.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        FC_ToolsPanel_Win.setAnimated(True)
        self.ToolsPanelMainwidget = QtWidgets.QWidget(FC_ToolsPanel_Win)
        self.ToolsPanelMainwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolsPanelMainwidget.sizePolicy().hasHeightForWidth())
        self.ToolsPanelMainwidget.setSizePolicy(sizePolicy)
        self.ToolsPanelMainwidget.setObjectName("ToolsPanelMainwidget")
        self.ToolsPanelLayout = QtWidgets.QVBoxLayout(self.ToolsPanelMainwidget)
        self.ToolsPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.ToolsPanelLayout.setSpacing(0)
        self.ToolsPanelLayout.setObjectName("ToolsPanelLayout")
        self.ToolsPaneltabWidget = QtWidgets.QTabWidget(self.ToolsPanelMainwidget)
        self.ToolsPaneltabWidget.setObjectName("ToolsPaneltabWidget")
        self.tabList = []
        self.scrList =[]
        self.scrAWCList = []
        self.pushButton = []
        print setDict
        for i in range(len(setDict)):
            process = setDict.keys()[i]

            self.tabList.append("tab_"+process)
            self.scrList.append("scr_" + process)
            self.scrAWCList.append("scrAWC_" + process)
        for i in range(len(setDict)):
            process = setDict.keys()[i]
            plugList = setDict.values()[i]
            self.tabList[i] = QtWidgets.QWidget()
            self.tabList[i].setObjectName("tab_"+process)
            self.ToolsPaneltabWidget.setTabText(i,process)
            self.scrList[i] = QtWidgets.QScrollArea(self.tabList[i])
            self.scrList[i].setGeometry(QtCore.QRect(0, 0, 250, 278))
            self.scrList[i].setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.scrList[i].setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scrList[i].setWidgetResizable(True)
            self.scrList[i].setObjectName("scr_" + process)
            self.scrAWCList[i] = QtWidgets.QWidget()
            self.scrAWCList[i].setGeometry(QtCore.QRect(0, -94, 230, 10+35*len(plugList)))
            self.scrAWCList[i].setMinimumSize(QtCore.QSize(0, 10+35*len(plugList)))
            self.scrAWCList[i].setObjectName("scrAWC_" + process)

            self.pushButton = []
            for p in range(len(plugList)):
                plug = plugList[p]
                self.pushButton.append("tab_" + process + plug.keys()[0])

            for p in range(len(plugList)):
                plug = plugList[p]

                self.pushButton[p] = QtWidgets.QPushButton(self.scrAWCList[i])
                self.pushButton[p].setGeometry(QtCore.QRect(5, 5+35*p, 225, 30))
                self.pushButton[p].setObjectName("pushButton_"+plug.keys()[0])
                self.pushButton[p].setText(plug.values()[0])
                dict_template = {}
                dict_template["DDC"] =DDC
                dict_template["process"] = process
                dict_template["plug"] = plug.keys()[0]
                self.pushButton[p].clicked.connect(lambda dict_template = dict_template: self.pushButton_clicked(dict_template))

            self.scrList[i].setWidget(self.scrAWCList[i])
            self.ToolsPaneltabWidget.addTab(self.tabList[i], process)

        self.ToolsPanelLayout.addWidget(self.ToolsPaneltabWidget)
        FC_ToolsPanel_Win.setCentralWidget(self.ToolsPanelMainwidget)

        self.retranslateUi(FC_ToolsPanel_Win,setDict)
        self.ToolsPaneltabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FC_ToolsPanel_Win)

    def retranslateUi(self, FC_ToolsPanel_Win,setDict):
        _translate = QtCore.QCoreApplication.translate
        FC_ToolsPanel_Win.setWindowTitle(_translate("FC_ToolsPanel_Win", "ToolsPanel"))
        # self.pushButton.setText(_translate("FC_ToolsPanel_Win", "PushButton"))
        for i in range(len(setDict)):
            process = setDict.keys()[i]
            # self.ToolsPaneltabWidget.setTabText(self.ToolsPaneltabWidget.indexOf(i), _translate("FC_ToolsPanel_Win", process))


    def pushButton_clicked(self,dict):
        script = os.environ['SOFTWARE_PATH']

        script = r'{}/{}'.format(script, 'scripts')
        scriptsPath = script.replace('\\', r'/')
        envPaths = [r'{}/{}'.format(scriptsPath, dict["process"])]
        envPaths.append(scriptsPath + r'/ScriptPackages')

        for path in envPaths:
            if path in sys.path:
                print 'The Python Env Path Already there'
            else:
                sys.path.append(path)

        if dict['DDC'] == "Maya":
            for path in envPaths:
                if path in os.environ['MAYA_SCRIPT_PATH']:
                    print 'The MEL Env Path Already there'
                else:
                    os.environ['MAYA_SCRIPT_PATH'] = '{};{}'.format(path, os.getenv('MAYA_SCRIPT_PATH'))

        module = importlib.import_module(dict["plug"])

        module.main()
        # link = eval('{}()'.format(dict["plug"]))
        # link.main()

    # def getToolsPanelSet(self,DDC):
    #
    #     scripts = os.environ['PIPELINE_PATH'] +'/'
    #     scripts_dir = os.path.dirname(scripts)
    #     setPath = scripts_dir.replace("ui", "config/"+DDC+"_set.json").replace('\\', r'/')
    #
    #     _dict = {}
    #     with codecs.open(setPath, 'r') as file:
    #         datas = json.load(file)
    #
    #     if cmp(datas, _dict) == 0:
    #         pass
    #     else:
    #         _dict.update(datas)
    #
    #
    #     return _dict["set"]
        # setPath = scripts_dir.replace("ANI", "ScriptPackages").replace('\\', r'/')



