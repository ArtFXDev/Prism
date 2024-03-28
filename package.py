# -*- coding: utf-8 -*-


name = 'prism'

version = '2.0.0-1'

description = "Prism Pipeline"

cachable = True

def commands():

    env.PRISM_USER_PREFS.set("~/Documents/Prism2")  # Current default
    env.PRISM_DEFAULT_USER_PREFS.set("{root}/templates/Prism.json")

    # if install is on server - we should rather use rez package caching
    # env.PYTHONDONTWRITEBYTECODE.set("1")

    # launches with tray using Prism.exe
    alias("prismt", r"start {root}\Prism\Python39\Prism.exe {root}\Prism\Scripts\PrismTray.py projectBrowser")

    # direct python launch
    alias("prism", r"{root}\Prism\Python39\python.exe {root}\Prism\Scripts\PrismCore.py projectBrowser")


    # prism_console (wip)
    """
    env.PYTHONPATH.append('{root}/Prism/Scripts')
    script_path = expandvars(r"{root}\Prism\Scripts")
    print(script_path)
    command = f'import sys;sys.path.append("{script_path}");import PrismCore;pcore=PrismCore.create(prismArgs=["noUI", "loadProject"])'
    print(command)

    alias("prism_console", rf'{root}\Prism\Python39\python.exe -i -c "{command}"') 
    """


    """
    Variables:

    # 
    PRISM_PROJECT_CONFIG_NAME
    PRISM_PROJECT_CONFIG_PATH

    PRISM_DEFAULT_PLUGIN_PATH 
    PRISM_PLUGIN_PATHS 
    PRISM_PLUGIN_SEARCH_PATHS 

    PRISM_LICENSE_FILE 

    PRISM_USER_PREFS 

    env.PRISM_UPDATE_CHECK_ENABLED.set("0")
    """

# alias("python", expandvars("${HA_APP}/foss/python/3.9/python"))