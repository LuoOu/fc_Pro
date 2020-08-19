import maya.cmds as cmds
def autoPlacePivot():
    obj = cmds.ls(sl=1)
    if len(obj) != 0:
        cmds.xform(obj, cp=1)
        bbox = cmds.exactWorldBoundingBox()
        bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
        cmds.xform(obj, piv=bottom, ws=1)
        cmds.move( 0, 0, 0, obj, rpr=1 )

        
# autoPlacePivot()