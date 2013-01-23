``dj cmd``, for short
=====================

.. image::
    https://api.travis-ci.org/nigma/dj-cmd.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/nigma/dj-cmd

Tired of typing ``python manage.py runserver``? Just

::

    pip install dj-cmd

and then

::

    dj run

from any project's directory.

Features
--------

- saves typing
- automatically locates ``manage.py`` script in the current or parent directories
- works great with virtualenv, even on Windows

Commands
--------

List of command aliases is a matter of personal taste, so go ahead and adjust
the config or fork the project and add yours to the `aliases.py`_ file.

Currently supported commands:

- ``run`` - runserver
- any valid ``manage.py`` command

Config file
+++++++++++

Command aliases can also be specified using a config file.

If a ``.djcmd`` or ``.dj.ini`` config file is present in the user's home directory
or in the ``manage.py`` base directory, it is used to populate the list
of command aliases.

`Example <https://github.com/nigma/dj-cmd/blob/master/.djcmd>`_ of the ``.djcmd`` config file::

    [commands]
    cs=collectstatic --noinput
    r=runserver
    sh=shell

    rp=runserver_plus
    shp=shell_plus

    m=migrate
    sma=schemamigration --auto

Put it in your home or in the ``manage.py`` base directory of your project.

License
-------

``dj-cmd`` is released under the BSD license.


Similar projects
----------------

This is not the first project of this kind. Other may suits you better,
this works well for me.

- http://pypi.python.org/pypi/django-shortcuts
- http://pypi.python.org/pypi/Django-dj

Other Resources
---------------

- GitHub repository - https://github.com/nigma/dj-cmd
- PyPi Package site - http://pypi.python.org/pypi/dj-cmd
- Distutils `dev <https://github.com/nigma/django-herokuify/tarball/master#egg=django-herokuify-dev>`_ version link.

.. _aliases.py: https://github.com/nigma/dj-cmd/blob/master/src/aliases.py
