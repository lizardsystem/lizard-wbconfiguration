"""
Model resources for API.
"""
from djangorestframework.resources import ModelResource

from lizard_wbconfiguration.models import AreaConfiguration


class AreaConfigurationResource(ModelResource):
    """
    AreaConfigurationResource
    """
    model = AreaConfiguration
    fields = ()
