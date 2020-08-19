# -*- coding: UTF-8 -*-
#.@FileName:ezMel2Python_link
#.@Date:2019-03-15:13:33
#.@Aurhor:LuoOu
import maya.cmds as cmds
import sys
import shutil
import os

def main(*args):
    cmds.about(windows=1)
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Mod", "ScriptPackages")
    DW_MaterialManagerPath = scriptsPath + r'/Mod/DW_MaterialManager/'
    useprefspath = cmds.internalVar(usd = 1)
    presetsPATHExists = os.path.exists(useprefspath + r'DW_MaterialManager/presets/')
    if not presetsPATHExists:
        os.makedirs(useprefspath + r'DW_MaterialManager/presets/')
    UIdefaultPresetPath = DW_MaterialManagerPath + r'presets/UI_defaultPreset.json'
    UIlastPresetPath = DW_MaterialManagerPath + r'presets/UI_lastPreset.json'
    UIdefaultPresetuseprefspath = useprefspath + r'DW_MaterialManager/presets/UI_defaultPreset.json'
    UIlastPresetuseprefspath = useprefspath + r'DW_MaterialManager/presets/UI_lastPreset.json'
    shutil.copyfile(UIdefaultPresetPath, UIdefaultPresetuseprefspath)
    shutil.copyfile(UIlastPresetPath, UIlastPresetuseprefspath)

    # if the systerm is windows,then use \\ replace /
    if cmds.about(windows=1):
        DW_MaterialManagerPath = DW_MaterialManagerPath.replace(r'/', '\\')
    else:
        pass

    if DW_MaterialManagerPath not in sys.path:
        sys.path.insert(0, DW_MaterialManagerPath)

    try:
        import UI

    except:
        cmds.error('the DW_MaterialManager folder is placed wrong,the right path is : {0}'.format(scriptsPath))

    reload(UI)
    UI.UI()