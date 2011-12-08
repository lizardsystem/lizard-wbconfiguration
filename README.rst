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

    $> bin/django wbconfiguration_to_dbf --ident=[area configuration
    ident]

AreaConfiguration
----------------------------------------
Each area configuration could contains 10 structures.
2 of them are default and the other 8 ara free addedebale.

the structure will be created automaticlly on openign the waterbalance
configuration form with is_computed=true (Peilhandhaving In
defaul and Peilhandhaving Uit defaul). This 2 structures are not
deletable.

Structeres
--------------------------------------------
Defualt structures - the structure will be created automaticlly on opennign the waterbalance
configuration form with is_computed=true (Peilhandhaving In
defaul and Peilhandhaving Uit defaul). This 2 structures are not
deletable.

Structures have a code of the next format:
kw_<area ident>__<number 1-10>
for example: kw_2100__4

Buckets
--------------------------------------------
The buckets have a code of the next format:
wb_<area ident>__<number 1-10>
for example: wb_2100__4
