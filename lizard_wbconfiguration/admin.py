from django.contrib import admin

from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import ParameterMapping
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration.models import AreaGridConfiguration
from lizard_wbconfiguration.models import AreaGridFieldsConfiguration


class GriedFieldsInline(admin.TabularInline):
    model = AreaGridFieldsConfiguration


class GridAdmin(admin.ModelAdmin):
    inlines = [
        GriedFieldsInline,
        ]


admin.site.register(AreaConfiguration)
admin.site.register(ParameterMapping)
admin.site.register(Structure)
admin.site.register(Bucket)
admin.site.register(BucketsType)
admin.site.register(AreaGridConfiguration, GridAdmin)
