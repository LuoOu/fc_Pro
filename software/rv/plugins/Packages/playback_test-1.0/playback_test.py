import sys

from rv import commands 
from rv import rvtypes


class PlaybackTest(rvtypes.MinorMode):
    def __init__(self):
        rvtypes.MinorMode.__init__(self)

        self.enabled = False

        self.modename = "playback-check"
        self.init(self.modename, 
                [], None, 
                [("Plugins", [("Test", [("Playback", self.run, None, None)])])]
                )

    def run(self, dummy_event):
        self.enabled = True
        from PySide import QtGui, QtCore, QtOpenGL
        QtCore.QTimer.singleShot(50, lambda: self.start_play())
        self.start_play()

    def stop_play(self):
        from PySide import QtCore
        from rv import commands
        from random import randint
        commands.stop()
        QtCore.QTimer.singleShot(50, lambda: self.start_play())
        frame = randint(1, commands.frameEnd())
        commands.setFrame(frame)

    def start_play(self):
        from PySide import QtCore
        from rv import commands
        from random import randint
        commands.play()
        # From 0.5sec to 5secs
        playtime = randint(500, 5000)
        QtCore.QTimer.singleShot(playtime, lambda: self.stop_play())

def createMode():
    return PlaybackTest()

