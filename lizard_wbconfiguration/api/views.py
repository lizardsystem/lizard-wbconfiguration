"""
API views not coupled to models.
"""
import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils import simplejson as json
from django.db.models.fields import DateTimeField
from django.db.models.fields import BooleanField

from djangorestframework.views import View
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import AreaGridFieldConfiguration
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import StructureInOut
from lizard_wbconfiguration import models

from lizard_area.models import Area

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


class WaterBalanceAreaObjectConfiguration(View):
    """
    View and save the area configuration objects.
    Buckets and Structures.
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

    def create_default_structures(self, object_id):
        """
        Create 10 structures.
        """
        area_configuration = AreaConfiguration.objects.get(
            ident=object_id)
        area_configuration.create_default_structures()

    def last_areaobject_codenumber(self, area_configuration, areaobject_class):
        """ Return code number of the last structure. """
        area_objects = areaobject_class.objects.filter(
            area__id=area_configuration.id,
            code__contains=areaobject_class.CODE_DELIMETER)
        number = None
        if area_objects.exists():
            last_areaobject = area_objects.order_by('-id')[0]
            number = last_areaobject.code_number()
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

    def delete_areaobjects(self, data, areaobject_class):
        """Deactivate area objects exclusive computed structures."""
        success = True
        try:
            for record in data:
                areaobject_id = self.retrieve_id(record)
                area_objects = areaobject_class.objects.filter(
                    id=areaobject_id)
                if not area_objects.exists():
                    continue
                area_object = area_objects[0]
                if type(area_object) == Structure and area_object.is_computed:
                    continue
                area_object.deleted = True
                area_object.save()
        except:
                success = False
        return success

    def create_bucket(self, area):
        """
        Create a bucket.
        """
        bucket = Bucket(area=area, data_set=area.data_set)
        last_codenumber = self.last_areaobject_codenumber(
            area, Bucket)
        if last_codenumber is None:
            last_codenumber = bucket.code_number()

        bucket.code = bucket.create_code(last_codenumber + 1)
        bucket.save()
        return bucket

    def create_buckets(self, data, area):
        """Create area object."""
        touched_objects = []
        success = True
        for record in data:
            if 'id' in record.keys():
                del record['id']
            bucket = self.create_bucket(area)
            if bucket is None:
                success = False
                continue
            if not self.update_areaobject(record, bucket):
                success = False

            touched_objects.append(bucket)
        return (success, touched_objects)

    def update_areaobjects(self, data, areaobject_class):
        touched_objects = []
        success = True
        for record in data:
            areaobject_id = self.retrieve_id(record)
            area_objects = areaobject_class.objects.filter(id=areaobject_id)
            if not area_objects.exists():
                logger.error("%s with id=%s not exists." % (
                        areaobject_class._meta.module_name, areaobject_id))
                success = False
                continue
            area_object = area_objects[0]
            if not self.update_areaobject(record, area_object):
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
                if areaobject_field.rel.to == BucketsType:
                    bucket_types = BucketsType.objects.filter(
                        bucket_type=value)
                    if not bucket_types.exists():
                        logger.error("Bucket type %s not exists" % value)
                        success = False
                        continue
                    value = bucket_types[0]
                elif areaobject_field.rel.to == StructureInOut:
                    structure_inout = StructureInOut.objects.filter(
                        code=value)
                    if not structure_inout.exists():
                        logger.error("Bucket type %s not exists" % value)
                        success = False
                        continue
                    value = structure_inout[0]
                else:
                    logger.error("Undefined relation to %s." % (
                            areaobject_field.rel.to))
            if isinstance(areaobject_field, BooleanField):
                value = self.str2bool(value)
            setattr(area_object, key, value)
            area_object.save()
        return success

    def post(self, request):
        """
        Retrieve data from content, find the area object,
        if area object not available create a new.
        Removes id element from data to avoid overriding id of area object.
        ForeignKey fields need a related object (BucketType).
        Saves the data.

        """

        object_id = self.CONTENT.get('object_id', None)
        action = request.GET.get('action', None)
        areaobject_type = self.CONTENT.get('area_object_type', None)
        data = json.loads(self.CONTENT.get('data', []))
        if type(data) == dict:
            data = [data]

        areaobject_class = self.areaobject_class(areaobject_type)
        touched_objects = []

        if action == 'delete' and areaobject_class == Bucket:
            success = self.delete_areaobjects(
                data, areaobject_class)
        elif action == 'create' and areaobject_class == Bucket:
            area = AreaConfiguration.objects.get(ident=object_id)
            success, touched_objects = self.create_buckets(data, area)
        elif action == 'update':
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
        ident = request.GET.get('object_id', None)
        area_configs = AreaConfiguration.objects.filter(ident=ident)
        if area_configs.exists():
            area_config = area_configs[0]
        else:
            area_config = WaterBalanceAreaConfiguration.create(ident)
        grid_name = request.GET.get('grid_name', None)
        return self.area_configuration(area_config, grid_name)

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
            if field.rel.to == Area:
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

    @classmethod
    def create(self, ident):
        """Create a AreaConfiguration for the Area with the given ident."""
        try:
            area = Area.objects.get(ident=ident)
        except Area.DoesNotExist:
            logger.warning("We cannot create a WaterBalanceAreaConfiguration for the non-existing Area with ident '%s'." % ident)
            return None
        area_config = AreaConfiguration(ident=area.ident,
                                        name=area.name,
                                        area=area,
                                        data_set=area.data_set)
        area_config.save()
        return area_config

    def allowed_data_set_id(self, request):
        """Returns first allowed data_set_id."""
        data_set_ids = request.allowed_data_set_ids
        for data_set_id in data_set_ids:
            return data_set_id
        return None

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
        data_set_id = self.allowed_data_set_id(request)
        if data_set_id is None:
            logger.debug("User %s is not allowed to maintain data sets.",
                         request.user.username)
            return {'success': False}

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
                if areaconfig_field.rel.to == Area:
                    continue

            if isinstance(areaconfig_field, DateTimeField):
                value = self.datetimefield_value(areaconfig_field, value)
                if value is None:
                    continue
            setattr(area_config, field_name, value)

        try:
            area_config.save()
        except Exception as ex:
            logger.error("Could not save wb-configuration for %s" % object_id)
            logger.error(','.join(map(str, ex.args)))
            return {'success': False}

        return {'success': True}

    def datetimefield_value(self, field, value):
        val = None
        try:
            if field.name == 'start_dt':
                val = datetime.datetime.strptime(
                    value, self.date_format())
            else:
                curr_year = datetime.datetime.today().year
                val = datetime.datetime.strptime(
                    "%s/%s" % (value, curr_year),
                    self.date_format())
        except ValueError as ex:
            logger.debug(','.join(map(str, ex.args)))
        except TypeError as ex:
            logger.debug(','.join(map(str, ex.args)))
        except Exception as ex:
            logger.debug(','.join(map(str, ex.args)))

        return val

    def date_format(self):
        return "%d/%m/%Y"

    def startseason_format(self):
        return "%d/%m"


class WBSummary(View):

    """
    WB configuration summary.
    """
    def get(self, request):
        object_id = request.GET.get('object_id', None)
        areaconfigurations = AreaConfiguration.objects.filter(ident=object_id)
        context = {}
        if areaconfigurations.exists():
            buckets = Bucket.objects.filter(area=areaconfigurations[0])
            structures_in = Structure.objects.filter(
                area=areaconfigurations[0],
                in_out__code='in')
            structures_out = Structure.objects.filter(
                area=areaconfigurations[0],
                in_out__code='uit')

            context = {'areaconfiguration': areaconfigurations[0],
                       'buckets': buckets,
                       'structures_in': structures_in,
                       'structures_out': structures_out}

        return render_to_response('wbconfiguration_summary.html', context)
