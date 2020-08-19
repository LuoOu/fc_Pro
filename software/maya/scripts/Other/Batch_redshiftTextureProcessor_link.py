# -*- coding: UTF-8 -*-
#.@FileName:Batch_redshiftTextureProcessor_link
#.@Date:2019-03-15:10:37
#.@Aurhor:LuoOu

import maya.mel as mel
import os

def main(*args):
    script = os.path.realpath(__file__)
    scripts_dir = os.path.dirname(script)
    scriptsPath = scripts_dir.replace("Other", "ScriptPackages").replace('\\', r'/')
    mel.eval('source "{}/Other/Batch_redshiftTextureProcessor/Batch_redshiftTextureProcessor.mel";'.format(scriptsPath))

