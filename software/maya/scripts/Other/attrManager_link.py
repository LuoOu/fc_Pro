# -*- coding: UTF-8 -*-
#.@FileName:ezMel2Python_link
#.@Date:2019-03-15:13:33
#.@Aurhor:LuoOu

import maya.cmds as cmds
import sys
import os

def main(*args):
    cmds.about(windows=1)
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Other", "ScriptPackages").replace('\\', r'/')
    attrManagerPath = scriptsPath + r'/Other/attrManager'

    # if the systerm is windows,then use \\ replace /
    if cmds.about(windows=1):
        attrManagerPath = attrManagerPath.replace(r'/', '\\')
    else:
        pass

    if attrManagerPath not in sys.path:
        sys.path.insert(0, attrManagerPath)

    try:
        import attrManager

    except:
        cmds.error('the attrManager folder is placed wrong,the right path is : {0}'.format(attrManagerPath))

    reload(attrManager)
    attrManager.attrManager()
    # print "ok"
    # attrManager.attrManager()
