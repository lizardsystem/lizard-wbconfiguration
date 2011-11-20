from django.contrib import admin
from django.contrib.admin import ModelAdmin

from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import ParameterMapping
from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import Bucket
from lizard_wbconfiguration.models import BucketsType
from lizard_wbconfiguration.models import AreaGridConfiguration
from lizard_wbconfiguration.models import AreaField
from lizard_wbconfiguration.models import AreaGridFieldConfiguration


def make_published(modeladmin, request, queryset):
    print "===================================="
    print queryset
    queryset.update(name='w')


class AreaGridFieldConfigurationInline(admin.TabularInline):
    model = AreaGridFieldConfiguration
    #raw_id_fields = ("field_name",)
    #actions = [make_published]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print "_______________________________________"
        print kwargs
        print db_field.name

        #if db_field.name == "car":
        #    kwargs["queryset"] = Car.objects.filter(owner=request.user)
        return super(AreaGridFieldConfigurationInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class AreaGridConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name']
    #actions = [make_published]

    inlines = [
        AreaGridFieldConfigurationInline,
        ]


# admin.site.register(AreaConfiguration)
# admin.site.register(ParameterMapping)
# admin.site.register(Structure)
# admin.site.register(Bucket)
# admin.site.register(BucketsType)
admin.site.register(AreaField)
admin.site.register(AreaGridConfiguration, AreaGridConfigurationAdmin)
