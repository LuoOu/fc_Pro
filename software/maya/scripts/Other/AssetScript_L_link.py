# -*- coding: UTF-8 -*-
#.@FileName:ezMel2Python_link
#.@Date:2019-03-15:13:33
#.@Aurhor:LuoOu

import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel
import sys
import os

def main(*args):
    cmds.about(windows=1)
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Other", "ScriptPackages").replace('\\', r'/')
    ManagerPath = scriptsPath + r'/Other/AssetScript'
    mel.eval('source "{}/scripts/open_load_maya_file_about.mel";'.format(ManagerPath))
    mel.eval('source "{}/scripts/openDir.mel";'.format(ManagerPath))
    pm.python("execfile(r" + "\"" + str(ManagerPath) + "/asset_GuanLi.py" + "\"" + ")")

    if cmds.about(windows=1):
        AssetScript = ManagerPath.replace(r'/', '\\')
    else:
        pass

    if AssetScript not in sys.path:
        sys.path.insert(0, AssetScript)

    try:
        import asset_GuanLi

    except:
        cmds.error('the DW_MaterialManager folder is placed wrong,the right path is : {0}'.format(ManagerPath))

    reload(asset_GuanLi)
    asset_GuanLi.CGStorm_Asset_Manage_UI()

