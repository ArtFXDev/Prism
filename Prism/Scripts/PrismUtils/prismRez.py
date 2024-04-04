# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2023 Richard Frangenberg
# Copyright (C) 2023 Prism Software GmbH
#
# Licensed under GNU LGPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.


# This file contains functions for rez usage in Prism.

import os


def getRezCommand(args):
    """
    This function is used when PrismCore launches a DCC.
    We want to keep the current request, containing for example a project package, except "prism" package itself,
    and add it to the called command.

    For given "args", a rez command in list form,
    we add the current rez request, using REZ_USED_REQUEST env variable,
    we remove "prism" itself from the current request,
    and return the resulting rez command as a string.

    Note: we do not use the rez API, because Prism ships with its own python version.
    We cannot control compatibility.

    :param args: list of arguments
    :return: string of rez command
    """

    # we transform to a string
    args = ' '.join(args)  # convert to string if args is a list
    args = args.split("--")
    args[0] = args[0].strip()

    # retrieve the current request and remove "prism" package (anything starting with prism, eg. prism-2)
    currentRequest = os.environ.get("REZ_USED_REQUEST", "")
    requestedPackages = [x for x in currentRequest.split(" ") if not x.startswith("prism")]
    command = "{} {}".format(args[0], " ".join(requestedPackages))
    command = command.strip()

    if len(args) > 1:
        command = "{} -- {}".format(command, args[1].strip())

    return command


if __name__ == "__main__":

    # to test this code, start it from a rez environment,
    # for example `rez env prism-2 pycharm -- pycharm`

    result = getRezCommand("rez env testpackage maya -- maya".split(" "))
    print(result)

    result = getRezCommand("rez env testpackage maya -- maya".split(" "))
    print(result)

    result = getRezCommand("rez env testpackage houdini".split(" "))
    print(result)

    result = getRezCommand("rez env testpackage-0.2 nuke".split(" "))
    print(result)

    result = getRezCommand("rez env prism".split(" "))
    print(result)
