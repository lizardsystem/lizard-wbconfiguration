Changelog of lizard-wbconfiguration
===================================================


0.1.5 (unreleased)
------------------

- Nothing changed yet.


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
