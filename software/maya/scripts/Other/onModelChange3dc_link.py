# -*- coding: UTF-8 -*-
#.@FileName:autoPlacePivot_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import maya.cmds as cmds
import pymel.core as pm
import sys
import os


def main(*args):
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    cmds.about(windows=1)
    scriptsPath = scripts_dir.replace("Other", "ScriptPackages")
    onModelChange3dcPath = scriptsPath + r'/Other/onModelChange3dc'
    pm.python("execfile(r" + "\"" + str(scriptsPath) + "/Other/onModelChange3dc/onModelChange3dc.py" + "\"" + ")")

    if cmds.about(windows=1):
        onModelChange3dc = onModelChange3dcPath.replace(r'/', '\\')
    else:
        pass

    if onModelChange3dc not in sys.path:
        sys.path.insert(0, onModelChange3dc)

    try:
        import onModelChange3dc

    except:
        cmds.error('the onModelChange3dc folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    reload(onModelChange3dc)
    onModelChange3dc.onModelChange3dc()