# -*- coding: UTF-8 -*-
#.@FileName:dcclaunch
#.@Date:2020-06-24:09:29
#.@Aurhor:LuoOu
import os
import subprocess

def start_dcc(software, open_file=''):


    # self.setup()
    # self.setup_env()
    # print self._software_data
    # cmd = self._software_data['start'].format(open_file)
    # print cmd
    #
    # if open_file:
    #     if self._NAME == 'maya':
    #         cmd = '{} -file "{}"'.format(cmd, open_file)
    #     elif self._NAME == 'max' or self._NAME == 'houdini':
    #         cmd = '"{}" "{}"'.format(cmd, open_file)
    # print os.environ
    cmd = 'start "" "C:/Program Files/Autodesk/Maya2019/bin/maya.exe"'
    # os.startfile("C:/Program Files/Autodesk/Maya2019/bin/maya.exe")
    subprocess.Popen(cmd, shell=True, env=os.environ)

start_dcc("maya")