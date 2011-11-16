"""
API views not coupled to models.
"""
from django.core.urlresolvers import reverse

from djangorestframework.views import View
from lizard_wbconfiguration.models import AreaConfiguration

from lizard_area.models import Area
#from lizard_fewsnorm.models import


class RootView(View):
    """
    Startpoint.
    """
    def get(self, request):
        return {
            "root": reverse(
                'lizard_wbconfiguration_api_root'),
            }


class WBAreaConfiguration(View):
    """
    Treeview, basically a dump_bulk() from treebeard
    """
    def get(self, request, object_id):
        area_object = Area.objects.get(ident=object_id)
        areaconfig_object = AreaConfiguration()
        area_config = []
        for k,v in area_object.__dict__.iteritems():
            if k == 'ident' or k == 'name':
                area_config.append(
                    {'property': k,
                     'value': v,
                     'editable': False,
                     'type': type(v).__name__})

        for k,v in areaconfig_object.__dict__.iteritems():
            if k == 'start_dt' or k == 'ts_precipitation_id':
                area_config.append(
                    {'property': k,
                     'value': v,
                     'editable': False,
                     'type': type(v).__name__})
        return area_config

    def timeseries(self):
        pass

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
