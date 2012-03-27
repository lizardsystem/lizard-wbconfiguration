#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.core.management.base import BaseCommand
from lizard_wbconfiguration.export_dbf import DBFExporter
from lizard_wbconfiguration.models import DBFConfiguration

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Exports water balance configuration into dbf file.
    """

    help = ("Example: bin/django wbconfiguration_to_dbf")

    def handle(self, *args, **options):
        self.export_configured_areaobjects()

    def export_configured_areaobjects(self):
        wb_dbf = DBFExporter()
        dbf_configurations = DBFConfiguration.objects.all()
        logger.info("%s water balance configurations to export." % len(
                dbf_configurations))
        for dbf_configuration in dbf_configurations:
            owner = dbf_configuration.data_set
            save_to = dbf_configuration.save_to
            filename = dbf_configuration.filename
            if dbf_configuration.dbf_type == 'AreaConfiguration':
                wb_dbf.export_areaconfiguration(owner, save_to, filename)
            elif dbf_configuration.dbf_type == 'Bucket':
                wb_dbf.export_bucketconfiguration(owner, save_to, filename)
            elif dbf_configuration.dbf_type == 'Structure':
                wb_dbf.export_structureconfiguration(owner, save_to, filename)
            else:
                logger.debug("UNKNOWN source %s" % dbf_configuration.dbf_type)
        logger.info("Export water balance configurations is finished.")
