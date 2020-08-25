#*********************************************************************
# content   = Maya
# version   = 0.1.0
# date      = 2019-10-06
#
# license   = MIT <https://github.com/alexanderrichtertd>
# author    = Alexander Richter <alexanderrichtertd.com>
#*********************************************************************


import os

import maya.mel as mel
import maya.cmds as cmds
import pymel.core as pm
from fcLib.tankLib.codeLib import Code
from fcLib.tankLib.configLib import Tank

#*********************************************************************
# VARIABLE
# TITLE = os.path.splitext(os.path.basename(__file__))[0]
# LOG   = Tank().log.init(script=TITLE)


#*********************************************************************
# CLASS
class Maya(object):

    _NAME = 'maya'

    @property
    def scene_path(self):
        return pm.sceneName()

    def scene_save(self, file_path):
        return pm.saveFile(file_path)

    def scene_save_as(self, file_path, setup_scene=False):
        if setup_scene:
            self.scene_setup(file_path)
        return pm.saveAs(file_path)

    def scene_open(self, file_path):
        return pm.openFile(file_path, force=True)

    def scene_import(self, file_path):
        pass

    def scene_judge(self):
        self.scene_analysis()
        # file_path = self.scene_path
        # results = True
        # if len(file_path) >= len(os.environ['FC_LOCAL_ROOT']):
        #     pass
        # else:
        #     results = False
        # print file_path[0:len(os.environ['FC_LOCAL_ROOT'])]
        # if file_path[0:len(os.environ['FC_LOCAL_ROOT'])] == os.environ['FC_LOCAL_ROOT'].replace('\\','/'):
        #     pass
        # else:
        #     results = False

        # return results

    def scene_analysis(self):
        file_path = self.scene_path
        if file_path == 0:
            from fcLib.promptLib import errorLib
            errorLib.file_not_saved('')
        else:
            if not file_path.startswith(os.environ['FC_LOCAL_ROOT'].replace('\\','/')):
                from fcLib.promptLib import errorLib
                errorLib.file_path_error('')
            else:
                tmp_str = file_path[len(os.environ['FC_LOCAL_ROOT'])+1:len(file_path)]
                tmp_list = tmp_str.split('/')
                if not len(tmp_list) == 7:
                    from fcLib.promptLib import errorLib
                    errorLib.file_path_error('')
                else:
                    Code().set_code(tmp_str, 1)







        # # reference or open
        # if ref or ".abc" in self.save_dir or ".obj" in self.save_dir or ".fbx" in self.save_dir:
        #     # file -r -type "mayaBinary"  -ignoreVersion -gl -mergeNamespacesOnClash false -namespace "bull_MODEL_v004_jo" -options "v=0;" "K:/30_assets/bull/10_MODEL/WORK/bull_MODEL_v004_jo.mb";
        #     mel.eval('file -r -type "' + s.FILE_FORMAT_CODE["." + self.save_dir.split(".")[-1]] + '" -ignoreVersion -gl -mergeNamespacesOnClash false "' + self.save_dir.replace("\\", "/") + '"')


    #*********************************************************************
    # SHELF
    # def add_shelf(self, shelf_name='', header_footer=True):
    #     new_shelf  = []
    #     shelf_data = Tank().data_software['SHELF']
    #
    #     # GET header scripts
    #     if header_footer: new_shelf += shelf_data['HEADER']
    #
    #     # GET main scripts
    #     if shelf_name in shelf_data:
    #         new_shelf += shelf_data[shelf_name]
    #     else:
    #         LOG.warning('shelf {} doesnt exist'.format(shelf_name))
    #
    #     # GET footer scripts
    #     if header_footer: new_shelf += shelf_data['FOOTER']
    #
    #     LOG.debug('{} - {}'.format(shelf_name, new_shelf))
    #     if not shelf_name: shelf_name = os.getenv('PROJECT_NAME')
    #
    #     # DELETE old and CREATE shelf tab
    #     remove_shelfs = shelf_data.keys() + [shelf_name, os.getenv('PROJECT_NAME')]
    #     for shelf in remove_shelfs:
    #         if pm.shelfLayout(shelf, ex=1):
    #             pm.deleteUI(shelf)
    #
    #     pm.shelfLayout(shelf_name, p="ShelfLayout")
    #     pm.setParent(shelf_name)
    #
    #     # ADD shelf btn
    #     for btn in new_shelf:
    #         for key, item in btn.items():
    #             shelf_btn = 'pm.shelfButton({})'.format(item)
    #             eval(shelf_btn)
    #
    #     shelf_nr = len(mel.eval('layout -q -ca ShelfLayout;'))
    #     mel.eval('shelfTabLayout -edit -selectTabIndex {} ShelfLayout;'.format(shelf_nr))
