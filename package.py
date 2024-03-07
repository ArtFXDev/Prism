# -*- coding: utf-8 -*-


name = 'prism'

version = '2.0.0-1'

description = "Prism Pipeline"


def commands():

    env.PRISM_USER_PREFS.set("~/Documents/Prism2")  # Current default - changing this works

    env.PYTHONPATH.append('{root}/python')

    # launches with tray using Prism.exe
    alias("prismt", r"start {root}\Prism\Python39\Prism.exe {root}\Prism\Scripts\PrismTray.py projectBrowser")

    # direct python launch
    alias("prism", r"{root}\Prism\Python39\python.exe {root}\Prism\Scripts\PrismCore.py projectBrowser")


    """
    Variables:

    PRISM_DEFAULT_PLUGIN_PATH 
    PRISM_PLUGIN_PATHS 
    PRISM_PLUGIN_SEARCH_PATHS 

    PRISM_LICENSE_FILE 

    PRISM_USER_PREFS 

    env.PRISM_UPDATE_CHECK_ENABLED.set("0")
    """



# alias("python", expandvars("${HA_APP}/foss/python/3.9/python"))