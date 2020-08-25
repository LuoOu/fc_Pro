# -*- coding: UTF-8 -*-
#.@FileName:errorLib
#.@Date:2020-06-22:15:55
#.@Aurhor:LuoOu

from fcLib.appLib import fcPrompt

def file_not_saved(prompt = ''):
    title ='error'
    text = 'file not saved'
    fcPrompt.start(title,text,prompt)

def file_path_error(prompt = ''):
    title ='error'
    text = 'file path error'
    fcPrompt.start(title,text,prompt)
