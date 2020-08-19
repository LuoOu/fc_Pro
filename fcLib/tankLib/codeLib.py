# -*- coding: UTF-8 -*-
#.@FileName:codeLib
#.@Date:2020-07-03:16:50
#.@Aurhor:LuoOu
import os

import yaml

# from pipLib import pipefunc

#*********************************************************************
# VARIABLES
TITLE = os.path.splitext(os.path.basename(__file__))[0]

DATA_FORMAT = '.yml'



class Code(object):


    @property
    def data_project(self):
        return self.get_code('PROJECT_NAME')

    @property
    def data_module(self):
        return self.get_code('MODULE')

    @property
    def data_class(self):
        return self.get_code('CLASS')

    @property
    def data_entity(self):
        return self.get_code('ENTITY')

    @property
    def data_step(self):
        return self.get_code('STEP')

    @property
    def data_task(self):
        return self.get_code('TASK')

    @property
    def data_variant(self):
        return self.get_code('VARIANT')

    @property
    def data_version(self):
        return self.get_code('VERSION')


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

    def get_code(self, tier=''):

        code = os.environ[tier]
        return code






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