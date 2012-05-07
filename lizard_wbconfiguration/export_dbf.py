"""
API views not coupled to models.
"""
import os

from django.contrib.gis.geos import MultiPolygon
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos.point import Point

from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import StructureInOut
from lizard_wbconfiguration.models import WBConfigurationDBFMapping

from lizard_area.models import Area

from lizard_security.models import DataSet

from dbfpy.dbf import Dbf

import pkg_resources

import logging


class DBFExporter(object):
    """
    Creates a dbf file.
    """

    def __init__(self, logger=None):
        if logger is not None:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)

    def export_aanafvoergebieden(self, owner, save_to, filename):
        """Export areas into dbf."""
        filepath = self.file_path(save_to, filename)
        if owner is not None:
            areas = Area.objects.filter(data_set=owner)
        else:
            areas = Area.objects.exclude(data_set=None)
        areas = areas.exclude(area_class=Area.AREA_CLASS_KRW_WATERLICHAAM)

        success = self.create_dbf('area', areas, filepath)
        self.logger.debug("Status export areas is '%s' for %s to %s" % (
                success, owner, filepath))

    def export_areaconfiguration(self, owner, save_to, filename):
        """Export areaconfigurations into dbf."""
        filepath = self.file_path(save_to, filename)
        area_configurations = AreaConfiguration.objects.filter(data_set=owner)
        success = self.create_dbf('areaconfiguration',
                                  area_configurations,
                                  filepath)
        self.logger.debug("Status export areaconfig. is '%s' for %s to %s" % (
                success, owner.name, filepath))

    def export_bucketconfiguration(self, owner, save_to, filename):
        """Export buckets into dbf."""
        filepath = self.file_path(save_to, filename)
        buckets = Bucket.objects.filter(data_set=owner, deleted=False)
        success = self.create_dbf('bucket', buckets, filepath)
        self.logger.debug("Status export buckets is '%s' for %s into %s" % (
                success, owner.name, filepath))

    def export_structureconfiguration(self, owner, save_to, filename):
        """Export structures into dbf."""
        filepath = self.file_path(save_to, filename)
        structures = Structure.objects.filter(data_set=owner, deleted=False)
        success = self.create_dbf('structure', structures, filepath)
        self.logger.debug("Status export structure is '%s' for %s into %s" % (
                success, owner.name, filepath))

    def export_configuration_to_dbf(self, object_id):
        """
        Exports water balance configuration of passed area
        into 3 dbf files (AreaConfiguration, Bucket, Structure).
        """
        if object_id is None:
            return False

        area_configurations = AreaConfiguration.objects.filter(ident=object_id)
        if area_configurations.exists() == False:
            self.logger.debug('Water Balance configuration of area "%s" %s',
                         object_id, 'is NOT exists.')
            return False
        else:
            area_configuration = area_configurations[0]

            self.logger.debug("Export area configuration.")
            filename = self.create_filename('areaconfiguration')
            is_created_1 = self.create_dbf('areaconfiguration',
                                           [area_configuration],
                                           filename)

            buckets = Bucket.objects.filter(area=area_configuration)
            self.logger.debug("Export bucket.")
            filename = self.create_filename('bucket')
            is_created_2 = self.create_dbf('bucket', buckets, filename)

            structures = Structure.objects.filter(area=area_configuration)
            self.logger.debug("Export structure.")
            filename = self.create_filename('structure')
            is_created_3 = self.create_dbf('structure', structures, filename)
            if is_created_1 and is_created_2 and is_created_3:
                return True
            else:
                return False

    def file_path(self, save_to, filename):
        success = True
        if not os.path.exists(save_to):
            self.logger.error("Path %s not exists" % save_to)
            success = False

        if filename is None or len(filename) < 1:
            self.logger.error("File name is not exists")
            success = False

        if success:
            filename = ".".join((filename, 'dbf'))
            filepath = os.path.abspath(os.path.join(save_to, filename))
        else:
            filepath = self.create_filename('')
        return filepath

    def create_filename(self, modul_name):
        default_filename = 'not_configured.dbf'
        default_dbfdir = 'media/lizard_wbconfiguration/dbf'
        default_package = 'lizard_wbconfiguration'
        filenames = {
            'areaconfiguration': 'area_configuration.dbf',
            'structure': 'structures.dbf',
            'bucket': 'buckets.dbf'}

        if pkg_resources.resource_isdir(default_package,
                                        default_dbfdir):
            dbf_dir_path = pkg_resources.resource_filename(default_package,
                                                           default_dbfdir)

            filename = '%s/%s' % (dbf_dir_path, filenames.get(
                    modul_name, 'not_configured.dbf'))
            self.logger.info("File to save %s.", filename)
            return filename
        else:
            self.logger.debug('Location to write .dbf files is not defined.')
            self.logger.debug(
                'Used default file name "%s".' % default_filename)
            return default_filename

    def create_dbf(self, model_name, area_objects, filename):
        """
        Creates a dbf file.
        """
        success = False

        mapping = WBConfigurationDBFMapping.objects.filter(
            model_name__iexact=model_name).order_by('index')

        try:
            self.logger.info("Create en open dbf file='%s'." % filename)
            self.create_out(filename)
            self.logger.info("Add fields.")
            self.fields_to_dbf(mapping)
            self.logger.info("Store '%s' '%s'." % (
                    len(area_objects), model_name))
            self.store_data(area_objects, mapping)
            self.logger.info("Close file.")
            self.close_out()
            success = True
        except Exception as ex:
            self.logger.error(','.join(map(str, ex.args)))
        return success

    def fields_to_dbf(self, mapping):
        """
        Adds fields into dbf file.
        """
        for item in mapping:
            field_options = [str(item.dbffield_name),
                             str(item.dbffield_type)]
            print field_options
            if item.dbffield_length is not None:
                field_options.append(item.dbffield_length)
            if item.dbffield_decimals is not None:
                field_options.append(item.dbffield_decimals)
            self.add_field_out(field_options)

    def store_data(self, area_objects, mapping):
        """
        Store data into dbf file.
        """
        for area_object in area_objects:
            rec = self.new_record()
            for item in mapping:
                value = self.retrieve_value(area_object,
                                            item.wbfield_name.lower())
                if value is not None:
                    dbffield_name = item.dbffield_name.lower()
                    if dbffield_name == 'x' and isinstance(value, Point):
                        value = value.x
                    if dbffield_name == 'y' and isinstance(value, Point):
                        value = value.y

                    rec[dbffield_name] = value

            self.store_record(rec)

    def retrieve_value(self, area_object, field_name):
        """Return the value

        Arguments:
        area_object -- the instance object of a model
        field_name -- field name
        """
        if not hasattr(area_object, field_name):
            self.logger.debug("%s has not attribute %s" % (
                    area_object._meta.module_name, field_name))
            return None

        value = getattr(area_object, field_name)
        if value is None:
            self.logger.debug("Value of %s.%s is None." % (
                    area_object._meta.module_name, field_name))
            return None
        if isinstance(value, Area):
            if field_name.lower() == 'parent':
                value = value.ident
            else:
                value = value.id
        elif isinstance(value, BucketsType):
            value = value.code
        elif isinstance(value, StructureInOut):
            value = bool(value.index)
        elif isinstance(value, MultiPolygon):
            value = self.get_centrpoint(value)
        elif isinstance(value, Polygon):
            value = self.get_centrpoint(value)
        elif isinstance(value, DataSet):
            value = str(value.name)
        elif isinstance(value, unicode):
            value = value
        else:
            value = value
        return value

    def get_centrpoint(self, geometry):
        """Retrieve center point of geometry,
        transform the gometry to srid=28992."""
        srid = 28992
        if geometry.srid != srid:
            geometry_clone = geometry.transform(srid, clone=True)
            return geometry_clone.centroid

    def create_out(self, file_path):
        self.out = Dbf(file_path, new=True)

    def add_field_out(self, field_options):
        self.out.addField(tuple(field_options))

    def close_out(self):
        self.out.close()

    def new_record(self):
        return self.out.newRecord()

    def store_record(self, rec):
        rec.store()


class WbExporterToDict(DBFExporter):
    """Implements the export of a DBF to a dictionary."""

    def __init__(self, *args, **kwargs):
        DBFExporter.__init__(self, *args, **kwargs)

    def file_path(self, save_to, filename):
        return "don't care"

    def create_out(self, file_path):
        self.out = []

    def add_field_out(self, field_options):
        pass

    def close_out(self):
        pass

    def new_record(self):
        return {}

    def store_record(self, rec):
        # rec is a dictionary whose keys specify the field names of DBF
        # files. As the keys will be compared to the field names, we upper case
        # the keys explicitly.
        self.out.append(dict((k.upper(), v) for k, v in rec.items()))
