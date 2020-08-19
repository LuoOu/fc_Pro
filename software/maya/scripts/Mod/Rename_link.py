# -*- coding: UTF-8 -*-
#.@FileName:Rename_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import maya.mel as mel
import os
import maya.cmds as cmds

def main(*args):
    cmds.about(windows=1)
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Mod", "ScriptPackages/Mod/Rename").replace('\\',r'/')
    mel.eval('source "{}"'.format(scriptsPath))



