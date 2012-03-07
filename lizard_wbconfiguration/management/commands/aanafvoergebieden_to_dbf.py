#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.core.management.base import BaseCommand
from lizard_wbconfiguration.api.views import WaterBalanceDBF
from lizard_wbconfiguration.models import DBFConfiguration

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Exports 'aanafvoergebieden into dbf file.
    """

    help = ("Example: bin/django aanafvoergebieden_to_dbf")

    def handle(self, *args, **options):
        self.export_configured_areaobjects()

    def export_configured_areaobjects(self):
        wb_dbf = WaterBalanceDBF()
        dbf_configurations = DBFConfiguration.objects.filter(dbf_type="Area")
        logger.info("%s area's configurations to export." % len(
                dbf_configurations))
        for dbf_configuration in dbf_configurations:
            owner = dbf_configuration.data_set
            save_to = dbf_configuration.save_to
            filename = dbf_configuration.filename
            wb_dbf.export_aanafvoergebieden(owner, save_to, filename)
        logger.info("Export of 'aanafvoergebieden' is finished.")
