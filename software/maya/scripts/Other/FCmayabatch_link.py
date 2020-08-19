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
    FCmayabatchPath = scriptsPath + r'/Other/FCmayabatch'

    # if the systerm is windows,then use \\ replace /
    if cmds.about(windows=1):
        FCmayabatchPath = FCmayabatchPath.replace(r'/', '\\')
    else:
        pass

    if FCmayabatchPath not in sys.path:
        sys.path.insert(0, FCmayabatchPath)

    try:
        import FCmayabatch

    except:
        cmds.error('the FCmayabatch folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    reload(FCmayabatch)
    FCmayabatch.main()