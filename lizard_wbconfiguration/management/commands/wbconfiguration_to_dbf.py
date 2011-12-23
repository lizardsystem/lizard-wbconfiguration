#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from optparse import make_option

from django.core.management.base import BaseCommand
from lizard_wbconfiguration.api.views import WaterBalanceDBF
from lizard_wbconfiguration.models import DBFConfiguration

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Exports water balance configuration into dbf file.
    """

    help = ("Example: bin/django wbconfiguration_to_dbf --ident=ident")

    option_list = BaseCommand.option_list + (
        make_option('--ident',
                    help='Ident of area configuration',
                    type='str',
                    default=None),)

    def handle(self, *args, **options):
        if options['ident'] is not None:
            self.export_all_areaobjects(options['ident'])
        else:
            self.export_configured_areaobjects()

    def export_configured_areaobjects(self):
        wb_dbf = WaterBalanceDBF()
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

    def export_all_areaobjects(self, ident):
        wb_dbf = WaterBalanceDBF()
        wb_dbf.export_configuration_to_dbf(ident)
