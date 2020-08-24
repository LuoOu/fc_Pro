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

import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtCore, QtGui
from fcLib.tankLib.configLib import Tank
from fcLib.fileLib import folder
from fcLib.appLib.ui import ui_fcLoadTask
from fcLib.dccLib import dcclanch


def getMainWindow():
    '''This function should be overriden'''
    if os.environ['software'] == 'maya':
        import maya.OpenMayaUI as omui
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


class FcLoadTask(QWidget, ui_fcLoadTask.Ui_FcLoadTask):

    def __init__(self, *args, **kwargs):
        super(FcLoadTask,self).__init__(*args, **kwargs)

        for entry in QtWidgets.QApplication.allWidgets():
            # print entry.objectName()
            try:
                if entry.objectName() == "FcLoadTask":
                    entry.close()
            except AttributeError:
                None
                None
                None
        try:
            if os.environ['software'] == 'maya':
                import maya.OpenMayaUI as omui
                import shiboken2
                win = omui.MQtUtil.mainWindow()
                ptr = shiboken2.wrapInstance(long(win), QtWidgets.QMainWindow)
                self.setParent(ptr)
                self.setWindowFlags(Qt.Window)
        except:
            pass


        self.setupUi(self)


        self.script_data = Tank().data_script
        self.setStyleSheet(self.script_data[TITLE]['style'])
        self.show()

        #
        # parent = getMainWindow()
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
        try:
            pass
        except:
            pass

        self.setup()
        #
        # self.resize_widget(self.wgLoad)
        # self.wgLoad.show()
        # LOG.info('START : ArLoad')


    def setup(self):
        # FILL COMBO BOX -------------------------------
        self.lstModule.clear()
        self.lstClass.clear()
        self.lstEntity.clear()
        self.lstStep.clear()
        self.clear_meta()
        self.change_lstModule()

        # self.change_lstClass()
        # self.wgPreview.edtComment.setReadOnly(True)
        #
        # self.clear_meta()

        # for keys, items in self.data['project']['SCENES'].items():
        #     self.wgLoad.lstScene.addItem(keys)
        #
        # self.wgLoad.lstScene.setCurrentRow(0)


    #*********************************************************************
    # PRESS
    def press_btnAccept(self):
        if not os.path.exists(self.load_file):
            self.set_status('FAILED LOADING : Path doesnt exists: {}'.format(self.load_file), msg_type=3)
            return False

        open_software = self.software_format[os.path.splitext(self.load_file)[1][1:]].lower()

        # OPEN in current software
        try:
            if open_software == Tank().software.software:
                LOG.info(self.load_file)
                Tank().software.scene_open(self.load_file)
                self.wgHeader.close()
            else:
                try:    Tank().start_software(open_software, self.load_file)
                except: LOG.error('FAILED to open software', exc_info=True)
            # else: subprocess.Popen(self.load_file, shell=True)
        except: LOG.warning("No Software setup")

        note = arNotice.Notice(title = os.path.basename(self.load_file).split('.')[0],
                               msg   = self.wgPreview.edtComment.toPlainText(),
                               user  = self.wgPreview.lblUser.text(),
                               img   = self.preview_img_path if os.path.exists(self.preview_img_path) else 'lbl/lbl{}131'.format(Tank().software.software.lower().title()),
                               img_link = os.path.dirname(self.load_file))
        arNotice.ArNotice(note)


    def press_openMenu(self, list_widget):
        self.listMenu = QtGui.QMenu()
        self.listMenu.setStyleSheet(self.data['script'][TITLE]['style'])
        menu_item = self.listMenu.addAction("Add " + self.wgLoad.lstScene.currentItem().text())
        self.wgLoad.triggered.connect(self.press_menuItemAddFolder)
        menu_item = self.listMenu.addSeparator()
        menu_item = self.listMenu.addAction("ABC")
        self.wgLoad.triggered.connect(lambda: self.press_menuSort(list_widget))
        menu_item = self.listMenu.addAction("CBA")
        self.wgLoad.triggered.connect(lambda: self.press_menuSort(list_widget, True))

        parentPosition = self.wgLoad.lstTask.mapToGlobal(QtCore.QPoint(0, 0))
        self.listMenu.move(QtGui.QCursor().pos())
        self.listMenu.show()

    def press_menuItemAddFolder(self):
        import arSaveAs
        self.save_as = arSaveAs.start(new_file=False)

    def press_menuSort(self, list_widget, reverse=False):
        file_list = []
        for index in xrange(list_widget.count()):
             file_list.append(list_widget.item(index).text())
        list_widget.clear()
        list_widget.addItems(sorted(file_list, reverse=reverse))


    #*********************************************************************
    # CHANGE
    def change_lstModule(self):
        tmp_content = Tank().get_data('project')['MODULE']

        # self.scene_steps = len(self.data['project']['SCENES'][self.wgLoad.lstScene.currentItem().text()].split('/'))
        # if self.scene_steps < 5: self.wgLoad.lstAsset.hide()
        # else:
        #     self.wgLoad.lstAsset.itemSelectionChanged.connect(self.change_lstAsset)
        #     self.wgLoad.lstAsset.show()
        #
        self.lstModule.clear()
        if tmp_content:
            self.lstModule.addItems(sorted(tmp_content))
            self.lstModule.setCurrentRow(0)

    @Slot()
    def on_lstModule_itemSelectionChanged(self):
        self.change_lstClass()


    def change_lstClass(self):
        new_path    = os.environ['FC_LOCAL_ROOT'] + '/' + self.lstModule.currentItem().text()

        tmp_content = folder.get_file_list(new_path)


        self.lstClass.clear()
        if tmp_content:
            self.lstClass.addItems(sorted(tmp_content))
            self.lstClass.setCurrentRow(0)

    @Slot()
    def on_lstClass_itemSelectionChanged(self):
        self.change_lstEntity()

    def change_lstEntity(self):
        new_path    = os.environ['FC_LOCAL_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text()
        tmp_content = folder.get_file_list(new_path)

        self.lstEntity.clear()
        if tmp_content:
            self.lstEntity.addItems(sorted(tmp_content))
            self.lstEntity.setCurrentRow(0)

    @Slot()
    def on_lstEntity_itemSelectionChanged(self):
        self.change_lstStep()

    def change_lstStep(self):
        new_path    = os.environ['FC_LOCAL_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text() + '/' + self.lstEntity.currentItem().text()
        tmp_content = folder.get_file_list(new_path)

        newtmp_content = []
        if self.lstModule.currentItem().text() == 'Asset':
            for i in tmp_content:
                if i in Tank().get_data('project')['STEP'][self.lstModule.currentItem().text()]:
                    newtmp_content.append(i)
        else:
            newtmp_content = tmp_content


        self.lstStep.clear()
        if newtmp_content:
            self.lstStep.addItems(sorted(newtmp_content))
            self.lstStep.setCurrentRow(0)

    @Slot()
    def on_lstStep_itemSelectionChanged(self):
        self.fill_meta()
        self.change_combVariant()


    def change_combVariant(self):
        new_path = os.environ[
                       'FC_LOCAL_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text() + '/' + self.lstEntity.currentItem().text() + '/' + self.lstStep.currentItem().text()
        tmp_content = folder.get_file_list(new_path)


        self.combVariant.clear()
        if tmp_content:
            self.combVariant.addItems(sorted(tmp_content))
            self.combVariant.setCurrentIndex(0)

    @Slot()
    def on_combVariant_currentIndexChanged(self):
        self.change_combversion()


    def change_combversion(self):
        new_path = os.environ[
                       'FC_LOCAL_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text() + '/' + self.lstEntity.currentItem().text() + '/' + self.lstStep.currentItem().text() + '/' + self.combVariant.currentText()+"/work"
        if self.lstModule.currentItem().text() == 'Asset':
            file_type=self.lstEntity.currentItem().text()+'_'+ self.lstStep.currentItem().text()+'_' + self.combVariant.currentText()+'_v[0-9][0-9][0-9].ma'
            tmp_content = folder.get_file_list(new_path, file_type=file_type, extension=True)
        newtmp_content = folder.cut_filesplit_list(tmp_content,"_",4,True)

        self.combversion.clear()
        if newtmp_content:
            self.combversion.addItems(sorted(newtmp_content))
            self.combversion.setCurrentIndex(0)

    @Slot()
    def on_combversion_currentIndexChanged(self):
        self.change_labelPreview()

    def change_labelPreview(self):
        new_path = os.environ[
                       'FC_LOCAL_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text() + '/' + self.lstEntity.currentItem().text() + '/' + self.lstStep.currentItem().text() + '/' + self.combVariant.currentText()+"/work"

        if self.lstModule.currentItem().text() == 'Asset':
            new_img =self.lstEntity.currentItem().text() + '_' + self.lstStep.currentItem().text() + '_' + self.combVariant.currentText()+ '_' + self.combversion.currentText() + '.png'
            if os.path.exists(new_path+'/'+new_img):
                self.labelPreview.setPixmap(QtGui.QPixmap(QtGui.QImage(new_path+'/'+new_img)).scaled(200, 200))
            else:
                self.labelPreview.setPixmap(
                    QtGui.QPixmap(QtGui.QImage(Tank().get_img_path('btn/thumbnail'))).scaled(200, 200))

    @Slot()
    def on_btnLoad_clicked(self):
        new_path = os.environ[
                       'FC_LOCAL_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text() + '/' + self.lstEntity.currentItem().text() + '/' + self.lstStep.currentItem().text() + '/' + self.combVariant.currentText() + "/work"

        if self.lstModule.currentItem().text() == 'Asset':
            new_file = self.lstEntity.currentItem().text() + '_' + self.lstStep.currentItem().text() + '_' + self.combVariant.currentText() + '_' + self.combversion.currentText() + '.ma'
            if os.path.exists(new_path + '/' + new_file):
                dcclanch.start('maya',new_path + '/' + new_file)
        else:
            from fcLib.appLib import fcPrompt
            reload(fcPrompt)
            self.fcPrompt = fcPrompt.FcPrompt()







    #*********************************************************************
    # FUNCTIONS
    def fill_meta(self):
        self.combVariant.show()
        self.combversion.show()
        # self.btnCreate.show()
        self.btnLoad.show()


        # self.wgPreview.lblTitle.setText(self.file_name)
        # self.wgPreview.lblDate.setText(str(datetime.datetime.fromtimestamp(os.path.getmtime(self.load_file))).split(".")[0])
        # self.wgPreview.lblSize.setText(str("{0:.2f}".format(os.path.getsize(self.load_file)/(1024*1024.0)) + " MB"))
        #
        # self.extension = self.wgLoad.lstFiles.currentItem().text().split('.')[-1]
        # if self.extension in self.data['script'][TITLE].get('img'): software_img = "software/img"
        # else: software_img = "software/" + self.software_format[self.extension]
        # if self.file_data and self.file_data.has_key(self.wgLoad.lstFiles.currentItem().text()):
        #     current_file = self.file_data[self.wgLoad.lstFiles.currentItem().text()]
        #     comment = current_file.get('comment')
        #     user_id = current_file.get('user')
        # else:
        #     comment = ''
        #     user_id = 'unknown'
        #
        # self.wgPreview.edtComment.setPlainText(comment)
        # self.wgPreview.lblUser.setText(user_id)
        # self.wgPreview.lblSoftwareIcon.setPixmap(QtGui.QPixmap(QtGui.QImage(Tank().get_img_path(software_img))))
        # self.wgPreview.lblUserIcon.setPixmap(QtGui.QPixmap(QtGui.QImage(Tank().get_img_path('user/' + user_id))))

    def clear_meta(self):
        self.combVariant.clear()
        self.combVariant.hide()
        self.combversion.clear()
        self.combversion.hide()
        self.labelPreview.clear()
        # self._scaled = Tank().get_data('script')[self.lstModule.currentItem().text()]
        # print self._scaled
        self.labelPreview.setPixmap(QtGui.QPixmap(QtGui.QImage(Tank().get_img_path('btn/thumbnail'))).scaled(200, 200))
        self.btnCreate.hide()
        self.btnLoad.hide()
        self.btnSave.hide()


def create():
    app = QtWidgets.QApplication(sys.argv)
    main_widget = FcLoadTask()
    sys.exit(app.exec_())


def start():
    global main_widget
    main_widget = FcLoadTask()
# create()
