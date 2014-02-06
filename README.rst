``dj cmd``, for short
=====================

.. image::
    https://api.travis-ci.org/nigma/dj-cmd.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/nigma/dj-cmd

.. image:: https://pypip.in/v/dj-cmd/badge.png
    :target: https://pypi.python.org/pypi/dj-cmd/
    :alt: Latest Version

.. image:: https://pypip.in/d/dj-cmd/badge.png
    :target: https://pypi.python.org/pypi/dj-cmd/
    :alt: Downloads

.. image:: https://pypip.in/license/dj-cmd/badge.png
    :target: https://pypi.python.org/pypi/dj-cmd/
    :alt: License


Tired of typing ``python manage.py runserver`` to invoke Django commands? Just

::

    pip install dj-cmd

and then

::

    dj r

from any project's directory.

Features
--------

- saves typing
- automatically locates Django's ``manage.py`` script in the current or parent directories
- works great with virtualenv, even on Windows

Commands
--------

List of command aliases is a matter of personal taste, so go ahead and adjust
the config or fork the project and add yours to the `aliases.py`_ file.

Currently supported commands:

- ``r`` or ``run`` - runserver
- any valid ``manage.py`` command

Config file
+++++++++++

Command aliases can also be specified using a config file.

If a ``.djcmd`` or ``.dj.ini`` config file is present in the user's home directory
or in the ``manage.py`` base directory, it is used to populate the list
of command aliases.

`Example <https://github.com/nigma/dj-cmd/blob/master/.djcmd>`_ of the ``.djcmd`` config file::

    [commands]
    r=runserver
    rp=runserver_plus

    sh=shell
    sp=shell_plus

    cs=collectstatic --noinput

    m=migrate
    sma=schemamigration --auto
    smi=schemamigration --init

    mm=makemessages -a
    cm=compilemessages

    cleanpyc=clean_pyc

Put it in your home or in the ``manage.py`` base directory of your project.

License
-------

``dj-cmd`` is released under the BSD license.


Other Resources
---------------

- GitHub repository - https://github.com/nigma/dj-cmd
- PyPi Package site - http://pypi.python.org/pypi/dj-cmd

.. _aliases.py: https://github.com/nigma/dj-cmd/blob/master/src/aliases.py


Commercial Support
------------------

This app, and many others, have been created at `en.ig.ma <http://en.ig.ma/>`_
web & mobile development.

Do you need help building your web app or api backend? Just drop us a note
at `en@ig.ma <mailto:en@ig.ma>`_ and we will guide you from project idea
to live website.
