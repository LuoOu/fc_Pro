# -*- coding: UTF-8 -*-
#.@FileName:ToolsPanel
#.@Date:2019-07-17:15:04
#.@Aurhor:LuoOu
import os
import sys


import Qt
print Qt.__binding__
from Qt.QtCore import *
from Qt.QtGui import *
from Qt.QtWidgets import *
from Qt import QtWidgets, QtCore, QtGui


# try:
#     from PySide2.QtCore import *
#     from PySide2.QtGui import *
#     from PySide2.QtWidgets import *
#
# except:
#     from PySide.QtCore import *
#     from PySide.QtGui import *
#     from PySide.QtWidgets import *




BoilerDict = {
    'Environment': 'Standalone',
    'MainWindow': None,
    'Stylesheet': 'mayaDark.stylesheet' }

try:
    from maya import OpenMayaUI as omui
    import maya.cmds as cmds
    BoilerDict['Environment'] = 'Maya'
    from shiboken2 import wrapInstance
except ImportError:
    None
    None
    None


try:
    import MaxPlus
    BoilerDict['Environment'] = '3dsMax'
except ImportError:
    None
    None
    None


try:
    import hou
    BoilerDict['Environment'] = 'Houdini'
except ImportError:
    None
    None
    None


try:
    import nuke
    BoilerDict['Environment'] = 'Nuke'
except ImportError:
    None
    None
    None



# try:
#     import MaxPlus
#
#     THREEDSMAX = True
# except ImportError:
#     THREEDSMAX = False

try:
    import hiero
    BoilerDict['Environment'] = 'Hiero'
except ImportError:
    None
    None
    None

try:
    import hiero
    BoilerDict['Environment'] = 'Hiero'
except ImportError:
    None
    None
    None

# try:
#     import Katana
#     BoilerDict['Environment'] = 'Katana'
# except ImportError:
#     None
#     None
#     None
# try:
#     import ix
#     BoilerDict['Environment'] = 'Clarisse'
#     BoilerDict['WindowTitle'] = 'Image Viewer Nuke v%s' % _version.__version__
# except ImportError:
#     None
#     None
#     None
from fcLib.appLib.ui import ui_fcToolsPanel

def getMainWindow():
    '''This function should be overriden'''
    if BoilerDict['Environment'] == 'Maya':
        win = omui.MQtUtil_mainWindow()
        ptr = wrapInstance(long(win), QtWidgets.QMainWindow)
        return ptr
    if BoilerDict['Environment'] == '3dsMax':

        try:
            mainWindow = MaxPlus.GetQMaxWindow()
        except AttributeError:
            None
            None
            None
            mainWindow = MaxPlus.GetQMaxMainWindow()

        return mainWindow
    if BoilerDict['Environment'] == 'Houdini':
        return hou.qt.mainWindow()

    if BoilerDict['Environment'] == 'Nuke':

        for obj in QtWidgets.QApplication.instance().topLevelWidgets():
            if (
                    obj.inherits("QMainWindow")
                    and obj.metaObject().className() == "Foundry::UI::DockMainWindow"
            ):
                return obj
        else:
            raise RuntimeError("Could not find DockMainWindow instance")
            return None

    if BoilerDict['Environment'] == 'Hiero':
        return hiero.ui.mainWindow()

    # if BoilerDict['Environment'] == 'Katana':
    #     return Katana.Qt.QMainWindow()



class Form_Main(QMainWindow, ui_fcToolsPanel.Ui_ToolsPanel_Win):
    def __init__(self, *args, **kwargs):
        super(Form_Main, self).__init__(*args, **kwargs)
        for entry in QtWidgets.QApplication.allWidgets():

            try:
                if entry.objectName() == "FC_ToolsPanel_Win":
                    entry.close()
            except AttributeError:
                None
                None
                None


        parent = getMainWindow()


        # if DDC == "maya":
        #     from maya import OpenMayaUI as omui
        #
        #     from shiboken2 import wrapInstance
        #     mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        #     mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)
        #     self.setParent(mayaMainWindow)
        #
        #
        # elif DDC  == "nuke":
        # self.setParent(parent)
        #
        # elif DDC == "houdini":
        #     import hou
        #
        #     self.setParent(hou.qt.mainWindow(), Qt.Window)


        self.setParent(parent)

        self.setWindowFlags(Qt.Window)

        self.setupUi(self, BoilerDict['Environment'])


    # def showRigControlWindow(self):
    #     if self._rcwin is None:
    #         self._rcwin = RigControlWindow()
    #     self._rcwin.show()





    @Slot()
    def Check_Head_UI(self,_dict):
        """
        UI "Asset_Check_Head_LAY"
        """
        pass


    @Slot()
    def Check_tools_tabA_UI(self, _dict):
        """
        UI "Asset_Check_tools_tabA_LAY"
        """
        pass









def main():

    #
    # try:
    #     import MaxPlus
    #
    #     DDC = "maya"
    # except ImportError:
    #     pass
    #
    # try:
    #     import bpy
    #
    #     DDC = "maya"
    # except ImportError:
    #     pass
    #
    # try:
    #     import unreal  # noqa
    #
    #     DDC = "maya"
    # except ImportError:
    #     pass
    # print sys.argv
    # app = QApplication(sys.argv)
    # serverName = 'myuniqueservername'
    # socket = QLocalSocket()
    # socket.connectToServer(serverName)
    # if socket.waitForConnected(500):
    #     return (app.quit())
    #
    # localServer = QLocalServer()
    # localServer.listen(serverName)
    # try:
    #     ui = Form_Main()
    #     ui.show()
    #     sys.exit(app.exec_())
    # finally:
    #     localServer.close()

    ui = Form_Main()
    ui.show()
    # sys.exit(app.exec_())

    return ui

if __name__ == '__main__':
    main()
# try:
#     import hou
#     main()
# except:
#     print "No H"
