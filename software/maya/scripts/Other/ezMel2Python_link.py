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
    redshiftplayblastPath = scriptsPath + r'/Other/ezMel2Python/'

    # if the systerm is windows,then use \\ replace /
    if cmds.about(windows=1):
        redshiftplayblastPath = redshiftplayblastPath.replace(r'/', '\\')
        print redshiftplayblastPath
    else:
        pass

    if redshiftplayblastPath not in sys.path:
        sys.path.insert(0, redshiftplayblastPath)

    try:
        import ezMel2Python

    except:
        cmds.error('the redshift_playblast folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    # reload(redshift_playblast)
    #redshift_playblast_view.run_maya()
    ezMel2Python.ezMel2Python()
