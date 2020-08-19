# -*- coding: UTF-8 -*-
#.@FileName:configLib
#.@Date:2020-06-22:16:07
#.@Aurhor:LuoOu

#*********************************************************************
# content   = main hub
# version   = 0.1.0
# date      = 2019-10-06
#
# license   = MIT <https://github.com/alexanderrichtertd>
# author    = Alexander Richter <alexanderrichtertd.com>
#*********************************************************************

import os

import yaml

# from pipLib import pipefunc

#*********************************************************************
# VARIABLES
TITLE = os.path.splitext(os.path.basename(__file__))[0]

DATA_FORMAT = '.yml'



class Tank(object):

    # _software = ''
    #
    # def init_software(self, software=''):
    #     print "fcok"
    #     if not software:
    #         software = os.getenv('SOFTWARE')
    #
    #     if not self._software:
    #         if software == 'maya':
    #             from fcLib.dccLib.maya_dcc import Maya
    #             print "fcok2"
    #             self._software = Maya()
    #         elif software == 'max':
    #             from fcLib.dccLib.max_dcc import Max
    #             self._software = Max()
    #         elif software == 'nuke':
    #             from fcLib.dccLib.nuke_dcc import Nuke
    #             self._software = Nuke()
    #         elif software == 'houdini':
    #             from fcLib.dccLib.houdini_dcc import Houdini
    #             self._software = Houdini()
    #         else:
    #             from fcLib.dccLib.software import Software
    #             self._software = Software()
    #     return self._software
    #
    # @property
    # def software(self):
    #     return self.init_software()





    @property
    def data(self):
        return self.get_data()

    @property
    def data_project(self):
        return self.get_data('project')

    @property
    def data_software(self):
        return self.get_data('dcc/{}'.format(os.getenv('SOFTWARE')))

    @property
    def data_script(self):
        return self.get_data('script')

    @property
    def data_notice(self):
        return self.get_data('notice')


    #*********************************************************************
    # GET ANDDATA
    def get_data(self, file_name=''):

        file_name = file_name.split('.')[0]
        file_name = file_name.lower()
        file_path = os.environ['PIPELINE_PATH'] +"/config/"+file_name + DATA_FORMAT


        # OPEN config path
        if os.path.exists(file_path):
            return self.get_yml_file(file_path)

        else:
            print('CANT find file: {}'.format(file_path))
        return ''


    #*********************************************************************
    # PATH
    def get_pipeline_path(self, end_path):
        pipeline_path = os.getenv('PIPELINE_PATH')
        if not pipeline_path: return

        pipeline_path = pipeline_path.split(';')
        # find first fitting path
        for eachPath in pipeline_path:
            path = os.path.normpath(('/').join([eachPath,end_path]))

            if os.path.exists(path):
                return path

        return ''

    # def get_img_path(self, end_path='btn/default'):
    #     if '.' in end_path:
    #         img_format = ''
    #     else:
    #         img_format = self.data_project['EXTENSION']['icons']
    #
    #     path = self.get_pipeline_path('img/{}.{}'.format(end_path, img_format))
    #     if not path: path = self.get_pipeline_path('img/{}/default.{}'.format(os.path.dirname(end_path), img_format))
    #     if not path: path = self.get_pipeline_path('img/btn/default.{}'.format(img_format))
    #     return path


    #*********************************************************************
    # YAML
    def set_yml_file(self, path, content):
        with open(path, 'w') as outfile:
            try:
                yaml.dump(content, outfile, default_flow_style=False)
            except yaml.YAMLError as exc:
                print(exc)


    def get_yml_file(self, path):
        try:
            with open(path, 'r') as stream:
                # STRING into DICT
                yml_content = yaml.load(stream)
                if yml_content:
                    return yml_content
                else:
                    print('CANT load file: {}'.format(path))
        except yaml.YAMLError as exc:
            print(exc)

    # define & register custom tag handler
    # combine var with strings
    def join(loader, node):
        seq = loader.construct_sequence(node)
        return ''.join([str(i) for i in seq])

    # replace (multiple) ENV var
    def env(loader, node):
        seq  = loader.construct_sequence(node)
        path = os.getenv(seq[0])
        seq.pop(0)

        if not path: return ''
        path = path.split(';')

        new_env = ''
        for env in path:
            if new_env: new_env += ';'
            new_env += env
            if seq: new_env += ''.join([str(os.path.normpath(i)) for i in seq])
        return new_env

    # replace (multiple) with first ENV var
    def env_first(loader, node):
        seq  = loader.construct_sequence(node)
        path = os.getenv(seq[0])
        print seq

        if ';' in path: path = path.split(';')[0]
        seq.pop(0)

        if seq: path += ''.join([str(os.path.normpath(i)) for i in seq])
        return path

    yaml.add_constructor('!env', env)
    yaml.add_constructor('!env_first', env_first)
    yaml.add_constructor('!join', join)


    #*********************************************************************
    # ENV
    #
    # @BRIEF  creates or add enviroment variable
    #
    # @PARAM  STRING var, STRING content
    def add_env(self, var, content):
        if not content: return

        # CHECK for list
        if isinstance(content, list):
            for item in content:
                self.add_env(var, item)
        else:
            content = str(content)

            # CHECK empty
            if os.environ.__contains__(var):
                os.environ[var] += ('').join([';', content])
            else:
                os.environ[var] = ('').join([content])
            return os.environ[var]

    # GET env or empty str & WARNING
    def get_env(self, var):
        if os.environ.__contains__(var):
            return os.environ[var].split(';')[0]
        print('ENV doesnt exist: {}'.format(var))
        return ''

