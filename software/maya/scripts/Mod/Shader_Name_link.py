# -*- coding: UTF-8 -*-
#.@FileName:ModelClean_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import maya.mel as mel
import os


def main(*args):
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Mod", "ScriptPackages").replace('\\',r'/')
    mel.eval('source "{}/Mod/Shader_Name"'.format(scriptsPath))


