from celery.task import task
from django.core import management


@task()
def export_wbconfigurations_to_dbf():
    """
    Export water balance configurations into dbf.
    """
    management.call_command('wbconfiguration_to_dbf')
