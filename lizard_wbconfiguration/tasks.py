#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint: disable=C0111

# Copyright (c) 2012 Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

import logging
from zipfile import ZipFile

from celery.task import task
from django.core import management

from lizard_portal.configurations_retriever import create_configurations_retriever

from lizard_wbconfiguration.import_dbf import DBFImporter
from lizard_wbconfiguration.api.views import  WaterBalanceDBF
from lizard_wbconfiguration.models import DBFConfiguration

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
    retriever = create_configurations_retriever()
    for configuration in retriever.retrieve_configurations():
        zip_file = ZipFile(configuration.zip_file_path)
        zip_file.extract('aanafvoer_waterbalans.dbf', '/tmp')
        zip_file.extract('grondwatergebieden.dbf', '/tmp')
        zip_file.extract('pumpingstations.dbf', '/tmp')
        dbfimporter = DBFImporter()
        dbfimporter.fews_meta_info = configuration.meta_info
        dbfimporter.areas_filepath = '/tmp/aanafvoer_waterbalans.dbf'
        dbfimporter.buckets_filepath = '/tmp/grondwatergebieden.dbf'
        dbfimporter.structures_filepath = '/tmp/pumpingstations.dbf'
        dbfimporter.import_dbf()


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
    kwargs = {"data_set": "Waternet"}
    export_to_dbf.delay(**kwargs)


def run_importdbf_task():
    """Run import_dbf task."""
    kwargs = {"fews_meta_info": "INFO2",
              "areas_filepath": "/tmp/aanafvoer_waterbalans.dbf",
              "buckets_filepath": "/tmp/grondwatergebieden.dbf",
              "structures_filepath": "/tmp/pumpingstations.dbf"}
    import_dbf.delay(**kwargs)
