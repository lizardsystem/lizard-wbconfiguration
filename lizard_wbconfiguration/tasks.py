from celery.task import task
from django.core import management

from lizard_wbconfiguration.import_dbf import DBFImporter
from lizard_wbconfiguration.api.views import  WaterBalanceDBF
from lizard_wbconfiguration.models import DBFConfiguration

import logging


@task()
def export_wbconfigurations_to_dbf():
    """
    Export water balance configurations into dbf.
    """
    management.call_command('wbconfiguration_to_dbf')


@task()
def import_dbf(fews_meta_info=None,
               areas_filepath=None,
               buckets_filepath=None,
               structures_filepath=None):
    """
    Import wb areaconfigurations from dbf.
    """
    dbfimporter = DBFImporter()
    dbfimporter.fews_meta_info = fews_meta_info
    dbfimporter.areas_filepath = areas_filepath
    dbfimporter.buckets_filepath = buckets_filepath
    dbfimporter.structures_filepath = structures_filepath
    dbfimporter.import_dbf()
    return "<<import dbf>>"


@task()
def export_to_dbf(data_set=None):
    """
    Export water balance configurations into dbf.
    """
    logger = logging.getLogger(__name__)
    dbfexporter = WaterBalanceDBF()
    dbf_configurations = DBFConfiguration.objects.all()
    if data_set is not None:
        dbf_configurations = dbf_configurations.filter(data_set__name=data_set)
    logger.info("%s water balance configurations to export." % len(
            dbf_configurations))
    for dbf_configuration in dbf_configurations:
        owner = dbf_configuration.data_set
        save_to = dbf_configuration.save_to
        filename = dbf_configuration.filename
        if dbf_configuration.dbf_type == 'AreaConfiguration':
            dbfexporter.export_areaconfiguration(owner, save_to, filename)
        elif dbf_configuration.dbf_type == 'Bucket':
            dbfexporter.export_bucketconfiguration(owner, save_to, filename)
        elif dbf_configuration.dbf_type == 'Structure':
            dbfexporter.export_structureconfiguration(owner, save_to, filename)
        else:
            logger.debug("UNKNOWN source %s" % dbf_configuration.dbf_type)
    logger.info("Export water balance configurations is finished.")


@task()
def add():
    return "<<ADD task>>"


def run_export_task():
    """Run export_to_dbf task for HHNK."""
    from celery.execute import send_task
    kwargs = {"data_set": "HHNK"}
    export_to_dbf.delay(**kwargs)


def run_importdbf_task():
    """Run import_dbf task."""
    from celery.execute import send_task
    kwargs = {"fews_meta_info": "INFO2",
              "areas_filepath": "/tmp/aanafvoer_waterbalans.dbf",
              "buckets_filepath": "/tmp/grondwatergebieden.dbf",
              "structures_filepath": "/tmp/pumpingstations.dbf"}
    import_dbf.delay(**kwargs)
