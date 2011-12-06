lizard-wbconfiguration
==========================================

Introduction

Manages water balance configuration.


Development installation
------------------------

The first time, you'll have to run the bootstrap script to set up setuptools
and buildout::

    $> python bootstrap.py

And then run buildout to set everything up::

    $> bin/buildout

Run syncdb to build the models.

    $> bin/django syncdb

Load fixtures.

    $> bin/django loaddata wb_configuration

Create the dbf files voor AreaConfiguration, Buckets and Structures
with management command::

    $> bin/django wbconfiguration_to_dbf --ident=[area configuration ident]
