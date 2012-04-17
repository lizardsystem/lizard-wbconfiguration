#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint: disable=C0111

# Copyright (c) 2012 Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

import logging
from zipfile import ZipFile

from celery.task import task

from lizard_portal.configurations_retriever import create_configurations_retriever
from lizard_portal.models import ConfigurationToValidate

from lizard_wbconfiguration.import_dbf import DBFImporter
from lizard_wbconfiguration.export_dbf import DBFExporter
from lizard_wbconfiguration.models import DBFConfiguration

from lizard_task.handler import get_handler


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
def validate_wbconfigurations(taskname="",
                              username=None,
                              levelno=20,
                              data_set=None,
                              configtype=None):
    """
    Import wb areaconfigurations from dbf using
    validation configurations.
    """
    action = 1
    v_configs = ConfigurationToValidate.objects.filter(
        data_set__name__iexact=data_set,
        config_type=configtype,
        action=action)
    v_configs = v_configs.exclude(file_path=None)
    handler = get_handler(taskname, username)
    logger = logging.getLogger(taskname)
    logger.addHandler(handler)
    logger.setLevel(int(levelno))
    validated = 0
    failed = 0
    logger.info("Start validation of wbconfigurations for '%s'." % data_set)
    for v_config in v_configs:
        dbfimporter = DBFImporter(logger)
        dbfimporter.fews_meta_info = v_config.fews_meta_info
        dbfimporter.areas_filepath = v_config.area_dbf
        dbfimporter.buckets_filepath = v_config.grondwatergebieden_dbf
        dbfimporter.structures_filepath = v_config.pumpingstations_dbf
        logger.debug(
            "Start validation of 'aanafvoergebied' ident '%s'." % v_config.area.ident)
        status = dbfimporter.import_areaconfigurations('AreaConfiguration', v_config)
        if isinstance(status, tuple) and status[0]:
            logger.debug("Start validation of 'grondwatergebieden'.")
            status = dbfimporter.import_buckets('Bucket', v_config)
        if isinstance(status, tuple) and status[0]:
            logger.debug("Start validation of 'kunstwerken'.")
            status = dbfimporter.import_structures('Structure', v_config)
        if isinstance(status, tuple) and status[0]:
            ConfigurationToValidate.objects.get(id=v_config.id).delete()
            validated = validated + 1
            logger.debug("Validated with SUCCESS.")
        else:
            v_config.action = 0
            if isinstance(status, tuple) and len(status) > 1:
                v_config.action_log = status[1][:256]
            else:
                v_config.action_log = "Error ...."
            v_config.save()
            failed = failed + 1
            logger.debug("Validated with ERRORS.")
    logger.info("Succeed=%s, Failed=%s." % (validated, failed))
    logger.info("End validation.")
    logger.removeHandler(handler)
    return "<<validate_wbconfigurations>>"


@task()
def validate_all():
    """Import all currently available configurations.

    This method is a spike to see whether the import of water balance
    configurations actually works. As such, it is clearly a work in progress:

      - there are no unit tests;
      - it only supports water balance configurations;
      - dbf files are extracted to a hard-coded directory;
      - dbf files are not removed after the import;
      - zip files are not removed after the import;
      - there is no error handling.

    """
    logger = logging.getLogger(__name__)
    handler = get_handler('validate_all', 'admin')
    logger.addHandler(handler)
    retriever = create_configurations_retriever()
    for configuration in retriever.retrieve_configurations():
        zip_file = ZipFile(configuration.zip_file_path)
        zip_file.extract('aanafvoer_waterbalans.dbf', '/tmp')
        zip_file.extract('grondwatergebieden.dbf', '/tmp')
        zip_file.extract('pumpingstations.dbf', '/tmp')
        dbfimporter = DBFImporter()
        dbfimporter.logger = logger
        dbfimporter.fews_meta_info = configuration.meta_info
        dbfimporter.areas_filepath = '/tmp/aanafvoer_waterbalans.dbf'
        dbfimporter.buckets_filepath = '/tmp/grondwatergebieden.dbf'
        dbfimporter.structures_filepath = '/tmp/pumpingstations.dbf'
        dbfimporter.import_dbf()
    logger.removeHandler(handler)


@task()
def export_wbconfigurations_to_dbf(
    data_set=None,
    levelno=20,
    username=None,
    taskname="wb_export_to_dbf_all"):
    """
    Export water balance configurations into dbf.
    Use logging handler of lizard_task app. to write message into database.

    Arguments:
    data_set -- name of organisation as DataSet in lizard_security
    levelno -- logging level as number, 10=debug, 20=info, ...
    """
    handler = get_handler(taskname, username)
    logger = logging.getLogger(taskname)
    logger.addHandler(handler)
    logger.setLevel(int(levelno))
    dbfexporter = DBFExporter(logger)
    dbf_configurations = DBFConfiguration.objects.exclude(dbf_type='Area')
    if data_set is not None:
        dbf_configurations = dbf_configurations.filter(data_set__name=data_set)
    for dbf_configuration in dbf_configurations:
        owner = dbf_configuration.data_set
        save_to = dbf_configuration.save_to
        filename = dbf_configuration.filename
        if dbf_configuration.dbf_type == 'AreaConfiguration':
            logger.info("Start export aanafvoergebieden for '%s'." % data_set)
            dbfexporter.export_areaconfiguration(owner, save_to, filename)
        elif dbf_configuration.dbf_type == 'Bucket':
            logger.info("Start export grondwatergebieden for '%s'." % data_set)
            dbfexporter.export_bucketconfiguration(owner, save_to, filename)
        elif dbf_configuration.dbf_type == 'Structure':
            logger.info("Start export grondwatergebieden for '%s'." % data_set)
            dbfexporter.export_structureconfiguration(owner, save_to, filename)
        else:
            logger.debug("UNKNOWN source %s" % dbf_configuration.dbf_type)
    logger.info("END EXPORT.")
    logger.removeHandler(handler)


@task()
def export_aanafvoergebieden_to_dbf(
    data_set=None,
    taskname='aanafvoegebieden_export_to_dbf_all',
    levelno=20,
    username=None):
    """
    Export geo info of 'aanafvoergebieden' into dbf.
    """
    handler = get_handler(taskname, username)
    logger = logging.getLogger(taskname)
    logger.addHandler(handler)
    logger.setLevel(int(levelno))
    dbfexporter = DBFExporter(logger)
    dbf_configurations = DBFConfiguration.objects.filter(dbf_type='Area')
    if data_set is not None:
        dbf_configurations = dbf_configurations.filter(data_set__name=data_set)
    logger.info("%s water balance configurations to export." % len(
            dbf_configurations))
    for dbf_configuration in dbf_configurations:
        owner = dbf_configuration.data_set
        save_to = dbf_configuration.save_to
        filename = dbf_configuration.filename
        if dbf_configuration.dbf_type == 'Area':
            dbfexporter.export_aanafvoergebieden(owner, save_to, filename)
    logger.info("Export water balance configurations is finished.")
    logger.removeHandler(handler)


@task()
def add():
    return "<<ADD task>>"


def run_export_task():
    """Run export_to_dbf task for HHNK."""
    kwargs = {"data_set": "Waternet"}
    export_wbconfigurations_to_dbf.delay(**kwargs)


def run_importdbf_task():
    """Run import_dbf task."""
    kwargs = {"fews_meta_info": "MARK",
              "areas_filepath": "/tmp/aanafvoer_waterbalans.dbf",
              "buckets_filepath": "/tmp/grondwatergebieden.dbf",
              "structures_filepath": "/tmp/pumpingstations.dbf"}
    import_dbf.delay(**kwargs)
