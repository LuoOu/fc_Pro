# -*- coding: UTF-8 -*-
#.@FileName:exportABC
#.@Date:2019-11-06:14:13
#.@Aurhor:LuoOu
import os
import sys

# maya_location = os.path.normpath('C:/Program Files/Autodesk/Maya2017')
# python_maya_location = os.path.normpath("C:/Program Files/Autodesk/Maya2017/Python")
# maya_bin_location = os.path.normpath('C:/Program Files/Autodesk/Maya2017/bin')
#
# os.environ['MAYA_LOCATION'] = maya_location  # add maya location as a environment variable
# os.environ["PYTHONHOME"] = python_maya_location
# os.environ["PATH"] = maya_bin_location + ';' + os.environ["PATH"]

# Others

sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib/site-packages/setuptools-0.6c9-py2.6.egg")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib/site-packages/pymel-1.0.0-py2.6.egg")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib/site-packages/ipython-0.10.1-py2.6.egg")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib/site-packages/ply-3.3-py2.6.egg")
sys.path.append("C:/Program Files/Autodesk/Maya2017/bin/python26.zip")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/DLLs")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib/plat-win")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib/lib-tk")
sys.path.append("C:/Program Files/Autodesk/Maya2017//bin")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python")
sys.path.append("C:/Program Files/Autodesk/Maya2017/Python/lib/site-packages")

import maya.standalone as sta
import maya.cmds as cmds

sta.initialize(name='python')

def expabc():
    print 'start'
    filepath = sys.argv[1]
    outpath =sys.argv[2]
    cmds.file(filepath, open=True)
    print cmds.ls(type="mesh")

expabc()