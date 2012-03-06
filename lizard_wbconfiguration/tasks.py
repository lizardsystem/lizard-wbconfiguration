from celery.task import task
from django.core import management

from lizard_wbconfiguration.import_dbf import DBFImporter


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
    dbfimporter.areas_filepath=areas_filepath,
    dbfimporter.buckets_filepath=buckets_filepath,
    dbfimporter.structures_filepath=structures_filepath
    dbfimporter.import_dbf()
    return "<<import dbf>>"


def run_importdbf_task():
    from celery.execute import send_task
    kwargs = {fews_meta_info="INFO",
              areas_filepath=None,
              buckets_filepath=None,
              structures_filepath=None}
    send_task("lizard_wbconfiguration.tasks.import_dbf", kwargs=kwargs)

