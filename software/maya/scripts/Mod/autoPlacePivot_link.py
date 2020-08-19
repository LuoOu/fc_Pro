# -*- coding: UTF-8 -*-
#.@FileName:autoPlacePivot_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import maya.cmds as cmds
import pymel.core as pm
import sys
import os


def main(*args):
    print "ok"
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    cmds.about(windows=1)
    scriptsPath = scripts_dir.replace("Mod", "ScriptPackages")
    autoPlacePivotPath = scriptsPath + r'/Mod/autoPlacePivot'
    pm.python("execfile(r" + "\"" + str(scriptsPath) + "/Mod/autoPlacePivot/autoPlacePivot.py" + "\"" + ")")

    if cmds.about(windows=1):
        autoPlacePivot = autoPlacePivotPath.replace(r'/', '\\')
    else:
        pass

    if autoPlacePivot not in sys.path:
        sys.path.insert(0, autoPlacePivot)

    try:
        import autoPlacePivot

    except:
        cmds.error('the autoPlacePivot folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    reload(autoPlacePivot)
    autoPlacePivot.autoPlacePivot()
    