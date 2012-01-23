from django.contrib import admin

from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration.models import AreaGridConfiguration
from lizard_wbconfiguration.models import AreaField
from lizard_wbconfiguration.models import AreaGridFieldConfiguration
from lizard_wbconfiguration.models import WBConfigurationDBFMapping
from lizard_wbconfiguration.models import DBFConfiguration
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import StructureInOut

from lizard_security.admin import SecurityFilteredAdmin


class AreaGridFieldConfigurationInline(admin.TabularInline):
    model = AreaGridFieldConfiguration

    def fomrfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "field_name":
            kwargs["queryset"] = AreaField.objects.filter(
                model_name="bucket")
        return super(AreaGridFieldConfigurationInline,
                     self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class AreaGridConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name']

    inlines = [
        AreaGridFieldConfigurationInline,
        ]


class WBConfigurationDBFMappingAdmin(admin.ModelAdmin):
    list_display = (
        'model_name',
        'wbfield_name',
        'dbffield_name',
        'dbffield_type',
        'dbffield_length',
        'dbffield_decimals',
        'index')
    list_editable = (
        'wbfield_name',
        'dbffield_name',
        'dbffield_type',
        'dbffield_length',
        'dbffield_decimals',
        'index')
    list_filter = ('model_name',)


admin.site.register(DBFConfiguration)
admin.site.register(WBConfigurationDBFMapping, WBConfigurationDBFMappingAdmin)
admin.site.register(BucketsType)
admin.site.register(AreaField)
admin.site.register(AreaGridConfiguration, AreaGridConfigurationAdmin)
admin.site.register(Structure, SecurityFilteredAdmin)
admin.site.register(StructureInOut)
