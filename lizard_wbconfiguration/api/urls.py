# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
# from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from djangorestframework.views import InstanceModelView

from lizard_wbconfiguration.api.resources import AreaConfigurationResource

from lizard_wbconfiguration.api.views import RootView
from lizard_wbconfiguration.api.views import WBAreaConfiguration


admin.autodiscover()

NAME_PREFIX = 'lizard_wbconfiguration_api_'

urlpatterns = patterns(
    '',
    url(r'^$',
        RootView.as_view(),
        name=NAME_PREFIX + 'root'),
    url(r'^area_configuration/(?P<object_id>[0-9a-zA-Z]+)/$',
        WBAreaConfiguration.as_view(),
        name=NAME_PREFIX + 'area_configuration'),
    # url(r'^area_configuration/(?P<slug>[^/]+)/$',
    #     InstanceModelView.as_view(resource=AreaConfigurationResource),
    #     name=NAME_PREFIX + 'area_configuration'),
    )
