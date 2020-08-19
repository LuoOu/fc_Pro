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
    scriptsPath = scripts_dir.replace("Mod", "ScriptPackages")
    WindCyclePath = scriptsPath + r'/Mod/GeometryCache_WindCycle'
    pm.python("execfile(r" + "\"" + str(scriptsPath) + "/Mod/GeometryCache_WindCycle/GeometryCache_WindCycle.py" + "\"" + ")")

    if cmds.about(windows=1):
        WindCycle = WindCyclePath.replace(r'/', '\\')
    else:
        pass

    if WindCycle not in sys.path:
        sys.path.insert(0, WindCycle)

    try:
        import GeometryCache_WindCycle

    except:
        cmds.error('the GeometryCache_WindCycle folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    reload(GeometryCache_WindCycle)
    GeometryCache_WindCycle.GeometryCache_WindCycle()
    