# -*- coding: UTF-8 -*-
#.@FileName:launch
#.@Date:2020-06-22:15:55
#.@Aurhor:LuoOu

import os
import sys

try:
    import yaml
except:
    yaml_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(yaml_path + "/fcLib/site-packages")
    import yaml


#*********************************************************************
class Setup(object):

    def __init__(self):
        this_path = os.path.normpath(os.path.dirname(__file__))
        self.data_pipeline_path = []
        self.data_project_path  = os.path.normpath(('/').join([this_path.replace("Launch", "config"), 'pipeline.yml']))

        self.pipeline_env  = SmartDict()
        self.this_pipeline = os.path.normpath(os.path.dirname(this_path))

        # LOAD pipeline config
        if os.path.exists(self.data_project_path):
            with open(self.data_project_path, 'r') as stream:
                try:
                    self.pipeline_data = yaml.load(stream)
                except yaml.YAMLError as exc:
                    raise OSError ('STOP PROCESS', 'DATA file is corrupted', exc)
        else:
            raise OSError ('STOP PROCESS', 'PATH doesnt exist', self.data_project_path)

        # SEARCH and ADD current and sub paths
        for pipe in self.pipeline_data['PATH']:

            for status, path in pipe.items():
                # REPLACE $this with current_path
                if path == '$this':
                    path = self.this_pipeline

                if path and self.this_pipeline == path or self.data_pipeline_path:
                    if os.path.exists(path):
                        self.data_pipeline_path.append(path)
                        self.pipeline_status = status
                    else:
                        print('PIPELINE_PATH doesnt exist: {}\nSOURCE[PATH]: {}'.format(path, self.data_project_path))

        if not self.data_pipeline_path:
            raise OSError ('STOP PROCESS', 'PATH doesnt exist in config/pipeline.yml', self.this_pipeline)

        for packages in self.pipeline_data['PRO_PACKAGES']:
            for p, path in packages.items():
                if p == "packages":
                    self.pro_packages = path



        self.set_pipeline_env()



    def set_pipeline_env(self):

        # SET STATUS
        os.environ['PIPELINE_STATUS'] = self.pipeline_status
        os.environ['PRO_PACKAGES'] = self.pro_packages

        # ADD sub ENV
        for eachPath in self.data_pipeline_path:
            self.pipeline_env.add('PIPELINE_PATH', eachPath)

            if os.path.exists(eachPath + '/img'):        self.pipeline_env.add('IMG_PATH', eachPath + '/img')
            if os.path.exists(eachPath + '/software'):   self.pipeline_env.add('SOFTWARE_PATH', eachPath + '/software')
            if os.path.exists(eachPath + '/fcLib'):        self.pipeline_env.add('LIB_PATH', eachPath + '/fcLib')

            if os.path.exists(eachPath + '/fcLib/appLib'):   self.pipeline_env.add('APPS_PATH', eachPath + '/fcLib/appLib')
            if os.path.exists(eachPath + '/fcLib/site-packages'): self.pipeline_env.add('PACKAGES_PATH', eachPath + '/fcLib/site-packages')
            if os.path.exists(eachPath + '/fcLib/dccLib'):    self.pipeline_env.add('DCC_PATH', eachPath + '/fclib/dccLib')

        os.environ['CONFIG_PATH'] = self.data_pipeline_path[0] + '/config'
        # os.environ['DATA_PROJECT_PATH'] = self.data_pipeline_path[0] + '/config/project/' + self.pipeline_data['project']

        # ADD code env

        # ADD all pipeline env
        self.add_env('PIPELINE_PATH', (';').join(self.pipeline_env['PIPELINE_PATH']))
        try:
            self.add_env('IMG_PATH',     (';').join(self.pipeline_env['IMG_PATH']))
            self.add_env('LIB_PATH',     (';').join(self.pipeline_env['LIB_PATH']))
            self.add_env('APPS_PATH',    (';').join(self.pipeline_env['APPS_PATH']))
            self.add_env('PACKAGES_PATH',  (';').join(self.pipeline_env['PACKAGES_PATH']))
            self.add_env('DCC_PATH',     (';').join(self.pipeline_env['DCC_PATH']))

            self.add_env('SOFTWARE_PATH',     (';').join(self.pipeline_env['SOFTWARE_PATH']))
            self.add_env('SOFTWARE_SRC_PATH', (';').join(self.pipeline_env['SOFTWARE_PATH']))
        except: raise OSError ('STOP PROCESS', 'PATH doesnt exist in config/pipeline.yml', self.this_pipeline)





        sys.path.append(os.environ['PIPELINE_PATH'])
        sys.path.append(os.environ['IMG_PATH'] )
        sys.path.append(os.environ['LIB_PATH'])
        sys.path.append(os.environ['APPS_PATH'])
        sys.path.append(os.environ['DCC_PATH'])
        sys.path.append(os.environ['SOFTWARE_PATH'] )
        sys.path.append(os.environ['CONFIG_PATH'])
        # sys.path.append(os.environ['DATA_PROJECT_PATH'])


        self.add_env('PYTHONPATH', os.environ['IMG_PATH'])
        self.add_env('PYTHONPATH', os.environ['LIB_PATH'])
        self.add_env('PYTHONPATH', os.environ['APPS_PATH'])
        self.add_env('PYTHONPATH', os.environ['PACKAGES_PATH'])

        self.add_env('PYTHONPATH', os.environ['PIPELINE_PATH'])

        # # DATA ENV
        # os.environ['DATA_USER_PATH']      = self.data_pipeline_path[0] + '/config/user/' + getpass.getuser()
        # os.environ['DATA_USER_OVERWRITE'] = str(self.pipeline_data['user_data'])
        # sys.path.append(os.environ['DATA_USER_PATH'])

        # SET project Data
        from fcLib.tankLib.configLib import Tank

        self.project_data = Tank().data_project

        os.environ['PROJECT_NAME'] = self.project_data['name']
        # SET tier Data
        os.environ['MODULE'] = ''
        os.environ['CLASS'] = ''
        os.environ['ENTITY'] = ''
        os.environ['STEP'] = ''
        os.environ['TASK'] = ''
        os.environ['VARIANT'] = ''
        os.environ['VERSION'] = ''

        # ADD project path
        if os.path.exists(self.project_data['FC_SERVER_ROOT']):
            os.environ['FC_SERVER_ROOT'] = os.path.normpath(self.project_data['FC_SERVER_ROOT'])
        else:
            os.environ['FC_SERVER_ROOT'] = ''

        if os.path.exists(self.project_data['FC_LOCAL_ROOT']):
            os.environ['FC_LOCAL_ROOT'] = os.path.normpath(self.project_data['FC_LOCAL_ROOT'])
        else:
            os.environ['FC_LOCAL_ROOT'] = ''
        #
        # OS & PYTHON_VERSION
        os.environ['OS'] = sys.platform
        os.environ['PYTHON_VERSION'] = sys.version[:3]


    def add_env(self, var, content):
        content = os.path.normpath(content)
        if     os.environ.__contains__(var):
            os.environ[var] += ('').join([';', content])
        else:
            os.environ[var] = content
        return os.getenv(var)






#*********************************************************************
# CLASS
class SmartDict(dict):
    def __init__(self):
        super(dict)
        self = dict()

    def add(self, key, value):
        value = os.path.normpath(value)
        if self.has_key(key): self[key].append(value)
        else:                 self[key] = [value]

    def __missing__(self, key):
        return key



#*********************************************************************
# START
import argparse

parser = argparse.ArgumentParser(description='Setup your pipeline and start scripts.')
parser.add_argument('-so','--software', help='add software: nuke')
parser.add_argument('-p', '--proxy', action='store_true')

args = parser.parse_args()
args.software ='desktop'
Setup()
# print os.getenv('PACKAGES_PATH')
from fcLib.appLib import fcDesktop

fcDesktop.start()


