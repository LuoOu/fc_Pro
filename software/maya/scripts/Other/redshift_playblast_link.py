# -*- coding: UTF-8 -*-
# .@FileName:redshift_playblast_link
# .@Date:2019-03-15:10:37
# .@Aurhor:LuoOu

import maya.cmds as cmds
import pymel.core as pm
import sys
import os
import json

def main(*args):
    cmds.about(windows=1)
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Other", "ScriptPackages").replace('\\', r'/')
    redshiftplayblastPath = scriptsPath + r'/Other/'

    # if the systerm is windows,then use \\ replace /
    if cmds.about(windows=1):
        redshiftplayblastPath = redshiftplayblastPath.replace(r'/', '\\')
    else:
        pass

    if redshiftplayblastPath not in sys.path:
        sys.path.insert(0, redshiftplayblastPath)

    try:
        from redshift_playblast.view import redshift_playblast_view

    except:
        cmds.error('the redshift_playblast folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    # reload(redshift_playblast)
    redshift_playblast_view.run_maya()
