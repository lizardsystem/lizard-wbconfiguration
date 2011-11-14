from django.contrib import admin

from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import ParameterMapping
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import BucketsType


# class StructureInline(admin.TabularInline):
#     model = Structure


# class AreaStructureAdmin(admin.ModelAdmin):
#     inlines = [
#         StructureInline,
#         ]


admin.site.register(AreaConfiguration)
admin.site.register(ParameterMapping)
admin.site.register(Structure)
admin.site.register(Bucket)
admin.site.register(BucketsType)
