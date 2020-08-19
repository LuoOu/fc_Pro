# -*- coding: UTF-8 -*-
#.@FileName:GeometryCache_WindCycle
#.@Date:2019-12-13:11:11
#.@Aurhor:LuoOu

import maya.cmds as cmds

def GeometryCache_WindCycle():
    win_ui = 'GeometryCache_WindCycle'
    if cmds.window(win_ui,ex=1) ==1:
        cmds.deleteUI(win_ui)
    cmds.window(win_ui)
    cmds.columnLayout(columnAttach=('both', 5), rowSpacing=10, columnWidth=250)
    cmds.button(l=u"设置cacheBlend节点",c =GeometryCache_WindCycle_A)
    cmds.button(l=u"设置序号为0的节点", c=GeometryCache_WindCycle_B)
    cmds.button(l=u"设置序号为1的节点", c=GeometryCache_WindCycle_C)
    cmds.showWindow(win_ui)


def GeometryCache_WindCycle_A(*args):
    nonelist = cmds.ls(sl = True,type="cacheBlend")
    print nonelist
    if not len(nonelist) == 0:
        for i in nonelist:
            cmds.setKeyframe([i + ".cd[0].w"], t=1,v=1)
            cmds.setKeyframe([i + ".cd[0].w"], t=37, v=1)
            cmds.setKeyframe([i + ".cd[0].w"], t=75, v=0)
            cmds.setKeyframe([i + ".cd[0].w"], t=112, v=1)
            cmds.setKeyframe([i + ".cd[0].w"], t=150, v=1)

            cmds.setKeyframe([i + ".cd[1].w"], t=1, v=0)
            cmds.setKeyframe([i + ".cd[1].w"], t=37, v=0)
            cmds.setKeyframe([i + ".cd[1].w"], t=75, v=1)
            cmds.setKeyframe([i + ".cd[1].w"], t=112, v=0)
            cmds.setKeyframe([i + ".cd[1].w"], t=150, v=0)
def GeometryCache_WindCycle_B(*args):
    nonelist = cmds.ls(sl=True, type="cacheFile")
    print nonelist
    if not len(nonelist) == 0:
        for i in nonelist:
            cmds.setAttr(i+".startFrame", 75)
            cmds.setAttr(i+".preCycle", 1)
            cmds.setAttr(i + ".sourceStart", 0)


def GeometryCache_WindCycle_C(*args):
    nonelist = cmds.ls(sl=True, type="cacheFile")
    print nonelist
    if not len(nonelist) == 0:
        for i in nonelist:
            cmds.setAttr(i+".sourceStart", 0)
