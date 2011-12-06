#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from optparse import make_option

from django.core.management.base import BaseCommand
from lizard_wbconfiguration.api.views import WaterBalanceDBF

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
        if not options['ident']:
            logger.error("Expected --ident arg. Use -help for example.")
            return

        wb_dbf = WaterBalanceDBF()
        wb_dbf.export_configuration_to_dbf(options['ident'])
