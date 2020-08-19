# -*- coding: UTF-8 -*-
#.@FileName:ModelClean_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import maya.mel as mel
import maya.cmds as cmds

modlePath = cmds.getModulePath(moduleName='LuoOu_tools')

def main(*args):
    mel.eval('source "{}/scripts/ScriptPackages/Model/ModelCleaner";asModelCleaner'.format(modlePath))


