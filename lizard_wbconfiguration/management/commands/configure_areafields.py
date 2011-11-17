#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from optparse import make_option

from django.core.management.base import BaseCommand
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import AreaField

from django.db import transaction

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Set field names of AreaConfiguration clases
    into AreaField model.
    """

    help = ("Example: bin/django configure_areagrid "\
            "")

    option_list = BaseCommand.option_list + (
        make_option('--class_name',
                    help='Not implemented',
                    type='str',
                    default=None),
        make_option('--destination',
                    help='Not implemented',
                    type='str',
                    default=None))

    @transaction.commit_on_success
    def handle(self, *args, **options):

        area = AreaConfiguration()
        for k in area.__dict__.keys():
            AreaField.objects.create(field_name=k)
            logger.debug('Inserting "%s" field', k)
