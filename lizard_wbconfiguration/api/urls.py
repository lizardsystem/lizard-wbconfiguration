# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
# from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin


from lizard_wbconfiguration.api.views import RootView
from lizard_wbconfiguration.api.views import WaterBalanceAreaConfiguration
from lizard_wbconfiguration.api.views import WaterBalanceBucketConfiguration

admin.autodiscover()

NAME_PREFIX = 'lizard_wbconfiguration_api_'

urlpatterns = patterns(
    '',
    url(r'^$',
        RootView.as_view(),
        name=NAME_PREFIX + 'root'),
    url(r'^area_configuration/(?P<object_id>[0-9a-zA-Z]+)/' \
        '(?P<grid_name>[0-9a-zA-Z]+)/$',
        WaterBalanceAreaConfiguration.as_view(),
        name=NAME_PREFIX + 'area_configuration'),
    url(r'^bucket_configuration/(?P<object_id>[0-9a-zA-Z]+)/$',
        WaterBalanceBucketConfiguration.as_view(),
        name=NAME_PREFIX + 'bucket_configuration')
    )
