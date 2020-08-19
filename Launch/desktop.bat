:: fcDESKTOP

:: Hide Commands
@echo off

CALL %~dp0\setup_env.bat

start python %newDir%\launch.py %1 --software desktop
rem
exit
