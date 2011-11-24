"""
API views not coupled to models.
"""
from django.core.urlresolvers import reverse
from django.utils import simplejson as json

from djangorestframework.views import View
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import AreaGridFieldConfiguration
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import BucketsType

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


class WaterBalanceBucketConfiguration(View):
    """
    """

    def get(self, request):
        object_id = request.GET.get('object_id', None)
        buckets = Bucket.objects.filter(
            area__ident=object_id,
            deleted=False)
        if buckets.exists():
            return self.bucket_configuration(list(buckets))
        else:
            bucket = self.create_bucket(object_id)
            return self.bucket_configuration([bucket])

    def bucket_configuration(self, buckets):
        """
        Creates list of dictionaries objects from
        passed buckets object.
        """
        bucket_config = []
        for bucket in buckets:
            bucket_as_dict = {}
            for field in bucket._meta.fields:
                if field.rel:
                    value = str(getattr(bucket, field.name))
                else:
                    value = field.value_from_object(bucket)
                bucket_as_dict[field.name] = value
            bucket_config.append(bucket_as_dict)
        return bucket_config

    def create_bucket(self, object_id):
        """
        Creates a Bucket object related to AreaConfiguration.
        """
        print object_id
        area_config = AreaConfiguration.objects.get(ident=object_id)
        print area_config
        bucket = Bucket(area=area_config)
        bucket.save()
        return bucket

    def retrieve_bucket_id(self, record):
        if type(record) == dict:
            id = record.get('id', None)
            try:
                return int(id)
            except ValueError:
                logger.debug("Bucket ID '%s' is NOT a integer", id)
                return -1

    def post(self, request):
        """
        Retrieve data from content, find the bucket,
        if bucket not available create a new.
        Remove id element from data to avoid overriding Bucket.id.
        ForeignKey fields need a related object (TimeSeriesCache, BucketType).
        Save the data.
        @TODO replace value.split(',')[2] with timeseriescache.id
        """
        object_id = self.CONTENT.get('object_id', None)
        data = json.loads(self.CONTENT.get('data', []))
        if type(data) == dict:
            data = [data]

        for record in data:
            buckets = Bucket.objects.filter(id=self.retrieve_bucket_id(record))
            if buckets.exists():
                bucket = buckets[0]
            else:
                bucket = self.create_bucket(object_id)
            del record['id']
            for (key, value) in record.items():
                key = str(key)
                value = str(value)
                if value == "" or value == "None":
                    continue
                try:
                    bucket_field = bucket._meta.get_field(key)
                except:
                    continue
                if bucket_field.rel is not None:
                    if bucket_field.rel.to == TimeSeriesCache:
                        try:
                            timeseriescache = TimeSeriesCache.objects.get(
                                pk=value.split(',')[2])
                            value = timeseriescache
                        except IndexError:
                            return {'success': False}
                    elif bucket_field.rel.to == BucketsType:
                        bucket_types = BucketsType.objects.filter(
                            bucket_type=value)
                        if not bucket_types.exists():
                            return {'success': False}
                        bucket_type = bucket_types[0]
                        value = bucket_type
                    else:
                        return {'success': False}
                setattr(bucket, key, value)
            bucket.save()
        return {'success': True}


class WaterBalanceStructureConfiguration(View):
    """
    Structure configuration.
    """
    def get(self, request):
        object_id = request.GET.get('object_id', None)
        buckets = Bucket.objects.filter(
            area__ident=object_id,
            deleted=False)
        if buckets.exists():
            return self.bucket_configuration(list(buckets))
        else:
            bucket = self.create_bucket(object_id)
            return self.bucket_configuration([bucket])

    def structure_configuration(self, structures):
        """
        Creates list of dictionaries objects from
        passed structure object.
        """
        structure_config = []
        for structure in structures:
            structure_config.append(structure.__dict__)
        return structure_config

    def create_structure(self, object_id):
        area_configuration = AreaConfiguration.objects.get(ident=object_id)
        structures = None
        # structure = Structure(area_co=area_config)
        # structure.save()
        return structures

    def post(self, request):
        object_id = request.GET.get('object_id', None)
        data = json.loads(self.CONTENT.get('data', []))
        if type(data) == dict:
            data = [data]
        for record in data:
            structures = Structure.objects.filter(id=record.get('id', -1))
            if structures.exists():
                structere = structures[0]
            else:
                structere = self.create_structere(object_id)
            del record['id']
            for (key, value) in record.items():
                setattr(structere, key, value)
            structere.save()

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
