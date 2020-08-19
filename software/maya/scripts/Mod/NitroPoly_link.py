# -*- coding: UTF-8 -*-
#.@FileName:ModelClean_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import maya.cmds as cmds
import pymel.core as pm
import sys
import os

def main(*args):
    cmds.about(windows=1)
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Mod", "ScriptPackages")
    scriptsPath = scriptsPath.replace('\\', r'/')
    NitroPolyPath = scriptsPath + r'/Mod/NitroPoly'
    pm.python("execfile(r" + "\"" + str(scriptsPath) + "/Mod/NitroPoly/NitroPoly.py" + "\"" + ")")

    if cmds.about(windows=1):
        NitroPoly = NitroPolyPath.replace(r'/', '\\')
    else:
        pass

    if NitroPoly not in sys.path:
        sys.path.insert(0, NitroPoly)

    try:
        import NitroPoly

    except:
        cmds.error('the NitroPoly folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    reload(NitroPoly)
    NitroPoly.main()
    