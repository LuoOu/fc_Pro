# -*- coding: UTF-8 -*-
# .@FileName:ModelClean_link
# .@Date:2019-03-15:18:53
# .@Aurhor:LuoOu

import maya.cmds as cmds
import re
import maya.mel as mel


class RsAovGenerate(object):
    def __init__(self):
        self.idArr = None
        self.aovArr = None
        if cmds.window('myRsAovWindow', q=1, exists=1):
            cmds.deleteUI('myRsAovWindow')
        self.myWin = cmds.window('myRsAovWindow', t=u'创建ID')
        self.myColLayout = cmds.columnLayout(cat=['both', 12], rowSpacing=8, columnWidth=200, adjustableColumn=1)
        self.myIntSlider = cmds.intSliderGrp(l=u'起始ID :', v=1001, f=1, minValue=0, maxValue=99999, h=30,cw3=[50, 50, 100])
        self.myTextField = cmds.textFieldGrp(label=u'P什么什么命名:', cw2=[80, 120])
        self.myRadioBtn = cmds.radioButtonGrp(nrb=2, la2=[u'按模型分', u'按着色组分'], sl=2, cal=[1, 'left'], w=200,
                                              cw2=[100, 100], h=30)
        # self.myRowLayout = cmds.rowLayout(nc=3, columnWidth3=[60, 60, 60], h=30, cl3=["left", "right", "center"])
        # self.myBtn1 = cmds.button(l=u'检查', w=100, c=lambda *args: self.check1())
        self.myBtn2 = cmds.button(l=u'创建', w=100,h=30,
                                  c=lambda *args: self.run(cmds.intSliderGrp(self.myIntSlider, q=1, v=1),
                                                           cmds.textFieldGrp(self.myTextField, q=1, tx=1)))
        # self.myBtn3 = cmds.button(l=u'撤销', w=100,
        #                           c=lambda *args: self.run(cmds.intSliderGrp(self.myIntSlider, q=1, v=1),
        #                                                    cmds.textFieldGrp(self.myTextField, q=1, tx=1), remove=True))
        cmds.setParent('..')
        # self.myRowLayout2 = cmds.rowLayout(nc=3, columnWidth3=[145, 145, 145], h=30, cl3=["left", "right", "center"])
        # self.myBtn5 = cmds.button(l='ˢ����Ⱦ���', w=100, c="mel.eval('redshiftCreateAovTab')")

        cmds.showWindow(self.myWin)
        cmds.window(self.myWin, e=1, w=200, h=150, sizeable=True)


    def check1(self):
        start = self.getIDStart()
        if cmds.radioButtonGrp(self.myRadioBtn, q=1, sl=1) == 1:
            sel = cmds.ls(sl=1)
            num = len(sel)
            color = ([0.267, 0.267, 0.267], [0.3, 0.3, 0.8], [0.8, 0.6, 0.1], [0.9, 0.1, 0.1])
            msg = u'ѡ%d%dID%d层AOV;\nID范围:%d----%d' % (
            num, num, (num - 1) / 3 + 1, start, start + num)
            if num < 10:
                cmds.confirmDialog(m=msg, button=u'心里有点B数了吧', bgc=color[0])
            elif num < 20:
                cmds.confirmDialog(m=msg, button=u'心里有点B数了吧', bgc=color[1])
            elif num < 40:
                cmds.confirmDialog(m=msg, button=u'心里有点B数了吧', bgc=color[2])
            else:
                cmds.confirmDialog(m=msg, button=u'心里有点B数了吧', bgc=color[3])
        else:
            num = len(self.getMatSGArr())
            msg = u'ѡ%d%dID%d层AOV;\nID范围:%d----%d' % (
            num, num, (num - 1) / 3 + 1, start, start + num)
            cmds.confirmDialog(m=msg, button=u'心里有点B数了吧')



    def getTex(self):
        return cmds.textFieldGrp(self.myTextField, q=1, tx=1)

    def getIDStart(self):
        return cmds.intSliderGrp(self.myIntSlider, q=1, v=1)

    def createAov(self, number, aovName='jgb'):
        index = 1
        aovArr = []
        if number == 1:
            number = 1
        else:
            number = (number - 1) / 3 + 1
        for i in range(number):
            tmp = cmds.rsCreateAov(type='Puzzle Matte')
            aovName1 = aovName + "_PM_" + str(index)
            cmds.setAttr(tmp + '.name', aovName1, type='string')
            if cmds.radioButtonGrp(self.myRadioBtn, q=1, select=1) == 1:
                cmds.setAttr(tmp + '.mode', 1)
            aovArr.append(tmp)
            index += 1
        # mel.eval('redshiftCreateAovTab')
        mel.eval('redshiftUpdateActiveAovList')
        return aovArr

    def createID(self, startVaule=1001):
        idArr = []
        sel = cmds.ls(sl=1)
        idNum = len(sel)
        idVauleArr = []
        for i in sel:
            cmds.select(i)
            rsObjId = mel.eval('redshiftCreateObjectIdNode()')
            setName = self.getTex()+"_ID_"+str(int(self.getIDStart())+sel.index(i))

            idArr.append(cmds.rename(rsObjId, setName))

        for i in idArr:
            cmds.setAttr(i + '.objectId', startVaule)
            idVauleArr.append(startVaule)
            startVaule += 1
        cmds.select(sel)
        return idNum, idVauleArr, idArr


    def setAovID(self, idVauleArr, aovArr):
        index = 0
        for i in aovArr:
            cmds.setAttr(i + '.redId', idVauleArr[index])
            index += 1
            if index == len(idVauleArr):
                return
            cmds.setAttr(i + '.greenId', idVauleArr[index])
            index += 1
            if index == len(idVauleArr):
                return
            cmds.setAttr(i + '.blueId', idVauleArr[index])
            index += 1
            if index == len(idVauleArr):
                return


    def run(self, startVaule, aovName, remove=False):
        model = cmds.radioButtonGrp(self.myRadioBtn, q=1, sl=1)

        if model == 1:
            if remove == False:
                if self.getTex() == '':
                    cmds.confirmDialog(m=u'来个名字', button=u'知道了')
                    return

                idNum, idVauleArr, self.idArr = self.createID(startVaule)
                self.aovArr = self.createAov(idNum, self.getTex())
                self.setAovID(idVauleArr, self.aovArr)
            if remove == True:
                if self.idArr != None:
                    if self.aovArr != None:
                        cmds.delete(self.idArr)
                        cmds.delete(self.aovArr)
        else:
            if remove == True:
                if self.aovArr != None:
                    # cmds.delete(self.idArr)
                    cmds.delete(self.aovArr)
                    return
            matID_arr = self.mat_ID(startVaule)
            self.aovArr = self.createAov(len(matID_arr), aovName)
            self.setAovID(matID_arr, self.aovArr)

    # �ֲ���ID
    def getSG(self):
        # ѡ��SG�ڵ�
        tmp = cmds.ls(sl=1)
        sgs = cmds.ls(sl=1, type='shadingEngine')
        if sgs != []:
            return sgs
        # ѡ������
        '''
        mats = cmds.hyperShade(smn=1)
        selMats = cmds.ls(sl=1)
        cmds.select(tmp)
        sgs = cmds.listConnections(selMats, t='shadingEngine')
        '''
        geo = cmds.ls(sl=1, dag=1, type='mesh')
        sgs = cmds.listConnections(geo, type='shadingEngine')
        return sgs

    # �ֲ���ID
    def getMatSGArr(self):
        # ȥ�ظ�
        selSgSet = self.getSG()
        #  selSgSet[0][0]
        return self.quchong(selSgSet)

    def mat_ID(self, startVaule):
        mat_IdNumbs = []
        selSgSet = self.getMatSGArr()
        if 'initialShadingGroup' in selSgSet:
            selSgSet.remove('initialShadingGroup')
        if 'initialParticleSE' in selSgSet:
            selSgSet.remove('initialParticleSE')
        for i in selSgSet:
            #            if cmds.getAttr(i+'.rsMaterialId') !=0:
            cmds.setAttr(i + '.rsMaterialId', startVaule)
            mat_IdNumbs.append(startVaule)
            startVaule += 1

        return mat_IdNumbs


    def quchong(self, arr):
        newArr = []
        for i in arr:
            if i not in newArr:
                newArr.append(i)
        return newArr


bb = RsAovGenerate()
