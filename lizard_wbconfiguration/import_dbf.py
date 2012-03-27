"""
Import WB configurations.
"""
import datetime
import logging

from decimal import Decimal
from dbfpy.dbf import Dbf

from django.db.models import FieldDoesNotExist
from django.db.models.fields import DecimalField

from lizard_area.models import Area
from lizard_wbconfiguration.api.views import WaterBalanceAreaConfiguration
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import StructureInOut
from lizard_wbconfiguration.models import WBConfigurationDBFMapping


class DBFImporter(object):
    """
    Import wb areaconfigurations from dbf files.
    """

    def __init__(self):
        self.areas_filepath = None
        self.buckets_filepath = None
        self.structures_filepath = None
        self.fews_meta_info = None
        self.logger = logging.getLogger(__name__)
        self.read_only_fields = ('id', 'ident', 'data_set', 'area',
                                 'x', 'y', 'name', 'code')

    def import_dbf(self):
        """
        Run imports for 'aanafvoergebieden',
        'grondwatergebieden' and 'pumpingstations'.
        """
        if self.areas_filepath is None:
            self.logger.error("Filepath for 'aanafvoergebieden' does NOT set.")
            return
        if self.buckets_filepath is None:
            self.logger.error(
                "Filepath for 'grondwatergebieden' does NOT set.")
            return
        if self.structures_filepath is None:
            self.logger.error("Filepath for 'pumpingstations' does NOT set.")
            return

        self._import_areaconfigurations('AreaConfiguration')
        self._import_buckets('Bucket')
        self._import_structures('Structure')

    def _retrieve_importvalue(self, rec, mapping, model_object):
        """Retrieve a value from dbf record.

        Arguments:
        rec -- instance of DbfRecord object
        mapping -- instance of mapping object contening a field to import
        model_object -- instance of AreaConfigueration, Bucket or Structure object.
        """
        try:
            value = rec[mapping.dbffield_name]
            model_field = model_object._meta.get_field_by_name(
                mapping.wbfield_name)[0]
            if isinstance(value, float) and isinstance(
                model_field, DecimalField):
                return Decimal(str(value))
            if model_field.rel is not None:
                if model_field.rel.to == BucketsType:
                    bucket_types = BucketsType.objects.filter(
                        code=value)
                    if not bucket_types.exists():
                        self.logger.error("BucketType %s not exists" % value)
                        return
                    return bucket_types[0]
                elif model_field.rel.to == StructureInOut:
                    structure_inout = StructureInOut.objects.filter(
                        index=value)
                    if not structure_inout.exists():
                        self.logger.error("StructureInOut %s not exists" % (
                                value))
                        return
                    return structure_inout[0]
            return value
        except FieldDoesNotExist as ex:
            self.logger.error(','.join(map(str, ex.args)))
        except ValueError as ex:
            self.logger.error(','.join(map(str, ex.args)))
        except Exception as ex:
            self.logger.error(','.join(map(str, ex.args)))

    def _import_buckets(self, model_name):
        """Import buckets from dbf.
        Omit not existing objects.

        Arguments:
        model_name -- name of model as string 'Bucket'
        """
        mapping = WBConfigurationDBFMapping.objects.filter(
            model_name=model_name)

        db = Dbf(self.buckets_filepath)
        for rec in db:
            bucket = self._get_bucket(rec['GEBIED'], rec['ID'])
            if bucket is None:
                continue
            for item in mapping:
                if item.wbfield_name.lower() in self.read_only_fields:
                    self.logger.debug(
                        "Omit readonly field, dbf_fieldname='%s'." % (
                            item.wbfield_name))
                    continue
                try:
                    value = self._retrieve_importvalue(rec, item, bucket)
                    self.logger.debug("Set value='%s' of dbffield='%s' "\
                                          "in modelfield='%s'." % (
                            value, item.dbffield_name, item.wbfield_name))
                    if value is not None:
                        setattr(bucket, item.wbfield_name, value)
                except ValueError as ex:
                    self.logger.error(','.join(map(str, ex.args)))
                except Exception as ex:
                    self.logger.error(','.join(map(str, ex.args)))
            bucket.fews_meta_info = self.fews_meta_info
            bucket.save()
        db.close()

    def _import_structures(self, model_name):
        """Import structures from dbf.
        Omit not existing objects.

        Arguments:
        model_name -- name of model as string, 'Structure'
        """
        mapping = WBConfigurationDBFMapping.objects.filter(
            model_name=model_name)

        db = Dbf(self.structures_filepath)
        for rec in db:
            structure = self._get_structure(rec['GEBIED'], rec['ID'])
            if structure is None:
                continue
            for item in mapping:
                if item.wbfield_name.lower() in self.read_only_fields:
                    self.logger.debug(
                        "Omit readonly field, dbf_fieldname='%s'." % (
                            item.wbfield_name))
                    continue
                try:
                    value = self._retrieve_importvalue(rec, item, structure)
                    self.logger.debug(
                        "Set value='%s' of dbffield='%s' into modelfield='%s'." % (
                            value, item.dbffield_name, item.wbfield_name))
                    if value is not None:
                        setattr(structure, item.wbfield_name, value)
                except ValueError as ex:
                    self.logger.error(','.join(map(str, ex.args)))
                except Exception as ex:
                    self.logger.error(','.join(map(str, ex.args)))
            structure.fews_meta_info = self.fews_meta_info
            structure.save()
        db.close()

    def _import_areaconfigurations(self, model_name):
        """Import areaconfigurations from dbf.
        Omit not existing objects.

        Arguments:
        model_name -- name of model as string, 'AreaConfiguration'
        """
        mapping = WBConfigurationDBFMapping.objects.filter(
            model_name=model_name)

        db = Dbf(self.areas_filepath)

        for rec in db:
            areaconfiguration = self._get_areaconfiguration(rec['GAFIDENT'])
            if areaconfiguration is None:
                continue
            for item in mapping:
                if item.wbfield_name.lower() in self.read_only_fields:
                    self.logger.debug(
                        "Omit readonly field dbf_fieldname='%s'." % (
                            item.wbfield_name))
                    continue
                try:
                    value = self._retrieve_importvalue(
                        rec, item, areaconfiguration)
                    self.logger.debug(
                        "Set value='%s' of dbffield='%s' in modelfield='%s'." % (
                            value, item.dbffield_name, item.wbfield_name))
                    if value is not None:
                        setattr(areaconfiguration, item.wbfield_name, value)
                except ValueError as ex:
                    self.logger.error(','.join(map(str, ex.args)))
                except Exception as ex:
                    self.logger.error(','.join(map(str, ex.args)))
            areaconfiguration.fews_meta_info = self.fews_meta_info
            areaconfiguration.save()
        db.close()

    def _get_structure(self, ident, code):
        """Return the Structure with the given code.

        If no Structure exists with the given code and no AreaConfiguration
        exists with the given ident, this method returns None.

        Arguments:
          *ident*
            ident of the AreaConfiguration to which the Structure belongs
          *code*
            code of the Structure

        """
        try:
            structure = Structure.objects.get(code=code)
        except Structure.DoesNotExist:
            self.logger.debug(
                "Structure with '%s' does NOT exist. Try to create one." % code)
            try:
                area_config = AreaConfiguration.objects.get(ident=ident)
            except AreaConfiguration.DoesNotExist:
                self.logger.warning("We cannot create a Structure for the "
                                    "non-existing AreaConfiguration with ident "
                                    "'%s'." % ident)
                return None
            structure = Structure(name='', code=code, area=area_config,
                data_set=area_config.data_set)
            structure.save()
        return structure

    def _get_bucket(self, ident, code):
        """Return the Bucket with the given code.

        If no Bucket exists with the given code and no AreaConfiguration exists
        with the given ident, this method returns None.

        Arguments:
          *ident*
            ident of the AreaConfiguration to which the bucket belongs
          *code*
            code of the Bucket

        """
        try:
            bucket = Bucket.objects.get(code=code)
        except Bucket.DoesNotExist:
            self.logger.debug(
                "Bucket with '%s' does NOT exist. Try to create one." % code)
            try:
                area_config = AreaConfiguration.objects.get(ident=ident)
            except AreaConfiguration.DoesNotExist:
                self.logger.warning("We cannot create a Bucket for the "
                                    "non-existing AreaConfiguration with ident "
                                    "'%s'." % ident)
                return None
            bucket = Bucket(name='', code=code, area=area_config,
                data_set=area_config.data_set)
            bucket.save()
        return bucket

    def _get_areaconfiguration(self, ident):
        """ Return the AreaConfiguration with the given ident.

        Arguments:
          *ident*
            ident of Area object like '2103'

        """
        try:
            return AreaConfiguration.objects.get(ident=ident)
        except:
            self.logger.debug("AreaConfiguration ident='%s' does NOT exist. Try to create one." % ident)
            return WaterBalanceAreaConfiguration.create(ident)
