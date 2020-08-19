#-*-coding:utf-8-*-
 
from maya import OpenMayaUI as omui
import maya.cmds as cmds
import maya.mel as mel
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
 
import Ui_Batch_attrManager #加载编译成Py的.ui文件
 
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)#获得Maya主窗口
 
class Form_Main(QMainWindow,Ui_Batch_attrManager.Ui_Form_Main):#继承编译好的.py类
    def __init__(self,*args, **kwargs):
        super(Form_Main, self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)#将新窗口设置为maya的子级
        self.setWindowFlags(Qt.Window)
        self.setupUi(self)#运行父类初始化方法
        # self.connectSignals()
 
#这里是RS代理的General的槽函数
    @Slot()
    def on_radioButton_FromScene_clicked(self):
        """
        Slot documentation goes here.
        """
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        ALLProxyMeshLIST = cmds.ls(sl=1)
        for esy in ALLProxyMeshLIST:
            cmds.setAttr((str(esy) + ".materialMode"), 1)
        print  ("FromScene")
        cmds.select(ALLProxyMeshLIST)
    
    @Slot()
    def on_radioButton_FromProxy_clicked(self):
        """
        Slot documentation goes here.
        """
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        ALLProxyMeshLIST = cmds.ls(sl=1)
        for esy in ALLProxyMeshLIST:
            cmds.setAttr((str(esy) + ".materialMode"), 0)
        print  ("FromProxy")
        cmds.select(ALLProxyMeshLIST)
        
  
    @Slot()
    def on_radioButton_PreviewMesh_clicked(self):
        """
        Slot documentation goes here.
        """
        # xyl_rs_xfobjlist = cmds.ls(dag=1, type='RedshiftProxyMesh', sl=1)
        # xyl_rs_xf_onesp = ""
        # for xyl_rs_xf_onesp in xyl_rs_xfobjlist:
        #     print str(xyl_rs_xf_onesp) + "\n"
        #     cmds.setAttr((str(xyl_rs_xf_onesp) + ".displayMode"), 1)
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        ALLProxyMeshLIST = cmds.ls(sl=1)
        for esy in ALLProxyMeshLIST:
            cmds.setAttr((str(esy) + ".displayMode"), 1)
        print  ("PreviewMesh")
        cmds.select(ALLProxyMeshLIST)
        
    @Slot()
    def on_radioButton_BoundingBox_clicked(self):
        """
        Slot documentation goes here.
        """
        cmds.select(cmds.ls(type="RedshiftProxyMesh"))
        ALLProxyMeshLIST = cmds.ls(sl=1)
        for esy in ALLProxyMeshLIST:
	        cmds.setAttr((str(esy) + ".displayMode"), 0)
        print  ("BoundingBox")
        cmds.select(ALLProxyMeshLIST)
        
    @Slot()
    def on_checkBox_RPMDISL_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RPMDISL.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".displayMode")
            cmds.select(ALLProxyMeshLIST)
            print ("Create Layer Override")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".displayMode", remove=1)
            cmds.select(ALLProxyMeshLIST)
            print ("Remove Layer Override")
            
    @Slot()
    def on_checkBox_RPMMATL_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RPMMATL.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".materialMode")
            cmds.select(ALLProxyMeshLIST)
            print ("Create Layer Override")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".materialMode", remove=1)
            cmds.select(ALLProxyMeshLIST)
            print ("Remove Layer Override")
            
#这里是RS代理的Override的槽函数
    @Slot()
    def on_checkBox_RMOBJ_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMOBJ.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".objectIdMode"), 1)
            cmds.select(ALLProxyMeshLIST)
            print ("NO")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".objectIdMode"), 0)
            cmds.select(ALLProxyMeshLIST)
            print ("OFF")
            
    @Slot()      
    def on_checkBox_RMOBJL_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMOBJL.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".objectIdMode")
            cmds.select(ALLProxyMeshLIST)
            print ("Create Layer Override")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".objectIdMode", remove=1)
            cmds.select(ALLProxyMeshLIST)
            print ("Remove Layer Override")
            
    @Slot()
    def on_checkBox_RMTES_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMTES.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".tessellationMode"), 1)
            cmds.select(ALLProxyMeshLIST)
            print ("NO")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".tessellationMode"), 0)
            cmds.select(ALLProxyMeshLIST)
            print ("OFF")
            
    @Slot()      
    def on_checkBox_RMTESL_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMTESL.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".tessellationMode")
            cmds.select(ALLProxyMeshLIST)
            print ("Create Layer Override")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".tessellationMode", remove=1)
            cmds.select(ALLProxyMeshLIST)
            print ("Remove Layer Override") 
            
            
    @Slot()
    def on_checkBox_RMUSE_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMUSE.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".userDataMode"), 1)
            cmds.select(ALLProxyMeshLIST)
            print ("NO")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".userDataMode"), 0)
            cmds.select(ALLProxyMeshLIST)
            print ("OFF")
            
    @Slot()      
    def on_checkBox_RMUSEL_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMUSEL.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".userDataMode")
            cmds.select(ALLProxyMeshLIST)
            print ("Create Layer Override")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".userDataMode", remove=1)
            cmds.select(ALLProxyMeshLIST)
            print ("Remove Layer Override") 
            
    @Slot()
    def on_checkBox_RMVIS_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMVIS.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".visibilityMode"), 1)
            cmds.select(ALLProxyMeshLIST)
            print ("NO")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.setAttr((str(esy) + ".visibilityMode"), 0)
            cmds.select(ALLProxyMeshLIST)
            print ("OFF")
            
    @Slot()      
    def on_checkBox_RMVISL_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkBox_RMVISL.isChecked() == True:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".visibilityMode")
            cmds.select(ALLProxyMeshLIST)
            print ("Create Layer Override")
        else:
            cmds.select(cmds.ls(type="RedshiftProxyMesh"))
            ALLProxyMeshLIST = cmds.ls(sl=1)
            for esy in ALLProxyMeshLIST:
                cmds.editRenderLayerAdjustment(str(esy) + ".visibilityMode", remove=1)
            cmds.select(ALLProxyMeshLIST)
            print ("Remove Layer Override") 
            
#这里是RSShape的attr的槽函数
    # def rsChannelBoxControl():
    

    def rsSwitch(x):
        list = [".rsObjectId",
            ".rsEnableVisibilityOverrides",
            ".rsPrimaryRayVisible",
            ".rsSecondaryRayVisible",
            ".rsShadowCaster",
            ".rsShadowReceiver",
            ".rsReflectionCaster",
            ".rsReflectionVisible",
            ".rsRefractionCaster",
            ".rsRefractionVisible",
            ".rsGiCaster",
            ".rsGiVisible",
            ".rsCausticCaster",
            ".rsCausticVisible",
            ".rsFgCaster",
            ".rsFgVisible",
            ".rsSelfShadows",
            ".rsAOCaster",
            ".rsForceBruteForceGI",
            ".rsMatteEnable",
            ".rsMatteApplyToSecondaryRays",
            ".rsMatteShowBackground",
            ".rsMatteAffectedByMatteLights",
            ".rsMatteAlpha",
            ".rsMatteReflectionScale",
            ".rsMatteRefractionScale",
            ".rsMatteDiffuseScale",
            ".rsMatteShadowEnable",
            ".rsMatteShadowAffectsAlpha",
            ".rsMatteShadowTransparency",
            ".rsMatteShadowColor",
            ".rsMatteShadowColorR",
            ".rsMatteShadowColorG",
            ".rsMatteShadowColorB",
            ".rsEnableSubdivision",
            ".rsScreenSpaceAdaptive",
            ".rsDoSmoothSubdivision",
            ".rsMinTessellationLength",
            ".rsMaxTessellationSubdivs",
            ".rsOutOfFrustumTessellationFactor",
            ".rsSubdivisionRule",
            ".rsEnableDisplacement",
            ".rsMaxDisplacement",
            ".rsDisplacementScale",
            ".rsAutoBumpMap",
            ".rsCausticReceiver",
            ".rsGiReceiver"]
        sel = cmds.listRelatives(cmds.ls(sl=1), s=1)
        if sel != None:
            for s in sel:
                for e in list:
                    cmds.setAttr(s + e, k=int(x))
                    cmds.setAttr(s + e, cb=int(x))
        else:
            print ("Please select Object(s) first!")
    
    
    @Slot()      
    def on_pushButton_RSHID_clicked(self):
        """
        Slot documentation goes here.
        """
        RSATTRlist = [".rsObjectId",
            ".rsEnableVisibilityOverrides",
            ".rsPrimaryRayVisible",
            ".rsSecondaryRayVisible",
            ".rsShadowCaster",
            ".rsShadowReceiver",
            ".rsReflectionCaster",
            ".rsReflectionVisible",
            ".rsRefractionCaster",
            ".rsRefractionVisible",
            ".rsGiCaster",
            ".rsGiVisible",
            ".rsCausticCaster",
            ".rsCausticVisible",
            ".rsFgCaster",
            ".rsFgVisible",
            ".rsSelfShadows",
            ".rsAOCaster",
            ".rsForceBruteForceGI",
            ".rsMatteEnable",
            ".rsMatteApplyToSecondaryRays",
            ".rsMatteShowBackground",
            ".rsMatteAffectedByMatteLights",
            ".rsMatteAlpha",
            ".rsMatteReflectionScale",
            ".rsMatteRefractionScale",
            ".rsMatteDiffuseScale",
            ".rsMatteShadowEnable",
            ".rsMatteShadowAffectsAlpha",
            ".rsMatteShadowTransparency",
            ".rsMatteShadowColor",
            ".rsMatteShadowColorR",
            ".rsMatteShadowColorG",
            ".rsMatteShadowColorB",
            ".rsEnableSubdivision",
            ".rsScreenSpaceAdaptive",
            ".rsDoSmoothSubdivision",
            ".rsMinTessellationLength",
            ".rsMaxTessellationSubdivs",
            ".rsOutOfFrustumTessellationFactor",
            ".rsSubdivisionRule",
            ".rsEnableDisplacement",
            ".rsMaxDisplacement",
            ".rsDisplacementScale",
            ".rsAutoBumpMap",
            ".rsCausticReceiver",
            ".rsGiReceiver"]
        sel = cmds.listRelatives(cmds.ls(sl=1), s=1)

        for s in sel:
            for e in RSATTRlist:
                cmds.setAttr(s + e, cb=int(0))


    @Slot()      
    def on_pushButton_RSSHO_clicked(self):
        """
        Slot documentation goes here.
        """
        RSATTRlist = [".rsObjectId",
            ".rsEnableVisibilityOverrides",
            ".rsPrimaryRayVisible",
            ".rsSecondaryRayVisible",
            ".rsShadowCaster",
            ".rsShadowReceiver",
            ".rsReflectionCaster",
            ".rsReflectionVisible",
            ".rsRefractionCaster",
            ".rsRefractionVisible",
            ".rsGiCaster",
            ".rsGiVisible",
            ".rsCausticCaster",
            ".rsCausticVisible",
            ".rsFgCaster",
            ".rsFgVisible",
            ".rsSelfShadows",
            ".rsAOCaster",
            ".rsForceBruteForceGI",
            ".rsMatteEnable",
            ".rsMatteApplyToSecondaryRays",
            ".rsMatteShowBackground",
            ".rsMatteAffectedByMatteLights",
            ".rsMatteAlpha",
            ".rsMatteReflectionScale",
            ".rsMatteRefractionScale",
            ".rsMatteDiffuseScale",
            ".rsMatteShadowEnable",
            ".rsMatteShadowAffectsAlpha",
            ".rsMatteShadowTransparency",
            ".rsMatteShadowColor",
            ".rsMatteShadowColorR",
            ".rsMatteShadowColorG",
            ".rsMatteShadowColorB",
            ".rsEnableSubdivision",
            ".rsScreenSpaceAdaptive",
            ".rsDoSmoothSubdivision",
            ".rsMinTessellationLength",
            ".rsMaxTessellationSubdivs",
            ".rsOutOfFrustumTessellationFactor",
            ".rsSubdivisionRule",
            ".rsEnableDisplacement",
            ".rsMaxDisplacement",
            ".rsDisplacementScale",
            ".rsAutoBumpMap",
            ".rsCausticReceiver",
            ".rsGiReceiver"]
        sel = cmds.listRelatives(cmds.ls(sl=1), s=1)

        for s in sel:
            for e in RSATTRlist:
                cmds.setAttr(s + e, cb=int(1))

                   
def main():
    ui = Form_Main()
    ui.show()
    print 'run OK'
    return ui
if __name__ == '__main__':

    main()