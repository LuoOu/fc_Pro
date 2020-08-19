# -*- coding: UTF-8 -*-
#.@FileName:ModelClean_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import maya.cmds as cmds
import pymel.core as pm
import os
import os.path


def main(*args):
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    cmds.about(windows=1)
    scriptsPath = scripts_dir.replace("ANI", "ScriptPackages").replace('\\', r'/')
    pm.mel.source('{}/ANI/MG-PickerStudio/MGPicker_Program/MGPicker_WrittenByMiguel.mel'.format(scriptsPath))
    pm.mel.MG_PickerStudio(1)
    