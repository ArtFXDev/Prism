# Prism Pipeline

This is a fork of the Prism Pipeline.

Prism automates and simplifies the workflow of animation and VFX projects.

You can find more information on the website:

https://prism-pipeline.com/

This repository contains the Prism core application and the officially available open source plugins.
Additional features and plugins are available on the Prism website.

## This fork

This fork attempts to use Prism in a network and rez environment.  
We do not attempt to rezify prism itself and its dependencies.

*This is not yet a rez recipe. Installation needs to be done manually.*

To install, clone this repo into a rez package path, using the manual installation described below, and adapt the `package.py` file.

To run:

````commandline
rez env prism -- prism
````

### Rez caching

Prism package is heavy and should be cached.
In the rezconfig file, add a local **cache_packages_path**.

Example: 
`cache_packages_path = r"C:\rez\package_cache"` 

### Default User config from template

Upon launch, check of the user config:
- as defined in `PRISM_USER_PREFS`
- defaults to `~/Documents/Prism2`

If it does not exist, the template user pref file is used as a default
- as defined in `PRISM_DEFAULT_USER_PREFS`
- default in `templates\Prism.json`

This user config overrides the DCC startups by settings rez commands.
Example:
`"Houdini_path": "rez env houdini ssx_houdini -- houdini"`

## Project startup

We need server based project folders, and rez packages to configure the projects.

The project config file `pipeline.json` should be copied into the future project location.
Example: `D:\michaelhaussmann\PROJECTS\TESTPIPE\00_Pipeline\pipeline.json`

The project package.py should contain:
```
env.PRISM_PROJECT_CONFIG_PATH.set(r"D:\michaelhaussmann\PROJECTS\TESTPIPE\00_Pipeline\pipeline.json")
```

On startup the user can **Browse Projects** and select the project folder.
`D:\michaelhaussmann\PROJECTS\TESTPIPE`




## Getting Started

On the [website](https://prism-pipeline.com/downloads/) you can find the latest official installer.

For a getting started guide about how to use Prism see the [Documentation](https://prism-pipeline.com/docs/latest/).


## Installing

**At this time Prism 2 is supported on Windows only.**

Download the installer from the [website](https://prism-pipeline.com/downloads/)
(This version allows you to automatically update Prism and install new plugins)

or to install Prism manually:

* Download or clone this repository and download the [Prism dependencies](https://www.dropbox.com/scl/fi/zh9t0im2qsd6mtlmpd9vs/Prism_dependencies_v2.0.0.zip?rlkey=o0lhrixa5klm3bell35wuhvsy&dl=1).

* Extract the dependencies and copy the extracted folders into the "Prism" folder of this repository.

* Now the "Prism" folder should contain the folders like:
"Plugins", "Python39", "PythonLibs", "Scripts", ...

* Execute the setup.bat file to launch Prism.

## License

This project is licensed under the GNU LGPL-3.0-or-later License - see the [license-LGPL.txt](license-LGPL.txt) file for details.