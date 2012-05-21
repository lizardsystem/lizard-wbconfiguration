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
Each area configuration contains 10 structures and meny buckets.


Structeres
--------------------------------------------
Defualt structures - 10 structure will be created automaticlly on openign the waterbalance
configuration form with name. The user is not available to add or delete any structure.

The structure has next code format:
- <area_ident>_uitlaatPB
- <area_ident>_inlaatPB
- <area_ident>_uitlaat1
- <area_ident>_uitlaat2
- <area_ident>_uitlaat3
- <area_ident>_uitlaat4
- <area_ident>_inlaat1
- <area_ident>_inlaat2
- <area_ident>_inlaat3
- <area_ident>_inlaat4

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
