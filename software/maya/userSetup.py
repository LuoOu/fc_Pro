#*********************************************************************
# content   = setup maya
# version   = 0.1.0
# date      = 2019-12-01
#
# license   = MIT <https://github.com/alexanderrichtertd>
# author    = Alexander Richter <alexanderrichtertd.com>
#*********************************************************************


import os


import maya.cmds as cmds
# from fcLib.tankLib.configLib import Tank
# _software_data = Tank().data_software
# _env = _software_data.get('ENV', '')
# if (_env):
#     for env, content in _env.iteritems():
#         if isinstance(content, list):
#             for each in content: Tank().add_env(env, each)
#         else:
#             Tank().add_env(env, content)

import maya_utils
cmds.evalDeferred("maya_utils.load_menus()")
# from tankLib.tank import Tank
#
#
# #*********************************************************************
# # VARIABLE
# TITLE = 'userSetup' # os.path.splitext(os.path.basename(__file__))[0]
# LOG   = Tank().log.init(script=TITLE)
#
#
# #*********************************************************************
# # INIT AND PRINT CONSOLE
# Tank().init_software(os.getenv('SOFTWARE'))
#
# Tank().software.print_checked_header('menu', func=cmds.evalDeferred("maya_utils.load_menus()"))
# Tank().software.print_checked_header('shelf')
# Tank().software.print_checked_header('scene setup')
# Tank().software.print_checked_header('render setup')

# print("")


