# -*- coding: UTF-8 -*-
#.@FileName:launch
#.@Date:2020-06-22:15:55
#.@Aurhor:LuoOu

import os
import sys

try:
    from PySide2 import QtWidgets, QtGui
except:
    pyside_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(pyside_path + "/site-packages/pyside")
    from PySide2 import QtWidgets, QtGui



from fcLib.fileLib import folder

from fcLib.tankLib.configLib import Tank
from fcLib.dccLib import dcclanch


#*********************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
# LOG   = Tank().log.init(script=TITLE)


#*********************************************************************
# CLASS
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, parent=None):
        envdict = os.environ
        QtWidgets.QSystemTrayIcon.__init__(self, parent)
        # self.activated.connect(self.showMainWidget)
        self.setIcon(QtGui.QIcon(envdict['IMG_PATH'] +'/software/default'))

        self.parent = parent

        # Tank().init_os()
        self.script_data = Tank().data_script
        # self.user = Tank().user
        self.project_data = Tank().data_project
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(self.script_data[TITLE]['style'])

        # ADMIN UI
        # if True: # self.user.is_admin:
        #     adminMenu = QtWidgets.QMenu('Admin')
        #     adminMenu.setStyleSheet(self.config['script'][TITLE]['style'])
        #     menu.addMenu(adminMenu)
        #
        #     menuItem = adminMenu.addAction(QtGui.QIcon(Tank().get_img_path('btn/btn_folder')), 'Open Project Data')
        #     menuItem.triggered.connect(self.press_btnOpenProjectLog)
        #     menuItem = adminMenu.addAction(QtGui.QIcon(Tank().get_img_path('btn/btn_folder')), 'Open User Data')
        #     menuItem.triggered.connect(self.press_btnOpenLocalLog)
        #
        #     menu.addSeparator()

        # menuItem = menu.addAction(QtGui.QIcon(Tank().get_img_path('user/' + self.user.id)), self.user.id)
        # menuItem.triggered.connect(self.press_btnShowUserData)

        menuItem = menu.addAction(QtGui.QIcon(envdict['IMG_PATH'] +'/btn/btn_folder'), "Server Root")
        menuItem.triggered.connect(self.press_btnOpenServerPath)

        menu.addSeparator()

        menuItem = menu.addAction(QtGui.QIcon(envdict['IMG_PATH'] + '/btn/btn_folder'), "Local Root")
        menuItem.triggered.connect(self.press_btnOpenLocalPath)

        menu.addSeparator()

        subMenu = QtWidgets.QMenu('Software')
        subMenu.setStyleSheet(self.script_data[TITLE]['style'])
        menu.addMenu(subMenu)

        for soft, soft_func in self.script_data[TITLE]['SOFTWARE'].items():
            menuItem = subMenu.addAction(QtGui.QIcon(envdict['IMG_PATH'] + '/software/' + soft), soft.title())
            menuItem.triggered.connect(eval(soft_func))

        menu.addSeparator()
        #
        menuItem = menu.addAction(QtGui.QIcon(envdict['IMG_PATH'] + '/btn/btn_folder'), 'Load')
        menuItem.triggered.connect(self.press_btnLoad)

        menu.addSeparator()

        menuItem = menu.addAction(QtGui.QIcon(envdict['IMG_PATH'] +'/btn/btn_setting'), 'Setting')
        menuItem.triggered.connect(self.press_btnLoad)

        menu.addSeparator()
        #
        # menuItem = menu.addAction(QtGui.QIcon(Tank().get_img_path('btn/btn_report')), 'Report')
        # menuItem.triggered.connect(self.press_btnReport)
        #
        # menuItem = menu.addAction(QtGui.QIcon(Tank().get_img_path('btn/btn_help')), 'Help')
        # menuItem.triggered.connect(self.press_btnHelp)
        #
        menu.addSeparator()

        menuItem = menu.addAction(QtGui.QIcon((os.environ['IMG_PATH']+ '/btn/btn_denial')), 'Quit')
        menuItem.triggered.connect(self.press_closeStartup)

        self.setContextMenu(menu)


    #**********************
    # PRESS_TRIGGER


    def press_btnOpenServerPath(self):
        folder.open_folder(self.project_data['FC_SERVER_ROOT'])

    def press_btnOpenLocalPath(self):
        folder.open_folder(self.project_data['FC_LOCAL_ROOT'])
    #------------------------------
    def press_btnLoad(self):
        pass
        # import arLoad
        # reload(arLoad)
        # self.arLoad = arLoad.ArLoad()
    #------------------------------
    def press_btnOpenMaya(self):
        dcclanch.start('maya')

    def press_btnOpenNuke(self):
        dcclanch.start('nuke')

    def press_btnOpenHoudini(self):
        dcclanch.start('houdini')

    def press_btnOpenRv(self):
        dcclanch.start('rv')


    def press_btnLoad(self):
        from fcLib.appLib import fcLoadTask
        reload(fcLoadTask)
        self.fcLoadTask = fcLoadTask.FcLoadTask()

    #------------------------------
    def press_closeStartup(self):
        self.parent.instance().quit()


def start():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    trayIcon = SystemTrayIcon(app)
    trayIcon.show()
    trayIcon.setToolTip('[right click]')
    trayIcon.showMessage("", '[right click]', QtWidgets.QSystemTrayIcon.Information , 20000)

    app.exec_()
