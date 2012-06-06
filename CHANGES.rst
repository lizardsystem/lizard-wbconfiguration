Changelog of lizard-wbconfiguration
===================================================


0.5.4 (unreleased)
------------------

- Nothing changed yet.


0.5.3 (2012-06-06)
------------------

- fixes for history page in ie


0.5.2 (2012-05-31)
------------------

- Removed ydev tag from setup.py as well.

- Added functionality to remove rejected configuration on validation.

- Impoved logging of celery tasks.


0.5.1 (2012-05-29)
------------------

- Removed dev y-tag by making new release.


0.5 (2012-05-29)
----------------

- Add urls and views to display archived versions of wb configurations.s


0.4 (2012-05-21)
----------------

- Changed code format of structures.

- Deleted functionality to add or delete structures.


0.3 (2012-05-14)
----------------

- Increases the precision of most of the float fields (so the export of a
  waterbalance configuration to DBF can match the precision of the import,
  which is supplied by Deltares).


0.2 (2012-05-09)
----------------

- Updated tasks to work with lizard-task 0.5.


0.1.16 (2012-05-09)
-------------------

- Fixes the import of the name of a bucket and a structure (note that this
  change also allows the import and change of an area name).

- Fixes the export of a bucket and a structure to DBF.


0.1.15 (2012-05-08)
-------------------

- Updates the task to validate the water balance configuration to use a
  case-insensitive search for the water manager.
- Renamed the dbf-fields of buckets in import_dbf.py due a conflict of
  global variables in FEWS, #104.
- Adds functionality to export a water balance configuration to a list instead
  of a DBF file (required to compute a diff of a new and an existing water
  balance configuration).


0.1.14 (2012-04-13)
-------------------

- Added code_delimeter to Structure and Bucket models as global class variable.

- Updated function 'last_areaobject_codenumber' to prevent of creation dublicate code for structures and buckets.


0.1.13 (2012-04-12)
-------------------

- Renamed properties in the task 'validate_wbconfiguration'.


0.1.12 (2012-04-12)
-------------------

- Added functionality to import wbconfigurations using validation configuration.

- Created task to validate wbconfigurations.

0.1.11 (2012-03-26)
-------------------

- Fixed error in task.


0.1.10 (2012-03-26)
-------------------

- Renamed celery tasks.

- Fixed type of levelno parameter in 'export_aanafvoergebieden' task.


0.1.9 (2012-03-26)
------------------

- Deleted ForeignKey-fields referenced to TimeSeriesCache.

- Created timeseries fields as CharField.

- Added 'fews_meta_info' field into AreaConfiguration, Structure,
  Bucket.

- Added task to import areaconfigurations from dbf.

- Created fixture lizard_wbconfiguration.json (local).

- Changes on AreaConfiguration models for fews.


0.1.8 (2012-02-13)
------------------

- Added functionality to view a summary of wbconfiguration.


0.1.7 (2012-02-13)
------------------

- Added functionality to export 'aanafvoergebieden' to dbf.


0.1.6 (2012-02-08)
------------------

- Added management command 'aanafvoergebieden_to_dbf'.

- Replaced option arguments by management command 'wbconfiguration_to_dbf'.


0.1.5 (2012-02-06)
------------------

- Added OS4 fields into AreaConfiguration, Bucket, Structure model.


0.1.4 (2012-01-23)
------------------

- Fixed problem of repeated columns in dbf (issue #3).

- Fixed problem with decimal field (issue #2).

- Changed code format for buckets and structures.

- Implemented lizard-security for AreaConfiguration, Bucket,
  Structure.

- Added x, y fields to Bucket, Structure, AreaConfiguration models.

- Added field ingebr into Bucket, Structure.

- Resized decimal fields to max_digits=10.

- Changed field in_out in Structure model.

- Added index field into WBConfigurationDBFMapping model to order fields.


0.1.3 (2011-12-09)
------------------

- Created task to export area configuraition periodically.

- Added functions to create bucket code.

- Added functionalities to export water balance area configurations
  into dbf.

- Added model DBFConfiguration to configure export to dbf.


0.1.2 (2011-12-07)
------------------
- Added functions to create structure code.

- Added function to create default structures.

- Added admin scherm to configure dbf fields.

- Created management command to create dbf file.

- Added functions to create dbf files.

- Added fixture 001_wbconfiguration.

- Implemented functions to view and maintain structures.

- Implemented functions to view and maintain buckets.

- Added deleted field into Bucket, Structure model.


0.1.1 (2011-11-07)
------------------

- Nothing changed yet.


0.1 (2011-11-07)
----------------

- Under construction.

- Initial library skeleton created by nensskel.  [your name]
