#*********************************************************************
# content   = common functions
# version   = 0.1.0
# date      = 2019-12-01
#
# license   = MIT <https://github.com/alexanderrichtertd>
# author    = Alexander Richter <alexanderrichtertd.com>
#*********************************************************************


import os
import glob
import json
import time
import webbrowser

# NO logging since it will break the init



#*********************************************************************
# FUNCTIONS
# def help(name=''):
#     from fcLib.tankLib import Tank
#
#     if not name and os.getenv('SOFTWARE'):
#         name = os.getenv('SOFTWARE')
#
#     project_help = Tank().data_project['HELP']
#     if name in project_help:
#         webbrowser.open(project_help[name])
#     else:
#         webbrowser.open(project_help['default'])


# GET all (sub) keys in dict
def get_all_keys(key_list, dictonary=[]):
    for key, items in key_list.iteritems():
        dictonary.append(key)
        if isinstance(items, dict):
            get_all_keys(items, dictonary)

    return dictonary


# decorator: return function duration time
def get_duration(func):
    def timed(*args, **kw):
        startTime  = time.time()
        resultTime = func(*args, **kw)
        endTime    = time.time()

        printResult = '%r (%r, %r) %2.2f sec' % (func.__name__, args, kw, endTime-startTime)
        print(printResult)

        return resultTime

    return timed


def find_inbetween(text, first, last):
    try:
        start = text.index(first) + len(first)
        end   = text.index(last, start)
    except ValueError: return ""
    return text[start:end]


#*********************************************************************
# FOLDER
# @BRIEF  creates a folder, checks if it already exists,
#         creates the folder above if the path is a file
def create_folder(path):
    if len(path.split('.')) > 1: path = os.path.dirname(path)
    if not os.path.exists(path):
        try:    os.makedirs(path)
        except: print('CANT create folder: {}'.format(path))

# @BRIEF  opens folder even if file is given
def open_folder(path):
    path = os.path.normpath(path)
    if os.path.exists(path):
        if len(path.split('.')) > 1: path = os.path.dirname(path)
        webbrowser.open(path)
    else: print('UNVALID path: {}'.format(path))
    return path


#*********************************************************************
# FILES
# @BRIEF  get a file/folder list with specifics
#
# @PARAM  path string.
#         file_type string/string[]. '*.py'
#         extension bool. True:[name.py] False:[name]
#         exclude string /string[]. '__init__.py' | '__init__' | ['btnReport48', 'btnHelp48']
#
# @RETURN strint[].
def get_file_list(path, file_type='*', extension=False, exclude='*', add_path=False):
    if(os.path.exists(path)):
        getFile = []
        try:
            os.chdir(path)
        except:
            print('Invalid dir: {}'.format(path))
        for file_name in glob.glob(file_type):
            if exclude in file_name:
                continue
            if add_path:
                file_name = os.path.normpath(('/').join([path,file_name]))
            if extension:
                getFile.append(file_name)
            else:
                getFile.append((file_name.split('.')[0]))
        return getFile

def cut_filesplit_list(filelist,split_type='_',serial = 1,extension=True):
    newlist=[]
    if filelist:
        for i in filelist:
            if extension:
                print i
                tmp = i.split('.')[0]
                newlist.append(tmp.split(split_type)[serial])
            else:
                newlist.append(i.split(split_type)[serial])
    return newlist

##
# @BRIEF  GET ALL subfolders in the path
def get_deep_folder_list(path, add_path=False):
    if add_path: getFile = map(lambda x: x[0], os.walk(path))
    else:        getFile = map(lambda x: os.path.basename(x[0]), os.walk(path))

    try:    getFile.pop(0)
    except: print('CANT pop file. Path: {}'.format(path))

    return getFile



#*********************************************************************
# REPOSITORY
def make_github_issue(title, body=None, assignee='', milestone=None, labels=None):
    import requests
    from fcLib.tankLib import Tank

    REPO_DATA = Tank().user.data_user_path
    if not assignee: assignee = REPO_DATA['username']

    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_DATA['owner'], REPO_DATA['repository'])

    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (REPO_DATA['username'], REPO_DATA['password'])

    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'milestone': milestone,
             'labels': labels}

    # Add the issue to our repository
    repo = session.post(url, json.dumps(issue))

    if repo.status_code == 201:
        LOG.info('Successfully created Issue {}'.format(title))
    else:
        LOG.warning('Could not create Issue {}.\nResponse:{}'.format(title, repo.content))


#*********************************************************************
# TEST
# make_github_issue(title='Login Test', body='Body text', milestone=None, labels=['bug'])


