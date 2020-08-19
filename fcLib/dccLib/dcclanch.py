# -*- coding: UTF-8 -*-
#.@FileName:dcclanch
#.@Date:2020-06-24:12:38
#.@Aurhor:LuoOu
import os
import subprocess
from fcLib.tankLib.configLib import Tank
from fcLib.dccLib import dccenv

def start(software, open_file=''):
    dccenv.setup_env(software)
    os.environ['SOFTWARE'] = software

    software_data = Tank().data_software
    cmd = software_data['start'].format(open_file)

    if open_file:
        if software == 'maya':
            cmd = '{} -file "{}"'.format(cmd, open_file)
        elif software == 'max' or software == 'houdini':
            cmd = '"{}" "{}"'.format(cmd, open_file)
    subprocess.Popen(cmd, shell=True, env=os.environ)


