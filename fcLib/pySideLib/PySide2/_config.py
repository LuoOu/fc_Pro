built_modules = list(name for name in
    "Core;Gui;Widgets;PrintSupport;Sql;Network;Test;Concurrent;WinExtras;Xml;XmlPatterns;Help;Multimedia;MultimediaWidgets;OpenGL;Positioning;Location;Qml;Quick;QuickWidgets;Sensors;TextToSpeech;Charts;Svg;DataVisualization;UiTools;AxContainer;WebChannel;WebEngineCore;WebEngineWidgets;WebSockets;3DCore;3DRender;3DInput;3DLogic;3DAnimation;3DExtras"
    .split(";"))

shiboken_library_soversion = str(5.9)
pyside_library_soversion = str(5.9)

version = "5.9.0a1.dev1524638270"
version_info = (5, 9, 0, "a", 1)

__build_date__ = '2018-04-25T06:40:00+00:00'




# Timestamp used for snapshot build, which is part of snapshot package version.
__setup_py_package_timestamp__ = '1524638270'