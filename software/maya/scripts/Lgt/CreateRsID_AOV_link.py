# -*- coding: UTF-8 -*-
# .@FileName:ModelClean_link
# .@Date:2019-03-15:18:53
# .@Aurhor:LuoOu
import maya.cmds as cmds
import pymel.core as pm
import sys
import os


def main(*args):
    cmds.about(windows=1)
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("LGT", "ScriptPackages")
    scriptsPath = scriptsPath.replace('\\', r'/')
    CreateRsID_AOVPath = scriptsPath + r'/LGT/CreateRsID_AOV'
    pm.python("execfile(r" + "\"" + str(scriptsPath) + "/LGT/CreateRsID_AOV/CreateRsID_AOV.py" + "\"" + ")")

    if cmds.about(windows=1):
        CreateRsID_AOV = CreateRsID_AOVPath.replace(r'/', '\\')
    else:
        pass

    if CreateRsID_AOV not in sys.path:
        sys.path.insert(0, CreateRsID_AOV)

    try:
        import CreateRsID_AOV

    except:
        cmds.error('the CreateRsID_AOV folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    reload(CreateRsID_AOV)
