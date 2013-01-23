#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import os
import subprocess
import sys

from .aliases import DEFAULT_COMMANDS


def find_config_files(script_path, file_names=(".dj.ini", ".djcmd")):
    """
    Locates and returns a list of config files.

    By default it looks for ``.dj.ini`` or ``.djcmd`` files in:
       - user's home directory
       - ``manage.py`` script directory
    """
    directories = ["~", os.path.dirname(script_path)]
    config_files = []
    for directory in directories:
        for file_name in file_names:
            config_file = os.path.expanduser(os.path.join(directory, file_name))
            if os.path.exists(config_file):
                config_files.append(config_file)
    return config_files


def get_commands(config_files, section="commands",
                 default_commands=DEFAULT_COMMANDS):
    """
    Read alias definition from given config files.

    Example of config file::

        [commands]
        h=help
        rs=runserver
        sma=schemamigration --auto
    """
    commands = default_commands.copy()

    for config_file in config_files:
        if os.path.exists(config_file):
            from ConfigParser import ConfigParser
            parser = ConfigParser()
            parser.read([config_file])
            if parser.has_section(section):
                commands.update(
                    (k, v.split()) for k, v in parser.items(section)
                )

    return commands


def resolve_command(command, config_files):
    """
    Lookups command in the alias dict.
    """
    commands = get_commands(config_files=config_files)
    if command and command in commands:
        command = commands[command]
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
    script_path = find_script()
    config_files = find_config_files(script_path)
    command = resolve_command(command, config_files=config_files)

    args = [sys.executable, script_path]
    if command:
        if isinstance(command, (list, tuple)):
            args.extend(command)
        else:
            args.append(command)
    args.extend(params)

    return subprocess.call(args)


def main():
    """Entry-point function."""
    sys.exit(run(*sys.argv[1:]))


if __name__ == "__main__":
    main()
