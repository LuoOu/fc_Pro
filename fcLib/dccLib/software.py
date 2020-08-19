#*********************************************************************
# content   = setup software attributes
# version   = 0.1.0
# date      = 2019-06-06
#
# license   = MIT <https://github.com/alexanderrichtertd>
# author    = Alexander Richter <alexanderrichtertd.com>
#*********************************************************************


import os
import subprocess

from fcLib.fileLib import folder
from fcLib.tankLib.configLib import Tank


#*********************************************************************
# VARIABLE
# TITLE = os.path.splitext(os.path.basename(__file__))[0]
# LOG   = Tank().log.init(script=TITLE)


#*********************************************************************
# CLASS
class Singleton(object):
    def __new__(cls, *args, **kwds):

        self = "__self__"
        if not hasattr(cls, self):
            instance = object.__new__(cls)
            instance.init(*args, **kwds)
            setattr(cls, self, instance)
        return getattr(cls, self)

    def init(self, *args, **kwds):
        pass




class Software(Singleton):

    _NAME = 'software'

    def setup(self):
        os.environ['SOFTWARE'] = self._NAME
        print self._NAME
        self._software_data = Tank().data_software
        self._version = self._software_data['version']
        self._path    = self._software_data['path']



    def setup_env(self):
        # LOG.debug('- {} -----------------------------------------------------'.format(self._NAME.upper()))

        sub_path = []
        software_path = []

        for each_path in os.environ['SOFTWARE_SRC_PATH'].split(';'):
            # if not each_path.endswith('software'): each_path = os.path.dirname(each_path)
            tmp_paths  = ('/').join([each_path, self._NAME])
            software_path.append(tmp_paths)
            tmp_folder = folder.get_file_list(path=tmp_paths, exclude='.py', add_path=True)
            if not tmp_folder:
                continue
            sub_path.extend(tmp_folder)

        os.environ['SOFTWARE_PATH']     = (';').join(software_path)
        os.environ['SOFTWARE_SUB_PATH'] = (';').join(sub_path)
        # LOG.debug("SOFTWARE_PATH: {}".format(os.environ['SOFTWARE_PATH']))

        # GET config
        self._software_data = Tank().data_software
        self._env = self._software_data.get('ENV', '')

        # ADD software ENV
        if(self._env):
            for env, content in self._env.iteritems():
                if isinstance(content, list):
                    for each in content: Tank().add_env(env, each)
                else:
                    Tank().add_env(env, content)

            # LOG.debug('{}_ENV: {}'.format(self._NAME.upper(), self._env))



    #*********************************************************************
    # SOFTWARE
    def start(self, software, open_file=''):
        self._NAME = software

        self.setup()
        # self.setup_env()
        print self._software_data
        cmd = self._software_data['start'].format(open_file)
        print cmd

        if open_file:
            if self._NAME == 'maya':
                cmd = '{} -file "{}"'.format(cmd, open_file)
            elif self._NAME == 'max' or self._NAME == 'houdini':
                cmd = '"{}" "{}"'.format(cmd, open_file)
        print os.environ
        # cmd = 'start "" "C:/Program Files/Autodesk/Maya2019/bin/maya.exe"'
        # os.startfile("C:/Program Files/Autodesk/Maya2019/bin/maya.exe")
        subprocess.Popen(cmd, shell=True,env=os.environ)


    def add_menu(self, menu_node, software):
        self._NAME = software
        self.add_sub_menu = []
        self._software_data = Tank().data_software


        for menu_item in self._software_data['MENU']:
            try:
                self.add_menu_item(menu_node, menu_item)
            except:
                pass
                # LOG.error('SOFTWARE Menu couldnt be created', exc_info=True)

        if self._NAME == 'max':
            import MaxPlus
            main_menu = menu_node.Create(MaxPlus.MenuManager.GetMainMenu())
            for sub in self.add_sub_menu: sub.Create(main_menu, 0)

    def add_menu_item(self, menu_node, new_command):
        if   self._NAME == 'maya':
            import maya.cmds as cmds
        elif self._NAME == 'max' :
            import MaxPlus
        else:
            pass

        sub_menu = ''

        for keys, item in new_command.iteritems():
            print keys, item
            # if self._NAME == 'maya':
            #     print 'cmds.{}'.format(item).format(menu_node)
            #     eval('cmds.{}'.format(item).format(menu_node))

            if isinstance(item, dict) or isinstance(item, list):
                if self._NAME == 'maya':
                    sub_menu = cmds.menuItem(p=menu_node, l=keys, sm=True)
                elif self._NAME == 'max':
                    MaxPlus.MenuManager.UnregisterMenu(unicode(keys))
                    sub_menu = MaxPlus.MenuBuilder(keys)
                    self.add_sub_menu.append(sub_menu)
                elif self._NAME == 'nuke':
                    sub_menu = menu_node.addMenu(keys)

                if sub_menu and isinstance(item, list):
                    for it in item:
                        self.add_menu_item(sub_menu, it)
                elif sub_menu:
                    self.add_menu_item(sub_menu, item)

            else:
                if self._NAME == 'maya':
                    eval('cmds.{}'.format(item).format(menu_node))
                elif self._NAME == 'max':
                    import max_menu
                    eval('menu_node.{}'.format(item))
                elif self._NAME == 'nuke':
                    eval('menu_node.{}'.format(item))

















