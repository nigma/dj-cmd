``dj cmd``
==========

.. image:: https://img.shields.io/pypi/l/dj-cmd.svg
    :target: https://raw.githubusercontent.com/nigma/dj-cmd/master/LICENSE
    :alt: License

.. image:: https://secure.travis-ci.org/nigma/dj-cmd.svg?branch=master
    :target: http://travis-ci.org/nigma/dj-cmd
    :alt: Build Status

.. image:: https://img.shields.io/pypi/v/dj-cmd.svg
    :target: https://pypi.python.org/pypi/dj-cmd/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/dj-cmd.svg
    :target: https://pypi.python.org/pypi/dj-cmd/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/pypi/wheel/dj-cmd.svg
    :target: https://pypi.python.org/pypi/dj-cmd/
    :alt: Supports Wheel format


Tired of typing long Django commands like ``python manage.py runserver``? Just

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

Predefined shortcuts include:

- ``r`` or ``run`` - runserver
- any valid ``manage.py`` command

Config file
+++++++++++

Command aliases can be specified in a config file.

If a ``.djcmd`` or ``.dj.ini`` config file is present in the user's home directory
or in the ``manage.py`` base directory, it is used to populate the list
of command aliases.

`Example <https://github.com/nigma/dj-cmd/blob/master/.djcmd>`_ of the ``.djcmd`` config file::

    [commands]
    r=runserver
    rp=runserver_plus

    sh=shell
    sp=shell_plus
    dbs=dbshell

    cs=collectstatic --noinput

    m=migrate
    mm=makemigrations 
    sm=showmigrations

    cleanpyc=clean_pyc

Put it in your home or in the ``manage.py`` base directory of your project.

License
-------

``dj-cmd`` is released under the BSD license.


Other Resources
---------------

- GitHub repository - https://github.com/nigma/dj-cmd
- PyPi Package site - http://pypi.python.org/pypi/dj-cmd
- Sample config file - https://github.com/nigma/dj-cmd/blob/master/.djcmd

.. _aliases.py: https://github.com/nigma/dj-cmd/blob/master/src/aliases.py


Commercial Support
------------------

This app, and many others, have been created at `en.ig.ma <http://en.ig.ma/>`_
web & mobile development.

Want to create a cutting edge web or mobile app or need help with setting up backend architecture?
Just drop us a note at `en@ig.ma <mailto:en@ig.ma>`_ and we will guide you from idea
to a final product.
