#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from optparse import make_option

from django.core.management.base import BaseCommand
from lizard_wbconfiguration.models import AreaField

from django.db import transaction
from django.db.models import get_model


import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    (Remove and re-)insert model field names to wb configuration.
    """

    help = ("Example: bin/django wb_configuration --app=app "\
                "--model_name=model")

    option_list = BaseCommand.option_list + (
        make_option('--app',
                    help='app',
                    type='str',
                    default=None),
        make_option('--model_name',
                    help='Model name.',
                    type='str',
                    default=None))

    @transaction.commit_on_success
    def handle(self, *args, **options):
        if not options['app'] or not options['model_name']:
            logger.error("Expected --app and --model args. "\
                             "Use -help for example.")
            return

        model = get_model(options['app'], options['model_name'])
        for field in model._meta.fields:
            code = ".".join([options['app'],
                             options['model_name'],
                             field.name])
            AreaField.objects.get_or_create(
                code=code,
                app_name=options['app'].lower(),
                model_name=options['model_name'].lower(),
                field_name=field.name)
            logger.debug('Inserting "%s" field', field.name)
