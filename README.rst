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

    $> bin/django loaddata lizard_wbconfiguration

Create the dbf files voor AreaConfiguration, Buckets and Structures
with management command::

    $> bin/django wbconfiguration_to_dbf

AreaConfiguration
----------------------------------------
Each area configuration could contains 10 structures. 2 of them are default and the other 8 ara free addetable.


Structeres
--------------------------------------------
Defualt structures - the structure will be created automaticlly on openign the waterbalance
configuration form with name 'Peilhandhaving In defaul' and
'Peilhandhaving Uit defaul'. This 2 structures are not deletable.

Structures get a code of the next format:
kw_<area ident>__<number 1-10>
for example: kw_2100__4

Buckets
--------------------------------------------
The buckets get a code of the next format:
wb_<area ident>__<number 1-10>
for example: wb_2100__4

Configuration
---------------------------------
To configure table 'Gebied eigenschappen' and 'Openwater' use form
'Area grid configuration' of admin interface.

To configure dbf export use admin form 'Dbf configuration'.

To map water balance configuration fields with dbf fields use admin
form 'Wb configuration dbf mappings'.

Export wbconfigurations to dbf  as periodic task
-----------------------------------
Schedule 'lizard_wbconfiguration.tasks.export_to_dbf' periodic task in admin by Djcelery.

OR use management command

    $> bin/django wbconfiguration_to_dbf
