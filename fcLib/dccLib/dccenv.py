# -*- coding: UTF-8 -*-
#.@FileName:dccenv
#.@Date:2020-06-28:10:11
#.@Aurhor:LuoOu
import os
from fcLib.fileLib import folder
from fcLib.tankLib.configLib import Tank

def setup_env(software):
    os.environ['SOFTWARE'] = software
    _software_data = Tank().data_software
    _version = _software_data['version']
    _path = _software_data['path']

    # LOG.debug('- {} -----------------------------------------------------'.format(self._NAME.upper()))

    sub_path = []
    software_path = []

    for each_path in os.environ['SOFTWARE_SRC_PATH'].split(';'):
        # if not each_path.endswith('software'): each_path = os.path.dirname(each_path)
        tmp_paths = ('\\').join([each_path, software])
        software_path.append(tmp_paths)
        tmp_folder = folder.get_file_list(path=tmp_paths, exclude='.py', add_path=True)
        if not tmp_folder:
            continue
        sub_path.extend(tmp_folder)
    os.environ['SOFTWARE_PATH'] = (';').join(software_path)
    os.environ['SOFTWARE_SUB_PATH'] = (';').join(sub_path)
    # LOG.debug("SOFTWARE_PATH: {}".format(os.environ['SOFTWARE_PATH']))

    # GET config
    _software_data = Tank().data_software
    _env = _software_data['ENV']
    # ADD software ENV
    if (_env):
        for env, content in _env.iteritems():
            if isinstance(content, list):
                for each in content: Tank().add_env(env, each)
            else:
                Tank().add_env(env, content)