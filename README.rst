`dj cmd`, for short
===================

.. image::
    https://secure.travis-ci.org/nigma/dj-cmd.png?branch=master
    :alt: Build Status
    :target: https://secure.travis-ci.org/nigma/dj-cmd

Tired of typing `python manage.py runserver`? Just 

  `pip install dj-cmd` 

and then

  `dj run` 

from any project's subdirectory.

Features
--------

- saves typing
- automatically locates `manage.py` script in current or parent directories
- works great with virtualenv and on Windows

Commands
--------

List of command aliases is a matter of personal taste, so go ahead and adjust
it by forking the project and adding yours to the `aliases.py`_ file.

Currently supported commands:

- run - runserver
- any valid `manage.py` command

License
-------

`dj-cmd` is released under the BSD license.


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

.. _aliases.py: https://github.com/nigma/dj-cmd/blob/master/src/aliases.py
