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


def getMainWindow():
    '''This function should be overriden'''
    if os.environ['Environment'] == 'Maya':
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
            print entry.objectName()
            try:
                if entry.objectName() == "FcLoadTask":
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
        new_path    = os.environ['FC_SERVER_ROOT'] + '/' + self.lstModule.currentItem().text()
        print new_path
        tmp_content = folder.get_file_list(new_path)
        print tmp_content

        self.lstClass.clear()
        if tmp_content:
            self.lstClass.addItems(sorted(tmp_content))
            self.lstClass.setCurrentRow(0)

    @Slot()
    def on_lstClass_itemSelectionChanged(self):
        self.change_lstEntity()

    def change_lstEntity(self):
        new_path    = os.environ['FC_SERVER_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text()
        tmp_content = folder.get_file_list(new_path)

        self.lstEntity.clear()
        if tmp_content:
            self.lstEntity.addItems(sorted(tmp_content))
            self.lstEntity.setCurrentRow(0)

    @Slot()
    def on_lstEntity_itemSelectionChanged(self):
        self.change_lstStep()

    def change_lstStep(self):
        new_path    = os.environ['FC_SERVER_ROOT'] + '/' + self.lstModule.currentItem().text() + '/' + self.lstClass.currentItem().text() + '/' + self.lstEntity.currentItem().text()
        tmp_content = folder.get_file_list(new_path)

        self.lstStep.clear()
        if tmp_content:
            self.lstStep.addItems(sorted(tmp_content))
            self.lstStep.setCurrentRow(0)

    @Slot()
    def on_lstStep_itemSelectionChanged(self):
        self.fill_meta()

    def change_lstStatus(self):
        if self.scene_steps < 5: part_path = ''
        else: part_path = self.wgLoad.lstAsset.currentItem().text() + '/'

        if not self.wgLoad.lstStatus.currentItem() or not self.wgLoad.lstTask.currentItem(): return

        self.file_dir = self.load_dir + '/' + self.wgLoad.lstSet.currentItem().text() + '/' + part_path + self.wgLoad.lstTask.currentItem().text() + '/' + self.wgLoad.lstStatus.currentItem().text()
        tmp_content   = folder.get_file_list(self.file_dir, extension=True)

        self.wgLoad.lstFiles.clear()
        if not tmp_content: return

        file_list = []
        for file in tmp_content:
            if os.path.splitext(file)[1][1:] in self.software_keys: file_list.append(file)

        if file_list:
            if os.path.exists(self.file_dir + Tank().data_project['META']['file']):
                self.file_data = Tank().get_yml_file(self.file_dir + Tank().data_project['META']['file'])
            else: self.file_data = ''

            self.wgLoad.lstFiles.addItems(sorted(file_list, reverse=True))
            self.wgLoad.lstFiles.setCurrentRow(0)

    def change_lstFiles(self):
        self.extension = self.wgLoad.lstFiles.currentItem().text().split('.')[-1]
        self.file_name = self.wgLoad.lstFiles.currentItem().text().split('.')[0]

        if self.extension in self.data['script'][TITLE]['img']:
            self.preview_img_path = self.file_dir + '/' + self.wgLoad.lstFiles.currentItem().text()
        else:
            self.preview_img_path = self.file_dir + '/' + Tank().data_project['META']['dir'] + '/' + self.file_name + '.' + self.data['project']['EXTENSION']['thumbnail']

        self.load_file = self.file_dir + '/' + self.wgLoad.lstFiles.currentItem().text()

        if os.path.exists(self.preview_img_path):
            self.wgPreview.btnPreviewImg.setIcon(QtGui.QPixmap(QtGui.QImage(self.preview_img_path)))
        else: self.wgPreview.btnPreviewImg.setIcon(QtGui.QPixmap(QtGui.QImage(Tank().get_img_path("lbl/default"))))

        self.set_open_folder(self.file_dir)

        if os.path.exists(self.load_file): self.fill_meta()
        else: self.clear_meta()


    #*********************************************************************
    # FUNCTIONS
    def fill_meta(self):
        self.wgPreview.lblTitle.setText(self.file_name)
        self.wgPreview.lblDate.setText(str(datetime.datetime.fromtimestamp(os.path.getmtime(self.load_file))).split(".")[0])
        self.wgPreview.lblSize.setText(str("{0:.2f}".format(os.path.getsize(self.load_file)/(1024*1024.0)) + " MB"))

        self.extension = self.wgLoad.lstFiles.currentItem().text().split('.')[-1]
        if self.extension in self.data['script'][TITLE].get('img'): software_img = "software/img"
        else: software_img = "software/" + self.software_format[self.extension]
        if self.file_data and self.file_data.has_key(self.wgLoad.lstFiles.currentItem().text()):
            current_file = self.file_data[self.wgLoad.lstFiles.currentItem().text()]
            comment = current_file.get('comment')
            user_id = current_file.get('user')
        else:
            comment = ''
            user_id = 'unknown'

        self.wgPreview.edtComment.setPlainText(comment)
        self.wgPreview.lblUser.setText(user_id)
        self.wgPreview.lblSoftwareIcon.setPixmap(QtGui.QPixmap(QtGui.QImage(Tank().get_img_path(software_img))))
        self.wgPreview.lblUserIcon.setPixmap(QtGui.QPixmap(QtGui.QImage(Tank().get_img_path('user/' + user_id))))

    def clear_meta(self):
        self.wgPreview.lblUser.setText('')
        self.wgPreview.lblTitle.setText('')
        self.wgPreview.lblDate.setText('')
        self.wgPreview.lblSize.setText('')
        self.wgPreview.edtComment.setPlainText('')
        self.set_open_folder('')
        self.wgPreview.lblSoftwareIcon.setPixmap(QtGui.QPixmap(QtGui.QImage('')))
        self.wgPreview.lblUserIcon.setPixmap(QtGui.QPixmap(QtGui.QImage('')))


def create():
    app = QtWidgets.QApplication(sys.argv)
    main_widget = FcLoadTask()
    sys.exit(app.exec_())


def start():
    global main_widget
    main_widget = FcLoadTask()

# create()
