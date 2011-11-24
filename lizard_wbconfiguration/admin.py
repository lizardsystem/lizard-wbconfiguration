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

    def fomrfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "field_name":
            kwargs["queryset"] = AreaField.objects.filter(
                model_name="bucket")
        return super(AreaGridFieldConfigurationInline, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    # def formfield_for_dbfield(self, field, **kwargs):
    #     #print "+++++++++++++++++++++++"
    #     if field.name == 'grid':
    #         print "---------------------------------"
    #         #print field._get_val_from_obj()
    #         #print field.name
    #         #print field.value_to_string(()
    #         # print self.get_object(kwargs['request'], AreaGridConfiguration)
    #         # Note - get_object hasn't been defined yet
    #         # parent_trip = self.get_object(kwargs['request'], Trip)
    #         # contained_areagrid = AreaGridConfiguration.objects.filter(
    #         #     area__contains=parent_trip.area.area)
    #         # return forms.ModelChoiceField(queryset=contained_areas )
    #     return super(AreaGridFieldConfigurationInline, self).formfield_for_dbfield(field, **kwargs)



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
admin.site.register(BucketsType)
admin.site.register(AreaField)
admin.site.register(AreaGridConfiguration, AreaGridConfigurationAdmin)
