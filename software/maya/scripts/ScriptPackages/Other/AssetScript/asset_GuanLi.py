#!/usr/bin/env python
# -*- coding: utf-8 -*-
#file :asset_manage_tool.py
#author:u'韩德贵'
#email:1161516272@qq.com
#blog:http://blog.sina.com.cn/u/5617189132
#date:2017.11.23

#from PyQt4 import QtGui  # PyQt4
#from PySide import QtGui # PySide
#from  functools import partial
#Author = u'Author: 韩德贵  http://blog.sina.com.cn/u/5617189132'



import sys
import os
import os.path
import maya.cmds as cmds
import maya.mel
import codecs
def CGStorm_Asset_Manage_dir():
    global Asrlry_Path
    script = os.getcwd()
    scripts_dir = os.path.dirname(script)
    Asrlry_Path = scripts_dir + r'/scripts'

class CGStorm_Asset_Manage_UI():
    '''create main UI'''
    def __init__(self):
        global Asrlry_Path
        # script = os.path.realpath(__file__)
        # scripts_dir = os.path.dirname(script)
        # Asrlry_Path = scripts_dir + r'/scripts'
        '''get all need path ,and comman attribute'''
        self.windowName = u'CGStorm_Asset_manage_Window'
        self.windowTitle = u'资产管理工具'
        self.paneLayoutName = u'CGStormAssetManagePaneLayout'
        #self.assetPath = u'R:/resources/resources/asset_Library'
        #self.assetPath = u'L:/Asrlry/Assetlibrary'
        self.assetPath =''
        self.assetTestPath =''# u'D:/asset_test/model_asset/props/apple'
        self.userAppDir = cmds.internalVar(userAppDir=True)
        self.modules = ['scenes','rig','comp','fur','Animation','light','fx']
        #预览窗口的名字属性
        self.picPreviwWindow = ''
        #中间按钮名字属性
        self.bottonName = ''

        #图片后缀格式
        self.pictureExt = '.jpg'
        #文件名字空间属性
        self.nameSpace = ''

        #右边文件框列表布局属性
        self.scrollLayout_right_fileList = ''
        # 中间文件框列表布局属性
        self.scrollLayout_middle_picList = ''
        # 左边文件框列表布局属
        self.scrollLayout_left_DirList = ''
        #文件夹列表的framelayout名字属性
        self.assetTypeDir = 'asset_type_dir_frame_layout'
        #选择模块的属性
        self.selectedModule = ''
        #文件夹属性
        self.assetTypeDirList = {}
        self.assetTypeList = {}
        self.assetTypeList_bake = {}
        #创建一个名字对应字典
        self.asset_type_key = {'mod': u'模型资产库','rig': u'绑定资产库', 'fur': u'毛发模块', 'comp': u'合成模块', 'Animation': u'动画模块', 'light': u'灯光模块',
                               'fx': u'特效模块'}

        # self.screenWidth = QtGui.QDesktopWidget().screenGeometry().width()
        self.screenWidth = 256*4
        self.screenHeight = 144*4
        # self.screenHeight = QtGui.QDesktopWidget().screenGeometry().height()

        self.CGStormPath =""
        self.otherIconPath = Asrlry_Path+'/Scriptlibrary/scripts/AssetScript/icons/'
        self.mainUIiconPath = Asrlry_Path+'/Scriptlibrary/scripts/AssetScript/icons/'

        print self.CGStormPath  # 测试路径是否正确

        self.createMainUI()


    def createMainUI(self,):
        '''description'''
        if cmds.window(self.windowName, q=True, exists=True):
            print u'资产更新成功！'
            cmds.deleteUI(self.windowName)
        self.CGStormAssetManageWindow = cmds.window(self.windowName, backgroundColor=[0.15, 0.15, 0.15],
                                           retain=True, resizeToFitChildren=True, width=self.screenWidth,
                                           height=self.screenHeight,menuBar=True, title=self.windowTitle,
                                           sizeable=True)
        cmds.menu(label=u'资产目录设置', tearOff=True)
        #根据目录里面的文件，设置菜单命令
        self.create_asset_directory_menu_command()
        cmds.menuItem(divider=True)
        cmds.menuItem(label=u'删除库目录', command='run.open_asset_directory()')
        cmds.menuItem(divider=True)
        cmds.menuItem(label=u'新建库目录',command='run.set_asset_library_path_window_command()')
        cmds.menu(label=u'帮助', helpMenu=False)
        cmds.menuItem('Application...', label=u'关于资产管理工具...')

        # 采用tabLayout方式布局资产库类型，包括 ['mod','comp','fur','rig','Animation','light','fx']
        mainTabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

        #**************************************  mod  **************************************************************
        # 开始布局整个窗口，横排的三分式布局
        child_mod = cmds.paneLayout(self.paneLayoutName + u'_mod', configuration=u'vertical3')
        #布局比例 10,50,40
        cmds.paneLayout(self.paneLayoutName + u'_mod', edit=True, paneSize=[1, 10, 70])
        cmds.paneLayout(self.paneLayoutName + u'_mod', edit=True, paneSize=[3, 30, 70])
        # 新建一个左边的scrollLayout来放置资产库类型的文件夹列表
        cmds.scrollLayout(u'scrollLayout_left_Dir_List_mod',width=150, height=500,childResizable=True,
                        horizontalScrollBarThickness = 0,bgc=[0.1, 0.1, 0.1], visible=True)
        #默认创建模型目录
        #self.create_asset_type_dir_command(u'mod',u'mod')
        cmds.button(u'refresh_mod',label = u'刷 新 资 产',bgc = [0.5,0.5,0.5],
                  command = 'run.create_asset_type_dir_command(u"mod",u"mod")')
        cmds.intSliderGrp(u'mod_slider',cal =[1,'center'],columnWidth3 = [50,20,80],field=True,
                        label=u'图标数量', minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=50,value=3)
        cmds.setParent('..')
        # 中间布局
        cmds.scrollLayout(u'scrollLayout_middle_picList_mod',
                        width=self.screenWidth / 2 + 280,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1],
                        visible=True)
        cmds.setParent('..')

        # 右边布局############################################################################
        # 创建一个layout来放置切换的布局
        cmds.scrollLayout(u'scrollLayout_right_mod',
                        width=self.screenWidth / 4 - 10,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1], visible=True)

        cmds.setParent('..')
        cmds.setParent('..')

        # **************************************  rig  **************************************************************
        # 开始布局整个窗口，横排的三分式布局
        child_rig = cmds.paneLayout(self.paneLayoutName + u'_rig', configuration=u'vertical3')
        # 布局比例 10,50,40
        cmds.paneLayout(self.paneLayoutName + u'_rig', edit=True, paneSize=[1, 10, 70])
        cmds.paneLayout(self.paneLayoutName + u'_rig', edit=True, paneSize=[3, 30, 70])
        # 新建一个左边的scrollLayout来放置资产库类型的文件夹列表
        cmds.scrollLayout(u'scrollLayout_left_Dir_List_rig', width=150, height=500, childResizable=True,
                        horizontalScrollBarThickness=0, bgc=[0.1, 0.1, 0.1], visible=True)
        # 默认创建模型目录
        # self.create_asset_type_dir_command(u'rig',u'rig')
        cmds.button(u'refresh_rig', label=u'刷 新 绑 定 素 材', bgc=[0.5, 0.5, 0.5],
                  command='run.create_asset_type_dir_command(u"rig",u"rig")')
        cmds.intSliderGrp(u'rig_slider', cal=[1, 'center'], columnWidth3=[50, 20, 80], field=True,
                        label=u'图标数量', minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=50, value=3)
        cmds.setParent('..')
        # 中间布局
        cmds.scrollLayout(u'scrollLayout_middle_picList_rig',
                        width=self.screenWidth / 2 + 280,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1],
                        visible=True)
        cmds.setParent('..')

        # 右边布局############################################################################
        # 创建一个layout来放置切换的布局
        cmds.scrollLayout(u'scrollLayout_right_rig',
                        width=self.screenWidth / 4 - 10,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1], visible=True)

        cmds.setParent('..')
        cmds.setParent('..')

        # **************************************  fur  **************************************************************
        # 开始布局整个窗口，横排的三分式布局
        child_fur = cmds.paneLayout(self.paneLayoutName + u'_fur', configuration=u'vertical3')
        # 布局比例 10,50,40
        cmds.paneLayout(self.paneLayoutName + u'_fur', edit=True, paneSize=[1, 10, 70])
        cmds.paneLayout(self.paneLayoutName + u'_fur', edit=True, paneSize=[3, 30, 70])
        # 新建一个左边的scrollLayout来放置资产库类型的文件夹列表
        cmds.scrollLayout(u'scrollLayout_left_Dir_List_fur', width=150, height=500, childResizable=True,
                        horizontalScrollBarThickness=0, bgc=[0.1, 0.1, 0.1], visible=True)
        # 默认创建模型目录
        # self.create_asset_type_dir_command(u'fur',u'fur')
        cmds.button(u'refresh_fur', label=u'刷 新 资 产', bgc=[0.5, 0.5, 0.5],
                  command='run.create_asset_type_dir_command(u"fur",u"fur")')
        cmds.intSliderGrp(u'fur_slider', cal=[1, 'center'], columnWidth3=[50, 20, 80], field=True,
                        label=u'图标数量', minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=50, value=3)
        cmds.setParent('..')
        # 中间布局
        cmds.scrollLayout(u'scrollLayout_middle_picList_fur',
                        width=self.screenWidth / 2 + 280,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1],
                        visible=True)
        cmds.setParent('..')

        # 右边布局############################################################################
        # 创建一个layout来放置切换的布局
        cmds.scrollLayout(u'scrollLayout_right_fur',
                        width=self.screenWidth / 4 - 10,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1], visible=True)

        cmds.setParent('..')
        cmds.setParent('..')


        # **************************************  Animation  **************************************************************
        # 开始布局整个窗口，横排的三分式布局
        child_Animation = cmds.paneLayout(self.paneLayoutName + u'_Animation', configuration=u'vertical3')
        # 布局比例 10,50,40
        cmds.paneLayout(self.paneLayoutName + u'_Animation', edit=True, paneSize=[1, 10, 70])
        cmds.paneLayout(self.paneLayoutName + u'_Animation', edit=True, paneSize=[3, 30, 70])
        # 新建一个左边的scrollLayout来放置资产库类型的文件夹列表
        cmds.scrollLayout(u'scrollLayout_left_Dir_List_Animation', width=150, height=500, childResizable=True,
                        horizontalScrollBarThickness=0, bgc=[0.1, 0.1, 0.1], visible=True)
        # 默认创建模型目录
        # self.create_asset_type_dir_command(u'Animation',u'Animation')
        cmds.button(u'refresh_Animation', label=u'刷 新 动 作 素 材', bgc = [0.5,0.5,0.5],
                  command='run.create_asset_type_dir_command(u"Animation",u"Animation")')
        cmds.intSliderGrp(u'Animation_slider', cal=[1, 'center'], columnWidth3=[50, 20, 80], field=True,
                        label=u'图标数量', minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=50, value=3)
        cmds.setParent('..')
        # 中间布局
        cmds.scrollLayout(u'scrollLayout_middle_picList_Animation',
                        width=self.screenWidth / 2 + 280,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1],
                        visible=True)
        cmds.setParent('..')

        # 右边布局############################################################################
        # 创建一个layout来放置切换的布局
        cmds.scrollLayout(u'scrollLayout_right_Animation',
                        width=self.screenWidth / 4 - 10,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1], visible=True)

        cmds.setParent('..')
        cmds.setParent('..')

        # **************************************  light  **************************************************************
        # 开始布局整个窗口，横排的三分式布局
        child_light = cmds.paneLayout(self.paneLayoutName + u'_light', configuration=u'vertical3')
        # 布局比例 10,50,40
        cmds.paneLayout(self.paneLayoutName + u'_light', edit=True, paneSize=[1, 10, 70])
        cmds.paneLayout(self.paneLayoutName + u'_light', edit=True, paneSize=[3, 30, 70])
        # 新建一个左边的scrollLayout来放置资产库类型的文件夹列表
        cmds.scrollLayout(u'scrollLayout_left_Dir_List_light', width=150, height=500, childResizable=True,
                        horizontalScrollBarThickness=0, bgc=[0.1, 0.1, 0.1], visible=True)
        # 默认创建模型目录
        # self.create_asset_type_dir_command(u'light',u'light')
        cmds.button(u'refresh_light', label=u'刷 新 灯 光 素 材', bgc = [0.5,0.5,0.5],
                  command='run.create_asset_type_dir_command(u"light",u"light")')
        cmds.intSliderGrp(u'light_slider', cal=[1, 'center'], columnWidth3=[50, 20, 80], field=True,
                        label=u'图标数量', minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=50, value=3)
        cmds.setParent('..')
        # 中间布局
        cmds.scrollLayout(u'scrollLayout_middle_picList_light',
                        width=self.screenWidth / 2 + 280,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1],
                        visible=True)
        cmds.setParent('..')

        # 右边布局############################################################################
        # 创建一个layout来放置切换的布局
        cmds.scrollLayout(u'scrollLayout_right_light',
                        width=self.screenWidth / 4 - 10,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1], visible=True)

        cmds.setParent('..')
        cmds.setParent('..')

        # **************************************  fx  **************************************************************
        # 开始布局整个窗口，横排的三分式布局
        child_fx = cmds.paneLayout(self.paneLayoutName + u'_fx', configuration=u'vertical3')
        # 布局比例 10,50,40
        cmds.paneLayout(self.paneLayoutName + u'_fx', edit=True, paneSize=[1, 10, 70])
        cmds.paneLayout(self.paneLayoutName + u'_fx', edit=True, paneSize=[3, 30, 70])
        # 新建一个左边的scrollLayout来放置资产库类型的文件夹列表
        cmds.scrollLayout(u'scrollLayout_left_Dir_List_fx', width=150, height=500, childResizable=True,
                        horizontalScrollBarThickness=0, bgc=[0.1, 0.1, 0.1], visible=True)
        # 默认创建模型目录
        # self.create_asset_type_dir_command(u'fx',u'fx')
        cmds.button(u'refresh_fx', label=u'刷 新 特 效 素 材', bgc = [0.5,0.5,0.5],
                  command='run.create_asset_type_dir_command(u"fx",u"fx")')
        cmds.intSliderGrp(u'fx_slider', cal=[1, 'center'], columnWidth3=[50, 20, 80], field=True,
                        label=u'图标数量', minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=50, value=3)
        cmds.setParent('..')
        # 中间布局
        cmds.scrollLayout(u'scrollLayout_middle_picList_fx',
                        width=self.screenWidth / 2 + 280,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1],
                        visible=True)
        cmds.setParent('..')

        # 右边布局############################################################################
        # 创建一个layout来放置切换的布局
        cmds.scrollLayout(u'scrollLayout_right_fx',
                        width=self.screenWidth / 4 - 10,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1], visible=True)

        cmds.setParent('..')
        cmds.setParent('..')

        # ********************************************  comp   ******************************************************
        # 开始布局整个窗口，横排的三分式布局
        child_comp = cmds.paneLayout(self.paneLayoutName + u'_comp', configuration=u'vertical3')
        # 布局比例 10,50,40
        cmds.paneLayout(self.paneLayoutName + u'_comp', edit=True, paneSize=[1, 10, 70])
        cmds.paneLayout(self.paneLayoutName + u'_comp', edit=True, paneSize=[3, 30, 70])
        # 新建一个左边的scrollLayout来放置资产库类型的文件夹列表
        cmds.scrollLayout(u'scrollLayout_left_Dir_List_comp', width=150, height=500, childResizable=True,
                        horizontalScrollBarThickness=0, bgc=[0.1, 0.1, 0.1], visible=True)
        # 默认创建贴图目录
        # self.create_asset_type_dir_command(u'comp',u'comp')
        cmds.button(u'refresh_comp', label=u'刷 新 贴 图 素 材', bgc=[0.5, 0.5, 0.5],
                  command='run.create_asset_type_dir_command(u"comp",u"comp")')
        cmds.intSliderGrp(u'comp_slider', cal=[1, 'center'], columnWidth3=[50, 20, 80], field=True,
                        label=u'图标数量', minValue=1, maxValue=10, fieldMinValue=1, fieldMaxValue=50, value=3)
        cmds.setParent('..')
        # 中间布局
        cmds.scrollLayout(u'scrollLayout_middle_picList_comp',
                        width=self.screenWidth / 2 + 280,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1],
                        visible=True)
        cmds.setParent('..')

        # 右边布局############################################################################
        # 创建一个layout来放置切换的布局
        cmds.scrollLayout(u'scrollLayout_right_comp',
                        width=self.screenWidth / 4 - 10,
                        height=670,
                        childResizable=True,
                        horizontalScrollBarThickness=0,
                        bgc=[0.1, 0.1, 0.1], visible=True)

        cmds.setParent('..')
        cmds.setParent('..')

        cmds.tabLayout(mainTabs, edit=True, tabLabel=((child_mod, self.asset_type_key[u'mod']), \
                                                    (child_rig, self.asset_type_key[u'rig']), \
                                                    (child_fur, self.asset_type_key[u'fur']),\
                                                    (child_comp,self.asset_type_key[u'comp']),\
                                                    (child_Animation,self.asset_type_key[u'Animation']),\
                                                    (child_light,self.asset_type_key[u'light']),\
                                                    (child_fx,self.asset_type_key[u'fx'])))

        cmds.showWindow(self.CGStormAssetManageWindow)

    def create_asset_type_dir_command(self,selectedModule = u'mod',moduleName = u'mod'):
        '''获取到选择的库类型，创建对应的文件夹列表'''
        self.selectedModule = selectedModule
        #self.selectedModule = cmds.radioCollection('asset_type', query=True, select=True)
        if cmds.frameLayout('asset_type_dir_frame_layout' + '_' + moduleName , q=True, exists=True):
            print (u'显示 '+ self.asset_type_key[self.selectedModule] + u' 资产')
            cmds.deleteUI('asset_type_dir_frame_layout' + '_' + moduleName)
        cmds.frameLayout('asset_type_dir_frame_layout' + '_' + moduleName,
                       label=self.asset_type_key[self.selectedModule] + u'  子类型列表',
                       parent = u'scrollLayout_left_Dir_List' + '_' + moduleName)
        cmds.columnLayout(bgc=[0.1, 0.1, 0.1],adjustableColumn = True)
        #获取文件夹列表创建对应的framelayout
        if os.path.exists(self.assetPath + '/'+ selectedModule ):
            self.assetTypeDirList = os.listdir(self.assetPath + '/'+ selectedModule )
            if self.assetTypeDirList:
                if 'Thumbs.db' in self.assetTypeDirList:
                    self.assetTypeDirList.remove('Thumbs.db')
                for oneDir in self.assetTypeDirList:
                    if os.path.isdir(self.assetPath + '/'+ selectedModule + '/' + oneDir):
                        cmds.frameLayout(label=oneDir, borderVisible=False, collapsable=True, collapse=True,
                                       bgc=[0.1, 0.1, 0.1], marginWidth=20, width=150,
                                       collapseCommand='run.create_asset_persp_pic_command("'+ \
                                                       self.assetPath + '/'+ selectedModule + '/' + oneDir+'","'+moduleName + '")',
                                       expandCommand='run.create_asset_persp_pic_command("'+ \
                                                     self.assetPath + '/'+ selectedModule + '/' +oneDir+'","'+moduleName + '")')
                        # aa
                        cmds.columnLayout(bgc=[0.1, 0.1, 0.1])


                        self.assetTypeList = os.listdir(self.assetPath + '/' + selectedModule + '/' + oneDir)
                        if 'Thumbs.db' in self.assetTypeList:
                            self.assetTypeList.remove('Thumbs.db')
                        if self.assetTypeList:
                            for oneAsset in self.assetTypeList:
                                if os.path.isdir(self.assetPath + '/' + selectedModule + '/' + oneDir+ '/'+oneAsset):
                                    cmds.frameLayout(label=oneAsset, borderVisible=False, collapsable=True, collapse=True,
                                                   font='fixedWidthFont', bgc=[0.1, 0.1, 0.1], marginWidth=20,
                                                   collapseCommand='run.create_asset_persp_pic_command("' + \
                                                                   self.assetPath + '/' + selectedModule \
                                                                   + '/'+oneDir+'/'+ oneAsset+'","'+moduleName + '")',
                                                   expandCommand='run.create_asset_persp_pic_command("'+self.assetPath \
                                                                 + '/' +selectedModule + '/' +oneDir+'/'+ oneAsset+'","'+moduleName + '")')
                                    cmds.columnLayout(bgc=[0.1, 0.1, 0.1])
                                    self.assetTypeList_bake = os.listdir(self.assetPath + '/' + selectedModule \
                                                                         + '/' + oneDir+ '/'+oneAsset)
                                    if 'Thumbs.db' in self.assetTypeList_bake:
                                        self.assetTypeList_bake.remove('Thumbs.db')
                                    if self.assetTypeList_bake:
                                        for oneAsset_bake in self.assetTypeList_bake:
                                            if os.path.isdir(self.assetPath + '/' +selectedModule+ '/'+oneDir+ '/' \
                                                                     + oneAsset + '/'+oneAsset_bake):
                                                cmds.frameLayout(label=oneAsset_bake, borderVisible=False,
                                                               collapsable=False,
                                                               collapse=True,
                                                               font='fixedWidthFont', bgc=[0.1, 0.1, 0.1],
                                                               marginWidth=20,
                                                               collapseCommand='run.create_asset_persp_pic_command("'+ \
                                                                               self.assetPath + '/' + selectedModule \
                                                                               + '/' + oneDir + '/' + oneAsset + '/'\
                                                                               +oneAsset_bake+ '","'+moduleName + '")',
                                                               expandCommand='run.create_asset_persp_pic_command("' + \
                                                                             self.assetPath + '/' + selectedModule \
                                                                             + '/' + oneDir + '/'+ oneAsset+ '/'\
                                                                             +oneAsset_bake+ '","'+moduleName + '")')
                                                cmds.setParent('..')
                                    cmds.setParent('..')
                                    cmds.setParent('..')

                        cmds.setParent('..')
                        cmds.setParent('..')
        #bb
        cmds.setParent('..')
        cmds.setParent('..')

    def create_asset_persp_pic_command(self,dirPath,moduleName = u'mod'):
        '''创建缩略图显示列表'''
        #删除已经有的pic图标，新建选择的目录缩略图
        if (cmds.scrollLayout(u'scrollLayout_middle_picList'+ '_'+ moduleName, query=True,childArray = True)):
            for one in cmds.scrollLayout(u'scrollLayout_middle_picList'+ '_'+ moduleName, query=True,childArray = True):
                cmds.deleteUI(one,layout = True)

        #每次都查询显示图标多少来确定
        value = cmds.intSliderGrp(moduleName + '_slider', query=True, value=True)
        cmds.rowColumnLayout(u'middle_rowColumnLayout'+ '_'+ moduleName,numberOfColumns = value,
                           parent = u'scrollLayout_middle_picList'+ '_'+ moduleName)

        #搜索给定路径里面的文件夹以及文件，获取对应图标，生成缩略图按钮，
        print '*****'
        print dirPath
        print '*****'
        dirName = os.path.split(dirPath)[1] + self.pictureExt
        if os.path.isdir(dirPath):
            dirList = os.listdir(dirPath)
            if 'Thumbs.db' in dirList:
                dirList.remove('Thumbs.db')
            if dirList:
                print dirList
                for oneDir in dirList:
                    if os.path.isdir(dirPath+'/'+oneDir):
                        if os.path.exists(dirPath + '/'+ oneDir + '/' + oneDir +self.pictureExt):
                            print '%%%%%'
                            print (dirPath + '/'+ oneDir + '/' + oneDir +self.pictureExt)
                            print '%%%%%'
                            cmds.iconTextButton(style='iconAndTextVertical', label=(oneDir +self.pictureExt),
                                              image1=(dirPath + '/'+ oneDir + '/' + oneDir +self.pictureExt),
                                              command='run.create_asset_selected_details_command("' + \
                                                      dirPath + '/' + oneDir + '","'+moduleName + '")',
                                              width =256,height =276,
                                              parent = u'middle_rowColumnLayout'+ '_'+ moduleName,
                                              doubleClickCommand='run.preview_pic_window_command("'\
                                                     +dirPath + '/'+ oneDir + '/' + oneDir +self.pictureExt+'")')
                            #选择模型库的贴图后右键所产生的按钮和命令
                            if 'mod' in dirPath.split('/'):
                                dirName = os.path.split(dirPath)[1]
                                self.assetTestPath = dirPath
                                
                                cmds.popupMenu(markingMenu=True)
                                # ---------------------------S-----------------------------------------------------
                            cmds.menuItem(radialPosition='N', label=u'    打开路径     ',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath +"/"+ oneDir +'\\")")')
                            cmds.menuItem(radialPosition='S', label=u'     导入Assembly     ',
                                        command='run.maya_tool_command("' + self.assetTestPath+  '/' + oneDir +  '/'+ oneDir+"_AR.ma"+ '","import","mayaAscii")') 
                            cmds.menuItem(radialPosition='SW', label=u'   静态Arnold代理   ',
                                        command='run.maya_tool_command("' + self.assetTestPath+  '/' + oneDir +  '/'+ oneDir+"_Proxy_Ar_Static.ma"+ '","import","mayaAscii")')  
                            cmds.menuItem(radialPosition='SE', label=u'   静态Redshift代理   ',
                                        command='run.maya_tool_command("' + self.assetTestPath+  '/' + oneDir +  '/'+ oneDir+"_Proxy_Rs_Static.ma"+ '","import","mayaAscii")')
                        else:
                            print u'没有对应的缩略图文件！'
                    elif oneDir == dirName:
                        print '%%%%%'
                        print dirName
                        print '%%%%%'
                        self.bottonName = cmds.iconTextButton(style='iconAndTextVertical', label=dirName,
                                          image1=(dirPath + '/' + dirName),width =256,height =276,
                                          parent = u'middle_rowColumnLayout'+ '_'+ moduleName,
                                          command='run.create_asset_selected_details_command("'+dirPath+'","'+moduleName + '")',
                                          doubleClickCommand='run.preview_pic_window_command("' \
                                                     + dirPath + '/' + dirName + '")')
                        if 'mod' in dirPath.split('/'):
                            dirName = os.path.split(dirPath)[1]
                            self.assetTestPath = dirPath
                            
                            cmds.popupMenu(markingMenu=True)
                            # ---------------------------S-----------------------------------------------------
                        cmds.menuItem(radialPosition='N', label=u'    打开路径     ',
                                    command='maya.mel.eval("openDir(\\"' + self.assetTestPath +"/"+ oneDir +'\\")")')
                        cmds.menuItem(radialPosition='S', label=u'     导入Assembly     ',
                                    command='run.maya_tool_command("' + self.assetTestPath+  '/' + oneDir +  '/'+ oneDir+"_AR.ma"+ '","import","mayaAscii")') 
                        cmds.menuItem(radialPosition='SW', label=u'   静态Arnold代理   ',
                                    command='run.maya_tool_command("' + self.assetTestPath+  '/' + oneDir +  '/'+ oneDir+"_Proxy_Ar_Static.ma"+ '","import","mayaAscii")')  
                        cmds.menuItem(radialPosition='SE', label=u'   静态Redshift代理   ',
                                    command='run.maya_tool_command("' + self.assetTestPath+  '/' + oneDir +  '/'+ oneDir+"_Proxy_Rs_Static.ma"+ '","import","mayaAscii")')    			

                    else:
                        print u'其他不识别文件！'
                cmds.setParent('..')

    def create_asset_selected_details_command(self,dirPath,moduleName = u'mod'):
        # 如果存在右边layoutUI，就删掉重新创建
        # self.pane_scrollLayout_right = cmds.scrollLayout(u'scrollLayout_right', bgc=[0.15, 0.15, 0.15])
        if (cmds.scrollLayout(u'scrollLayout_right'+ '_'+ moduleName, query=True,childArray = True)):
            for one in cmds.scrollLayout(u'scrollLayout_right'+ '_'+ moduleName, query=True,childArray = True):
                cmds.deleteUI(one, layout=True)

        # 文件筐里面的布局
        dirName = os.path.split(dirPath)[1]
        cmds.rowColumnLayout(u'right_rowColumnLayout'+ '_'+ moduleName,numberOfColumns=1,
                           parent = u'scrollLayout_right'+ '_'+ moduleName)
        cmds.separator(style=u'in', height=10, width=self.screenWidth / 4 - 10,
                     parent = u'right_rowColumnLayout'+ '_'+ moduleName)
        cmds.text(label=(dirName + u'  资产文件列表'), width=self.screenWidth / 4 - 10,
                parent =u'right_rowColumnLayout'+ '_'+ moduleName)
        cmds.separator(style=u'in', height=10, width=self.screenWidth / 4 - 10,
                     parent = u'right_rowColumnLayout'+ '_'+ moduleName)

        # 文件和文件夹选项'D:/asset_test/model_asset/props/apple'
        self.assetTestPath = dirPath
        if os.path.exists(self.assetTestPath):
            self.fileList = os.listdir(self.assetTestPath)
            if self.fileList:
                if 'Thumbs.db' in self.fileList:
                    self.fileList.remove('Thumbs.db')
                for oneFile in self.fileList:
                    if os.path.isdir(self.assetTestPath + '/' + oneFile):
                        cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                          parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                          image1=(self.otherIconPath + 'dir.png'))
                        cmds.popupMenu(markingMenu=True)
                        cmds.menuItem(divider=True)
                        cmds.menuItem(label=u'打开当前文件目录',
                                    command='maya.mel.eval("openDir(\\"' + self.assetTestPath \
                                            + '/' + oneFile + '\\")")')
                    else:
                        if os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.mov' or \
                                        os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.avi':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'mov.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'播放',
                                        command='maya.mel.eval("check_tool(\\"' + self.assetTestPath \
                                                + '/' + oneFile + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'用RV播放',
                                        command='maya.mel.eval("rv_check_tool(\\"' + self.assetTestPath \
                                                + '/' + oneFile + '\\")")')
                        elif os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.ma':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'hsFileMayaMA.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Open',
                                        command='maya.mel.eval("openMayaFile(\\"' + self.assetTestPath \
                                                + '/' + oneFile + '\\")")')
                            cmds.menuItem(label=u'Import',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","import","mayaAscii")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Import With Namespace',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","importNS","mayaAscii")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'CreateReference',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","reference","mayaAscii")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'新开maya打开当前文件',
                                        command='maya.mel.eval("openMayaFileWithNewMaya(\\"' + self.assetTestPath \
                                                + '/' + oneFile + '\\")")')
                        elif os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.mb':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'hsFileMayaMB.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Open',
                                        command='maya.mel.eval("openMayaFile(\\"' + self.assetTestPath \
                                                + '/' + oneFile + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Import',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","import","mayaBinary")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Import With Namespace',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","importNS","mayaBinary")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'CreateReference',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","reference","mayaBinary")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'新开maya打开当前文件',
                                        command='maya.mel.eval("openMayaFileWithNewMaya(\\"' + self.assetTestPath \
                                                + '/' + oneFile + '\\")")')
                        elif os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.obj':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'hsFileOBJ.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Send To Maya',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","import","OBJ")')
                            cmds.menuItem(label=u'Send To Maya With Namespace',
                                        command='run.maya_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","importNS","OBJ")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Send To 3DsMax',
                                        command='')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Send To Houdini',
                                        command='')
                        elif os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.abc':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'hsFileABC.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Open',
                                        command='run.alembic_tool_command("'+self.assetTestPath \
                                                + '/'+oneFile + '","open")')
                            cmds.menuItem(label=u'Import To Maya',
                                        command='run.alembic_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","import")')
                            cmds.menuItem(label=u'Reference To Maya',
                                        command='run.alembic_tool_command("' + self.assetTestPath \
                                                + '/' + oneFile + '","reference")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Send To 3DsMax',
                                        command='')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Send To Houdini',
                                        command='')
                        elif os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.max':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'max_icon.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Send To 3DsMax',
                                        command='')
                        elif os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.hip' or \
                                        os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.bgeo':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'houdini.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'Send To Houdini',
                                        command='')
                        elif os.path.splitext(self.assetTestPath + '/' + oneFile)[1] == '.hdr':
                            cmds.iconTextButton(style='iconAndTextHorizontal', label=oneFile,
                                              parent=u'right_rowColumnLayout'+ '_'+ moduleName,
                                              image1=(self.otherIconPath + 'hdr.png'))
                            cmds.popupMenu(markingMenu=True)
                            cmds.menuItem(label=u'打开当前文件目录',
                                        command='maya.mel.eval("openDir(\\"' + self.assetTestPath + '\\")")')
                            cmds.menuItem(divider=True)
                            cmds.menuItem(label=u'设置为当前HDR环境',
                                        command='maya.mel.eval("setHDRtexture(\\"' + self.assetTestPath \
                                                +'/'+oneFile+ '\\")")')
        cmds.setParent('..')
        cmds.setParent('..')

    def preview_pic_window_command(self,picFilePath):
        if cmds.window('preview_window', q=True, exists=True):
            cmds.deleteUI('preview_window')
        cmds.window('preview_window',width=1024, height=1024,resizeToFitChildren=True,sizeable= True,title='Preview')
        cmds.formLayout('preview_folm')
        bt_preview = cmds.iconTextButton(style='iconAndTextHorizontal', scaleIcon=True,
                               image=picFilePath,width=1024, height=1024,
                               command='cmds.deleteUI("preview_window")', label='')
        cmds.formLayout('preview_folm', edit=True, attachForm=[(bt_preview, 'top', 0), (bt_preview, 'left', 0), \
                                                 (bt_preview, 'right', 0), (bt_preview, 'bottom', 0)])
        cmds.showWindow('preview_window')

        # abc文件相关命令工具集
        def alembic_tool_command(self, filePath, importMode):
            '''abc文件相关命令工具集'''
            if importMode == 'open':
                cmds.AbcImport(filePath, mode='open', fitTimeRange=True)
            elif importMode == 'import':
                cmds.AbcImport(filePath, mode='import')
            elif importMode == 'reference':
                # self.nameSpace = os.path.splitext(filePath.split('/')[-1])[0] #根据文件名字来得到namaspace
                self.namaSpace = filePath.split('/')[-2]  # 根据文件上级目录得到名字空间，需要上级目录和文件名一致
                cmds.file(filePath, reference=True, type="Alembic", namespace=self.namaSpace,
                        ignoreVersion=True, groupLocator=True, mergeNamespacesOnClash=False)
            else:
                print 'fileMode error!'

    # maya文件相关命令工具集
    def maya_tool_command(self, filePath, importMode='import', fileType='mayaBinary'):
        '''maya文件相关命令工具集,fileType:"mayaAscii", "mayaBinary", "mel", "OBJ",
        "directory", "plug-in", "audio", "move", "EPS",'''
        self.namaSpace = filePath.split('/')[-2]
        if importMode == 'import':
            cmds.file(filePath, i=True, type=fileType, renameAll=True, mergeNamespacesOnClash=True, namespace=':',
                    ignoreVersion=True, options="mo=1", preserveReferences=True)
        elif importMode == 'importNS':
            cmds.file(filePath, i=True, type=fileType, renameAll=True, mergeNamespacesOnClash=False,
                    namespace=self.namaSpace, ignoreVersion=True, options="mo=1", preserveReferences=True)
        elif importMode == 'reference':
            cmds.file(filePath, reference=True, type=fileType, mergeNamespacesOnClash=False,
                    namespace=self.namaSpace, ignoreVersion=True, options="mo=1", preserveReferences=True)
        else:
            print "fileMode error!"

    #设置资产库目录工具
    def set_asset_library_path_window_command(self):
        '''
        新建或者设置资产目录
        :param self:
        :return:
        '''
        windowName = u'AssetDirectoryWindow'

        if cmds.window(windowName,q=True, exists=True):
            cmds.deleteUI(windowName)
        myWindow = cmds.window(windowName,title = u'设置资产库目录')
        cmds.rowColumnLayout(numberOfColumns = 2,columnWidth = [(1,100),(2,350)])
        cmds.text(label='     ')
        cmds.text(label='     ')
        cmds.text(label=u'请输入资产库目录名称：')
        cmds.textField(u'Asset_Library_Name',text = u'朱小八')
        cmds.text(label='     ')
        cmds.text(label='     ')
        cmds.text(label=u'请输入资产库目录路径：')
        cmds.textField(u'Asset_Library_Path', text=u'Z:\\zxb\\scenes')
        cmds.text(label='     ')
        cmds.text(label='     ')
        cmds.text(label=u'按照以上的格式：')
        cmds.button(label = u'  设置新的资产库目录  ',
                  command = u'run.save_comment_to_file()')
        cmds.text(label='     ')
        cmds.text(label='     ')

        cmds.showWindow(myWindow)

    def save_comment_to_file(self):
        '''
        保存内容到文件
        :return:
        '''
        path = self.userAppDir + u'assetLibraryDirectory/'
        if not os.path.exists(path):
            os.makedirs(path)
        filePath = path + cmds.textField(u'Asset_Library_Name', query=True, text=True, ) + '.xml'
        comment = cmds.textField(u'Asset_Library_Path', query=True, text=True)
        comment = comment.replace('\\','/')
        print comment+u'  新建资产目录成功'
        with open(filePath, 'w') as f:
            f.write(comment)
        #初始化当前目录为资产库目录
        self.assetPath = comment
    def save_defalt_derectory_to_file(self,comment):
        '''
        设置默认启动目录
        :return:
        '''
        path = self.userAppDir + u'assetLibraryDirectory/'
        if not os.path.exists(path):
            os.makedirs(path)
        filePath = path + 'defalt' + '.xml'
        comment = comment.replace('\\', '/')
        print comment+u'  默认启动路径设置成功'
        with open(filePath, 'w') as f:
            f.write(comment)

    def get_comment_of_file(self,filePath):
        '''
        读取文件内容
        :param filePath:
        :return:
        '''
        if os.path.isfile(filePath):
            with open(filePath, 'r') as f:
                comment = f.read()
            return comment
        else:
            return ''

    def create_asset_directory_menu_command(self):
        '''
        获取maya文档路径下面是否存在资产目录文件，并读取内容，设置为菜单命令
        :return:
        '''
        path = self.userAppDir + u'assetLibraryDirectory/'
        #获取defalt启动目录
        defaltComment = self.get_comment_of_file(path + u'defalt.xml')

        cmds.menuItem(divider=True, dividerLabel=u'资产库目录选项')
        cmds.radioMenuItemCollection()
        if os.path.exists(path):
            fileList = os.listdir(path)
            if fileList:
                for one in fileList:
                    if os.path.isfile(path + one):
                        if one != u'defalt.xml':
                            label = os.path.splitext(one)[0]
                            comment = self.get_comment_of_file(path + '/'+one)
                            command = 'run.assetPath = "'+ comment + '"'
                            #print command
                            #根据defalt启动目录文件，来确定当前启动的资产库目录是哪个
                            if defaltComment == comment:
                                cmds.menuItem(label=label, radioButton=True, command=command)
                            else:
                                cmds.menuItem(label=label, radioButton=False,command=command)
                            # 并且把素材库路径设置为最后一个列表的路径
                if defaltComment:
                    self.assetPath = defaltComment
                else:
                    self.assetPath = comment

        cmds.menuItem(divider=True, dividerLabel=u'默认资产库目录选项')
        cmds.menuItem(subMenu=True, label=u'设置默认目录')
        cmds.radioMenuItemCollection()
        if os.path.exists(path):
            fileList = os.listdir(path)
            if fileList:
                for one in fileList:
                    if os.path.isfile(path + one):
                        if one != u'defalt.xml':
                            label = os.path.splitext(one)[0]
                            comment = self.get_comment_of_file(path + '/'+one)
                            cmds.menuItem(label=u'设置 '+label + u' 为默认启动目录', radioButton=False,
                                        command='run.save_defalt_derectory_to_file("'+ comment +'")')
        cmds.setParent('..',menu = True)

    #打开目录
    def open_asset_directory(self):
        path = self.userAppDir + u'assetLibraryDirectory/'
        if os.path.isdir(path):
            try:
                os.startfile(path)
            except:
                subprocess.Popen(['xdg-open', path])

    # todo
    # 发送文件到max相关命令集合，fileType有alembic，obj，fbx等等，
    def send_file_to_max_command(self, filePath, importMode='import', fileType='alembic'):
        '''todo'''
        pass

    # todo
    # 发送文件到houdini相关命令集合，fileType有alembic，obj，fbx等等，
    def send_file_to_houdini_command(self, filePath, importMode, fileType='alembic'):
        '''todo'''
        pass




if __name__ == '__main__':
    CGStorm_Asset_Manage_dir()
    run = CGStorm_Asset_Manage_UI()



