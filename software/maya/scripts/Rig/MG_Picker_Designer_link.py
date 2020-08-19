# -*- coding: UTF-8 -*-
#.@FileName:MG_Picker_Designer_link
#.@Date:2019-03-15:18:53
#.@Aurhor:LuoOu
import pymel.core as pm
import maya.mel as mel
import os


def main(*args):
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("RIG", "ScriptPackages").replace('\\', r'/')
    pm.mel.source('{}/ANI/MG-PickerStudio/MGPicker_Program/MGPicker_WrittenByMiguel.mel'.format(scriptsPath))
    pm.mel.MG_PickerStudio(0)
    