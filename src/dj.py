#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import os
import subprocess
import sys

from .aliases import COMMANDS

def resolve_command(command):
    """
    Lookups command in the alias dict.
    """
    if command and command in COMMANDS:
        command = COMMANDS[command]
    return command or ""


def find_script(script_name="manage.py"):
    """
    Locates the `script_name` file by searching in the current and parent
    directories.

    :param str script_name: Name of the manage script. Default is `manage.py`.
    :returns: Path to the manage script.
    :rtype: str
    """
    searched_paths = []

    directory = os.getcwd()
    while True:
        script_path = os.path.join(directory, script_name)
        searched_paths.append(script_path)
        if os.path.exists(script_path):
            return script_path

        base_directory = os.path.dirname(directory)
        if base_directory == directory:
            sys.exit(
                "dj-cmd: No '{0}' script found in this directory or its parents.\n"
                "Searched paths:\n{1}".format(script_name,
                    "\n".join(" - {0}".format(path) for path in searched_paths)
                )
            )
        directory = base_directory


def run(command=None, *params):
    """
    Locates manage script and invokes it with resolved command param.
    """
    command = resolve_command(command)
    script_path = find_script()

    args = [sys.executable, script_path]
    if command:
        args.append(command)
    args.extend(params)

    return subprocess.call(args)


def main():
    """Entry-point function."""
    sys.exit(run(*sys.argv[1:]))


if __name__ == "__main__":
    main()
