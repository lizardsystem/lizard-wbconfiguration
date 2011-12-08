"""
API views not coupled to models.
"""
import sys
import datetime

from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.db.models.fields import DateTimeField
from django.db.models.fields import BooleanField

from djangorestframework.views import View
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import AreaGridFieldConfiguration
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import WBConfigurationDBFMapping
from lizard_wbconfiguration import models

from lizard_area.models import Area

from lizard_fewsnorm.models import TimeSeriesCache
from lizard_fewsnorm.models import Series

from dbfpy.dbf import Dbf

import pkg_resources

import logging
logger = logging.getLogger(__name__)


class RootView(View):
    """
    Startpoint.
    """
    def get(self, request):
        return {
            "root": reverse(
                'lizard_wbconfiguration_api_root'),
            }


class WaterBalanceDBF(View):
    """
    Creates a dbf file.
    """

    def post(self, request):
        """
        Creates a dbf files.
        """
        object_id = self.CONTENT.get('object_id', None)
        success = self.export_configuration_to_dbf(object_id)
        return {'success': success}

    def export_configuration_to_dbf(self, object_id):
        """
        Exports water balance configuration of passed area
        into 3 dbf files (AreaConfiguration, Bucket, Structure).
        """
        if object_id is None:
            return False

        area_configurations = AreaConfiguration.objects.filter(ident=object_id)
        if area_configurations.exists() == False:
            logger.debug('Water Balance configuration of area "%s" %s',
                         object_id, 'is NOT exists.')
            return False
        else:
            area_configuration = area_configurations[0]

            logger.debug("Export area configuration.")

            is_created_1 = self.create_dbf('areaconfiguration',
                                           [area_configuration])

            buckets = Bucket.objects.filter(area=area_configuration)
            logger.debug("Export bucket.")
            is_created_2 = self.create_dbf('bucket', buckets)

            structures = Structure.objects.filter(area=area_configuration)
            logger.debug("Export structure.")
            is_created_3 = self.create_dbf('structure', structures)

            if is_created_1 and is_created_2 and is_created_3:
                return True
            else:
                return False

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
            logger.info("File to save %s.", filename)
            return filename
        else:
            logger.debug('Location to write .dbf files is not defined.')
            logger.debug('Used default file name "%s".' % default_filename)
            return default_filename

    def create_dbf(self, model_name, area_objects):
        """
        Creates a dbf file.
        """
        success = False
        filename = self.create_filename(model_name)

        mapping = WBConfigurationDBFMapping.objects.filter(
            model_name__iexact=model_name)

        try:
            logger.debug("Create en open dbf file.")
            out = Dbf(filename, new=True)
            logger.debug("Add fields.")
            self.fields_to_dbf(area_objects, mapping, out)
            logger.debug("Store data.")
            self.store_data(area_objects, mapping, out)
            logger.debug("Close file.")
            out.close()
            success = True
        except IOError as ex:
            logger.error("%s, %s, %s" % (ex.message, ex.filename, ex.strerror))
        except ValueError as ex:
            logger.error("%s" % (ex.message))
        except:
            logger.error("Unexpected error: %s", sys.exc_info()[0])

        return success

    def fields_to_dbf(self, area_objects, mapping, out):
        """
        Adds fields into dbf file.
        """
        for area_object in area_objects:
            print len(mapping)
            for item in mapping:
                field_options = [str(item.dbffield_name),
                                 str(item.dbffield_type)]
                if item.dbffield_decimals is not None:
                    field_options.append(item.dbffield_decimals)
                if item.dbffield_length is not None:
                    field_options.append(item.dbffield_length)
                out.addField(tuple(field_options))

    def store_data(self, area_objects, mapping, out):
        """
        Store data into dbf file.
        """
        for area_object in area_objects:
            rec = out.newRecord()
            for item in mapping:
                value = self.retrieve_value(area_object,
                                            item.wbfield_name.lower())
                if value is not None:
                    rec[item.dbffield_name] = value
            rec.store()

    def retrieve_value(self, area_object, field_name):
        """Return the value

        Arguments:
        area_object -- the instance object of a model
        field_name -- field name
        """
        if not hasattr(area_object, field_name):
            logger.debug("%s has not attribute %s" % (
                    area_object._meta.module_name, field_name))
            return None
        value = getattr(area_object, field_name)
        if value is None:
            logger.debug("Value of %s.%s is None." % (
                    area_object._meta.module_name, field_name))
            return None
        if isinstance(value, TimeSeriesCache):
            value = str(value.parametercache.ident)
        elif isinstance(value, Area):
            value = value.id
        elif isinstance(value, BucketsType):
            value = value.name
        elif isinstance(value, unicode):
            value = str(value)
        elif isinstance(value, bool):
            value = 1 if value else 0
        else:
            value = value
        return value

    def retrieve_series_key(self, ts_cache):
        """Retrieve series key.

        Arguments:
        ts_cache -- the instance object of TimeSeriesCache type

        """
        db_source = ts_cache.geolocationcache.fews_norm_source
        series = Series.objects.using(db_source.name).get(
            location__id=ts_cache.geolocationcache.ident,
            parameter__id=ts_cache.parametercache.ident,
            moduleinstance__id=ts_cache.modulecache.ident,
            timestep__id=ts_cache.timestepcache.ident)
        return series.serieskey


class WaterBalanceAreaObjectConfiguration(View):
    """
    View and save the area configuration objects.
    Buckets and Structures.
    Area configuration contains 2 default structures(in, out).
    """

    def get(self, request):
        object_id = request.GET.get('object_id', None)
        area_object_type = request.GET.get('area_object_type', None)
        area_object_class = self.areaobject_class(area_object_type)

        if area_object_class is None:
            return {'data': []}

        if area_object_class == Structure:
            self.create_default_structures(object_id)

        area_objects = area_object_class.objects.filter(
            area__ident=object_id,
            deleted=False)

        return {'data': self.areaobject_configuration(list(area_objects))}

    def areaobject_class(self, area_object_type):
        try:
            if area_object_type.lower() == 'bucket':
                return getattr(models, "Bucket")
            elif area_object_type.lower() == 'structure':
                return getattr(models, "Structure")
            else:
                logger.debug("UNKNOWN area object type '%s'.",
                             area_object_type)
                return None
        except AttributeError:
            logger.debug("UNKNOWN area object type '%s'.", area_object_type)
            return None

    def areaobject_configuration(self, area_objects):
        """
        Creates list of dictionaries like
        [{key: value, key: value,},{key: value,},]
        """
        area_object_config = []
        for area_object in area_objects:
            area_object_as_dict = {}
            for field in area_object._meta.fields:
                if field.rel:
                    value = str(getattr(area_object, field.name))
                else:
                    value = field.value_from_object(area_object)
                area_object_as_dict[field.name] = value
            area_object_config.append(area_object_as_dict)
        return area_object_config

    def check_amount_structures(self, area_configuration):
        """Check allowed amount structures per area."""
        amount = 10
        structures = Structure.objects.filter(
            area__id=area_configuration.id,
            deleted=False)
        if len(structures) >= amount:
            logger.debug("Amount of structures is %d allowed %d, area %s" % (
                    len(structures), amount, area_configuration.ident))
            return False
        return True

    def exists_default_structure(self, area_configuration, in_out):
        """ Check and activate default structures. """
        structures = Structure.objects.filter(in_out=in_out,
                                              area__id=area_configuration.id,
                                              is_computed=True)
        print "%s AANTAL DEFAULT STRUCTURES %d" % (in_out, len(structures))
        for structure in structures:
            if structure.deleted == True:
                structure.deleted = False
                structure.save()

        if structures.exists():
            return True
        return False

    def create_default_structure(self, area_configuration, in_out):
        """Creates default structure.

        Arguments:
        area_configuration -- the object instance of AreaConfiguratin
        in_out -- the string choices see above STUCTURE_IN_OUT
        """
        names = {'in': "Peilhandhaving In defaul",
                 'uit': "Peilhandhaving Out default"}
        try:
            structure = Structure(name=names[in_out],
                                  in_out=in_out,
                                  area=area_configuration,
                                  is_computed=True)
            last_codenumber = self.last_structure_codenumber(
                area_configuration)
            if last_codenumber is None:
                last_codenumber = structure.code_number()
            structure.code = structure.create_code(last_codenumber + 1)
            structure.save()
        except Exception as ex:
            logger.debug(','.join(map(str, ex.args)))

    def create_default_structures(self, object_id):
        area_config = AreaConfiguration.objects.get(ident=object_id)
        in_out = ('in', 'uit')

        for item in in_out:
            if self.check_amount_structures(area_config) == False:
                break
            if not self.exists_default_structure(area_config, item):
                self.create_default_structure(area_config, item)

    def last_structure_codenumber(self, area_configuration):
        """ Return code number of the last structure. """
        structures = Structure.objects.filter(
            area__id=area_configuration.id)
        number = None
        if structures.exists():
            last_structure = structures.order_by('-id')[0]
            number = last_structure.code_number()
        return number

    def str2bool(self, value):
        mapping = {'false': False, 'true': True}
        return mapping[value.lower()]

    def retrieve_id(self, record):
        """
        Retrieve and cast to integer id element
        from record object.
        """
        if type(record) == dict:
            id = record.get('id', None)
            try:
                return int(id)
            except ValueError:
                logger.debug("Area  '%s' is NOT an integer", id)
                return -1

    def create_areaobject(self, area, areaobject_class):
        """
        Create a area object related to AreaConfiguration.
        Set code into the object.
        """
        print "create_areaobject %s" % area.ident
        area_object = areaobject_class(area=area)
        print "Area object of %s." % area.ident
        if isinstance(area_object, Structure):
            if self.check_amount_structures(area) == False:
                return None
            last_codenumber = self.last_structure_codenumber(area)
            if last_codenumber is None:
                last_codenumber = area_object.code_number()

            area_object.code = area_object.create_code(last_codenumber + 1)
            area_object.save()
        return area_object

    def delete_areaobjects(self, data, areaobject_class):
        """Deactivate area objects exclusive computed structures."""
        success = True
        try:
            for record in data:
                areaobject_id = self.retrieve_id(record)
                print areaobject_class
                area_objects = areaobject_class.objects.filter(
                    id=areaobject_id)
                print len(area_objects)
                if not area_objects.exists():
                    continue
                area_object = area_objects[0]
                print area_object.code
                print type(area_object) == Structure and area_object.is_computed
                if type(area_object) == Structure and area_object.is_computed:
                    continue
                area_object.deleted = True
                area_object.save()
        except:
                success = False
        return success

    def create_areaobjects(self, data, area, areaobject_class):
        """Create area object."""
        touched_objects = []
        success = True
        for record in data:
            if 'id' in record.keys():
                del record['id']
            print "objects "
            area_object = self.create_areaobject(area, areaobject_class)
            if area_object is None:
                success = False
                continue
            if not self.update_areaobject(record, area_object):
                print "SSSSSSSSSSSSSSSSS"
                success = False
            print "Starting save"

            #self.area_object.save()
            print "END Save"
            touched_objects.append(area_object)
        return (success, touched_objects)

    def update_areaobjects(self, data, areaobject_class):
        print "UPDATES"
        touched_objects = []
        success = True
        for record in data:
            print "ID"
            areaobject_id = self.retrieve_id(record)
            print areaobject_id
            area_objects = areaobject_class.objects.filter(id=areaobject_id)
            if not area_objects.exists():
                logger.error("%s with id=%s not exists." % (
                        areaobject_class._meta.module_name, areaobject_id))
                success = False
                continue
            area_object = area_objects[0]
            print "UPDATE OB.%s" % area_object.code
            if not self.update_areaobject(record, area_object):
                print "ACTI TRUE"
                success = False
            touched_objects.append(area_object)
        return (success, touched_objects)

    def update_areaobject(self, record, area_object):
        """Set values into area object.
        @TODO replace value.split(',')[2] with timeseriescache.id.
        """
        success = True
        for (key, value) in record.items():
            key = str(key)
            value = str(value)
            print "%s %s" % (key, value)
            if value == "" or value == "None":
                continue
            try:
                areaobject_field = area_object._meta.get_field(key)
            except:
                logger.error("Field %s.%s not exists." % (
                        area_object._meta.module_name, key))
                success = False
                continue
            if areaobject_field.rel is not None:
                if areaobject_field.rel.to == TimeSeriesCache:
                    try:
                        timeseriescache = TimeSeriesCache.objects.get(
                            pk=value.split(',')[2])
                        value = timeseriescache
                    except IndexError as ex:
                        logger.error(','.join(map(str, ex.args)))
                        success = False
                        continue
                elif areaobject_field.rel.to == BucketsType:
                    bucket_types = BucketsType.objects.filter(
                        bucket_type=value)
                    if not bucket_types.exists():
                        logger.error("Bucket type %s not exists" % value)
                        success = False
                        continue
                    value = bucket_types[0]
                else:
                    logger.error("Undefined relation to %s." % (
                            areaobject_field.rel.to))
            if isinstance(areaobject_field, BooleanField):
                print "BOOOOOL"
                value = self.str2bool(value)
                print type(value)
            setattr(area_object, key, value)
            area_object.save()
            print "Set"
        return success

    def post(self, request):
        """
        Retrieve data from content, find the area object,
        if area object not available create a new.
        Removes id element from data to avoid overriding id of area object.
        ForeignKey fields need a related object (TimeSeriesCache, BucketType).
        Saves the data.
        """
        object_id = self.CONTENT.get('object_id', None)
        action = request.GET.get('action', None)
        areaobject_type = self.CONTENT.get('area_object_type', None)
        data = json.loads(self.CONTENT.get('data', []))
        if type(data) == dict:
            data = [data]

        areaobject_class = self.areaobject_class(areaobject_type)
        print "+++++++++++++ %s", areaobject_class
        touched_objects = []

        if action == 'delete':
            succes  = self.delete_areaobjects(
                data, areaobject_class)
        elif action == 'create':
            area = AreaConfiguration.objects.get(ident=object_id)
            print area.ident
            success, touched_objects = self.create_areaobjects(
                data, area, areaobject_class)
        elif action == 'update':
            print "BEDIN UP."
            print data
            success, touched_objects = self.update_areaobjects(
                data, areaobject_class)
        else:
            logger.error("UKNOWN post action '%s'." % action)
            success = False

        return {'success': success,
                'data': self.areaobject_configuration(touched_objects)}


class WaterBalanceAreaConfiguration(View):
    """
    Area configuration.
    """
    def get(self, request):
        object_id = request.GET.get('object_id', None)
        grid_name = request.GET.get('grid_name', None)
        areaconfig_objects = AreaConfiguration.objects.filter(ident=object_id)
        if areaconfig_objects.exists():
            return self.area_configuration(areaconfig_objects[0], grid_name)
        else:
            return self.initial_area_configuration(object_id,
                                                   grid_name,
                                                   'admin')

    def area_configuration(self, area, grid_name):
        """
        Retrives area configuration.

        Arguments:
        area -- the area configuration object.
        grid_name -- the name of the table.
        """
        area_config = []
        for field in area._meta.fields:
            grid_field = AreaGridFieldConfiguration.objects.filter(
                field_name__field_name=field.name,
                grid__name__iexact=grid_name)
            if grid_field.exists():
                value = self.retrieve_value(area, field)
                area_config.append(
                    {'id': field.name,
                     'property': grid_field[0].display_name,
                     'value': value,
                     'editable': grid_field[0].editable,
                     'ts_parameter': grid_field[0].ts_parameter,
                     'type': grid_field[0].field_type})
        return area_config

    def retrieve_value(self, area, field):
        """Return a value.

        Arguments:
        area -- the object of AreaConfiguration
        field -- the object type field with respect to area
        """
        value = getattr(area, field.name)
        if value is None:
            return value

        if field.rel is not None:
            if field.rel.to == TimeSeriesCache:
                timeseries = getattr(area, field.name)
                if timeseries is not None:
                    value = '%s,%s,%s' % (
                        timeseries.geolocationcache.ident,
                        timeseries.parametercache.ident,
                        timeseries.id)
            elif field.rel.to == Area:
                if value is not None:
                    value = area.id
            else:
                logger.debug("Unexpected foreign key by %s.%s to %s." % (
                        area._meta.module_name,
                        field.name,
                        field.rel.to._meta.module_name))
        if isinstance(field, DateTimeField):
            if field.name == 'start_dt':
                value = value.strftime(self.startdate_format())
            else:
                value = value.strftime(self.startseason_format())
        return value

    def initial_area_configuration(self, object_id, grid_name,
                                   user_name):
        """
        Creates initial configuration.
        """
        area_object = Area.objects.get(ident=object_id)
        areaconfig_object = AreaConfiguration(
            ident=area_object.ident,
            name=area_object.name,
            area=area_object)
        areaconfig_object.save()
        area_config = self.area_configuration(areaconfig_object, grid_name)
        return area_config

    def post(self, request, pk=None):
        """
        Saves area configuration.
        Uses object_id to find AreaConfiguration.
        Expects data object as list of dict like:
        [{"value":"101.1,ALMR110,1514","id":"ts_kwel"},]
        where loc=101.1, par=ALMR110, id=1514.
        Escapes saving id field.
        """
        object_id = self.CONTENT.get('object_id', None)

        if not object_id:
            return {'success': False}

        data = json.loads(self.CONTENT.get('data', []))

        if type(data) == dict:
            data = [data]

        area_config = AreaConfiguration.objects.get(ident=object_id)

        for field in data:
            field_name = str(field['id'])
            value = str(field['value'])

            if field_name == 'id':
                continue
            try:
                areaconfig_field = area_config._meta.get_field(field_name)
            except:
                logger.debug("Field '%s.%s' is NOT exists." % (
                      area_config._meta.module_name, field_name))
                continue

            if areaconfig_field.rel:
                if areaconfig_field.rel.to == TimeSeriesCache:
                    timeseriescache = TimeSeriesCache.objects.get(
                        id=int(value.split(',')[2]))
                    setattr(area_config, field_name, timeseriescache)
                    continue
                if areaconfig_field.rel.to == Area:
                    continue

            if isinstance(areaconfig_field, DateTimeField):
                value = self.datetimefield_value(areaconfig_field, value)
                if value is None:
                    continue
            setattr(area_config, field_name, value)
        area_config.save()
        return {'success': True}

    def datetimefield_value(self, field, value):
        val = None
        try:
            if field.name == 'start_dt':
                val = datetime.datetime.strptime(
                    value, self.startdate_format())
            else:
                curr_year = datetime.datetime.today().year
                val = datetime.datetime.strftime(
                    "%s/%s" % (curr_year, value),
                    self.startseason_format())
        except ValueError as ex:
            logger.error(ex.message)
        return val

    def startdate_format(self):
        return "%d/%m/%Y"

    def startseason_format(self):
        return "%d/%m"
