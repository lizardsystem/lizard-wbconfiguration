"""
API views not coupled to models.
"""
from django.core.urlresolvers import reverse

from djangorestframework.views import View
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import AreaGridFieldConfiguration
from lizard_wbconfiguration.models import Bucket
from lizard_area.models import Area

from lizard_fewsnorm.models import GeoLocationCache
from lizard_fewsnorm.models import TimeSeriesCache
from lizard_fewsnorm.models import TimeStepCache
from lizard_fewsnorm.models import ModuleCache
from lizard_fewsnorm.models import ParameterCache


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
    def get(self, request, object_id):
        buckets = Buckets.objects.filter(area__ident=object_id)
        if buckets.exists():
            return self.bucket_configuration(list(buckets))
        else:
            return self.bucket_configuration([Bucket()])

    def bucket_configuration(self, buckets):
        """
        Creates list of dictionaries objects from
        passed buckets object.
        """
        bucket_config = []
        for bucket in buckets:
            bucket_config.append(bucket.__dict__)
        return bucket_config


class WaterBalanceStructureConfiguration(View):
    """
    Structure configuration.
    """
    def get(self, request, object_id):
        structure_object = None
        return []


class WaterBalanceAreaConfiguration(View):
    """
    Area configuration.
    """
    def get(self, request, object_id, grid_name):
        areaconfig_objects = AreaConfiguration.objects.filter(ident=object_id)
        if areaconfig_objects.exists():
            return self.area_configuration(areaconfig_objects[0], grid_name)
        else:
            return self.initial_area_configuration(object_id, grid_name)

    def area_configuration(self, area, grid_name):
        """
        Retrives area configuration.
        Expected singel area configuration object.
        """
        area_config = []
        for k, v in area.__dict__.iteritems():
            grid_field = AreaGridFieldConfiguration.objects.filter(
                field_name__field_name=k,
                grid__name__iexact=grid_name)
            if grid_field.exists():
                area_config.append(
                    {'property': grid_field[0].display_name,
                     'value': v,
                     'editable': grid_field[0].editable,
                     'type': grid_field[0].field_type})
        return area_config

    def initial_area_configuration(self, object_id, grid_name):
        """
        Cteates initial configuration.
        """
        area_object = Area.objects.get(ident=object_id)
        areaconfig_object = AreaConfiguration(
            ident=area_object.ident,
            name=area_object.name)
        area_config = self.area_configuration(areaconfig_object, grid_name)
        return area_config


    # def post(self, request, pk=None):

    #     data = json.loads(self.CONTENT.get('data', []))
    #     if type(data) == dict:
    #         data = [data]
    #     for record in data:
    #         area_config = AreaConfiguration.objects.get(id=int(record['id']))
    #         del record['id']
    #         for (key, value) in record.items():
    #             setattr(area_config, key, value)
    #         area_config.save()

    #     return {'success': True}
