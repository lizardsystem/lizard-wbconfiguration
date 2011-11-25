"""
API views not coupled to models.
"""
from django.core.urlresolvers import reverse
from django.utils import simplejson as json

from djangorestframework.views import View
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import AreaGridFieldConfiguration
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration import models

from lizard_area.models import Area

from lizard_fewsnorm.models import TimeSeriesCache

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
        Creates a dbf file.
        """
        return {'success': True}


class WaterBalanceAreaObjectConfiguration(View):
    """
    """

    def get(self, request):
        object_id = request.GET.get('object_id', None)
        area_object_type = request.GET.get('area_object_type', None)
        area_object_class = self.area_object_class(object_id, area_object_type)

        if area_object_class is None:
            return []

        area_objects = area_object_class.objects.filter(
            area__ident=object_id,
            deleted=False)
        if area_objects.exists():
            return self.area_object_configuration(list(area_objects))
        else:
            area_object = self.create_area_object(object_id, area_object_class)
            return self.area_object_configuration([area_object])

    def area_object_class(self, object_id, area_object_type):
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

    def area_object_configuration(self, area_objects):
        """
        Creates list of dictionaries objects from
        passed area_objects object.
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

    def create_area_object(self, object_id, area_object_class):
        """
        Creates a area object object related to AreaConfiguration.
        """
        area_config = AreaConfiguration.objects.get(ident=object_id)
        area_object = area_object_class(area=area_config)
        area_object.save()
        return area_object

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
                logger.debug("Bucket ID '%s' is NOT an integer", id)
                return -1

    def post(self, request):
        """
        Retrieve data from content, find the area object,
        if area object not available create a new.
        Remove id element from data to avoid overriding id of area object.
        ForeignKey fields need a related object (TimeSeriesCache, BucketType).
        Save the data.
        @TODO replace value.split(',')[2] with timeseriescache.id
        """
        object_id = self.CONTENT.get('object_id', None)
        area_object_type = self.CONTENT.get('area_object_type', None)
        data = json.loads(self.CONTENT.get('data', []))
        if type(data) == dict:
            data = [data]
        area_object_class = self.area_object_class(object_id, area_object_type)
        for record in data:
            area_objects = area_object_class.objects.filter(
                id=self.retrieve_id(record))
            if area_objects.exists():
                area_object = area_objects[0]
            else:
                area_object = self.create_area_object(
                    object_id, area_object_class)
            del record['id']
            for (key, value) in record.items():
                key = str(key)
                value = str(value)
                if value == "" or value == "None":
                    continue
                try:
                    area_object_field = area_object._meta.get_field(key)
                except:
                    continue
                if area_object_field.rel is not None:
                    if area_object_field.rel.to == TimeSeriesCache:
                        try:
                            timeseriescache = TimeSeriesCache.objects.get(
                                pk=value.split(',')[2])
                            value = timeseriescache
                        except IndexError:
                            return {'success': False}
                    elif area_object_field.rel.to == BucketsType:
                        bucket_types = BucketsType.objects.filter(
                            bucket_type=value)
                        if not bucket_types.exists():
                            return {'success': False}
                        bucket_type = bucket_types[0]
                        value = bucket_type
                    else:
                        return {'success': False}
                setattr(area_object, key, value)
            area_object.save()
        return {'success': True}


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
        Retrive area configuration.
        Expected singel area configuration object.
        """
        area_config = []
        for field in area._meta.fields:
            grid_field = AreaGridFieldConfiguration.objects.filter(
                field_name__field_name=field.name,
                grid__name__iexact=grid_name)
            if grid_field.exists():
                area_config.append(
                    {'id': field.name,
                     'property': grid_field[0].display_name,
                     'value': str(getattr(area, field.name)),
                     'editable': grid_field[0].editable,
                     'type': grid_field[0].field_type})
        return area_config

    def initial_area_configuration(self, object_id, grid_name, user_name):
        """
        Create initial configuration.
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
        Save area configuration.
        Use object_id to find AreaConfiguration.
        Expected data object as list of dict like:
        [{"value":"101.1,ALMR110,1514","id":"ts_kwel"},]
        where loc=101.1, par=ALMR110, id=1514.
        Escape saving id field.
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
                continue

            if areaconfig_field.rel:
                if areaconfig_field.rel.to == TimeSeriesCache:
                    timeseriescache = TimeSeriesCache.objects.get(
                        id=int(value.split(',')[2]))
                    setattr(area_config, field_name, timeseriescache)
                    continue
                if areaconfig_field.rel.to == Area:
                    continue
            setattr(area_config, field_name, value)

        area_config.save()

        return {'success': True}
