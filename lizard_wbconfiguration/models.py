# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
import logging
from django.db import models

from lizard_area.models import Area

from lizard_security.manager import FilteredManager
from lizard_security.models import DataSet


logger = logging.getLogger(__name__)


WB_DBF_MODELS = (
    ('AreaConfiguration', 'AreaConfiguration'),
    ('Bucket', 'Bucket'),
    ('Structure', 'Structure'),
    ('Area', 'Area'),
)

DBF_FIELD_TYPES = (
    ('C', 'Text'),
    ('N', 'Number'),
    ('D', 'Date'),
    ('L', 'Logical'),
)

EXTJS_DATA_TYPES = (
    ('boolean', 'boolean'),
    ('date', 'date'),
    ('float', 'float'),
    ('text', 'text'),
    ('timeserie', 'timeserie'),
)

STRUCTURE_IN_OUT = (
    ('in', 'In'),
    ('uit', 'Uit')
)


class WBConfigurationDBFMapping(models.Model):
    model_name = models.CharField(max_length=128, choices=WB_DBF_MODELS)
    wbfield_name = models.CharField(max_length=128)
    dbffield_name = models.CharField(max_length=128)
    dbffield_type = models.CharField(max_length=1, choices=DBF_FIELD_TYPES)
    dbffield_length = models.IntegerField(null=True, blank=True)
    dbffield_decimals = models.IntegerField(null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s wb=%s dbf=%s" % (self.model_name,
                                    self.wbfield_name,
                                    self.dbffield_name)

    class Meta:
        ordering = ['id']


class DBFConfiguration(models.Model):
    """Configuration for creating dbf's."""
    dbf_type = models.CharField(max_length=128, choices=WB_DBF_MODELS)
    data_set = models.ForeignKey(DataSet, null=True, blank=True)
    save_to = models.CharField(max_length=128, null=True, blank=True,
                               help_text="Example: '/home/naam/dbf/'.")
    filename = models.CharField(max_length=128,
                                help_text="Example: 'Buckets'.")
    enabled = models.BooleanField()

    def __unicode__(self):
        return "%s %s" % (self.dbf_type, self.data_set)


class AreaGridConfiguration(models.Model):
    """
    Grid of front end.
    """
    name = models.CharField(max_length=128)
    app_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.name


class AreaField(models.Model):
    """
    Field names of Area, Communique and AreaConfiguration model.
    Code field = api_name + "." + model_name + "." + field_name
    """
    code = models.CharField(primary_key=True, max_length=256)
    field_name = models.CharField(max_length=100)
    app_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.code


class AreaGridFieldConfiguration(models.Model):
    """
    Configuration grid fields.
    """
    field_name = models.ForeignKey(AreaField, max_length=128)
    display_name = models.CharField(max_length=128)
    editable = models.BooleanField()
    visible = models.BooleanField()
    ts_parameter = models.CharField(max_length=128,
                                    blank=True, null=True)
    field_type = models.CharField(max_length=128, choices=EXTJS_DATA_TYPES)
    grid = models.ForeignKey(AreaGridConfiguration)
    sequence = models.IntegerField()

    class Admin:
        list_filter = ('field_name')

    def __unicode__(self):
        return "%s %s" % (self.grid, self.field_name)


class AreaConfiguration(models.Model):
    """
    Areaconfiguration for water balance.
    Contains 2 deafault structures (in/out).
    """

    ident = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=128)
    area = models.OneToOneField(Area)
    y = models.DecimalField(max_digits=10, decimal_places=9,
                            null=True, blank=True)
    x = models.DecimalField(max_digits=10, decimal_places=9,
                            null=True, blank=True)
    start_dt = models.DateTimeField(null=True, blank=True,
                                    verbose_name="Start date")
    ts_precipitation = models.CharField(max_length=128, null=True, blank=True)
    ts_evaporation = models.CharField(max_length=128, null=True, blank=True)
    max_intake = models.DecimalField(max_digits=10, decimal_places=2,
                                     null=True, blank=True)
    max_outtake = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=True, blank=True)
    ts_concentr_chloride_1 = models.CharField(
        max_length=128, null=True, blank=True)
    ts_concentr_chloride_2 = models.CharField(
        max_length=128, null=True, blank=True)
    surface = models.DecimalField(max_digits=10, decimal_places=0,
                                  null=True, blank=True)
    bottom_height = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=True, blank=True)
    ts_water_level = models.CharField(max_length=128, null=True, blank=True)
    kwel_is_ts = models.BooleanField()
    kwel = models.DecimalField(max_digits=10, decimal_places=2,
                               null=True, blank=True)
    ts_kwel = models.CharField(max_length=128, null=True, blank=True)
    wegz_is_ts = models.BooleanField()
    wegz = models.DecimalField(max_digits=10, decimal_places=2,
                               null=True, blank=True)
    ts_wegz = models.CharField(max_length=128, null=True, blank=True)
    peilh_issp = models.BooleanField()
    sp_is_ts = models.BooleanField()
    ts_sp = models.CharField(max_length=128, null=True, blank=True)
    winterp = models.DecimalField(max_digits=6, decimal_places=2,
                                  null=True, blank=True)
    lentep = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    zomerp = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    herfstp = models.DecimalField(max_digits=6, decimal_places=2,
                                  null=True, blank=True)
    start_wp = models.DateTimeField(null=True, blank=True)
    start_lp = models.DateTimeField(null=True, blank=True)
    start_zp = models.DateTimeField(null=True, blank=True)
    start_hp = models.DateTimeField(null=True, blank=True)
    marge_ond = models.DecimalField(max_digits=10, decimal_places=2,
                                    null=True, blank=True)
    marge_bov = models.DecimalField(max_digits=10, decimal_places=2,
                                    null=True, blank=True)
    nutc_min_1 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    nutc_inc_1 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    nutc_min_2 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    nutc_inc_2 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    nutc_min_3 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    nutc_inc_3 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    nutc_min_4 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    nutc_inc_4 = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    ini_con_cl = models.DecimalField(max_digits=8, decimal_places=2,
                                     null=True, blank=True)
    ts_cl = models.CharField(max_length=128, null=True, blank=True)
    init_water_level = models.DecimalField(max_digits=8, decimal_places=2,
                                           null=True, blank=True)
    concentr_chloride_precipitation = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    concentr_chloride_seepage = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    min_concentr_phosphate_precipitation = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    min_concentr_phopshate_seepage = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    incr_concentr_phosphate_precipitation = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    incr_concentr_phosphate_seepage = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    min_concentr_nitrogyn_precipitation = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    min_concentr_nitrogyn_seepage = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    incr_concentr_nitrogyn_precipitation = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    incr_concentr_nitrogyn_seepage = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    min_concentr_so4_precipitation = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    min_concentr_so4_seepage = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    incr_concentr_so4_precipitation = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    incr_concentr_so4_seepage = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True)
    fews_meta_info = models.CharField(max_length=128, null=True, blank=True)
    supports_object_permissions = True
    data_set = models.ForeignKey(DataSet,
                                 null=True,
                                 blank=True)
    objects = FilteredManager()

    def __unicode__(self):
        return "%s" % self.ident


class StructureInOut(models.Model):
    code = models.CharField(max_length=3, choices=STRUCTURE_IN_OUT)
    index = models.IntegerField(max_length=1)
    description = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.code


class Structure(models.Model):
    """
    Structure.
    """
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    area = models.ForeignKey(AreaConfiguration)
    y = models.DecimalField(max_digits=10, decimal_places=9,
                            null=True, blank=True)
    x = models.DecimalField(max_digits=10, decimal_places=9,
                            null=True, blank=True)
    is_computed = models.BooleanField(default=False)
    ingebr = models.BooleanField(default=True)
    in_out = models.ForeignKey(StructureInOut,
                               null=True, blank=True)
    deb_is_ts = models.BooleanField()
    ts_debiet = models.CharField(max_length=128, null=True, blank=True)
    deb_zomer = models.DecimalField(max_digits=10, decimal_places=2,
                                    null=True, blank=True)
    deb_wint = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    concentr_chloride = models.DecimalField(max_digits=10, decimal_places=2,
                                            null=True, blank=True)
    min_concentr_phosphate = models.DecimalField(max_digits=10,
                                                 decimal_places=2,
                                                 null=True, blank=True)
    incr_concentr_phosphate = models.DecimalField(max_digits=10,
                                                  decimal_places=2,
                                                  null=True, blank=True)
    min_concentr_nitrogen = models.DecimalField(max_digits=10,
                                                decimal_places=2,
                                                null=True, blank=True)
    incr_concentr_nitrogen = models.DecimalField(max_digits=10,
                                                 decimal_places=2,
                                                 null=True, blank=True)
    min_concentr_so4 = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    incr_concentr_so4 = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    deleted = models.BooleanField(default=False)
    fews_meta_info = models.CharField(max_length=128, null=True, blank=True)
    supports_object_permissions = True
    data_set = models.ForeignKey(DataSet,
                                 null=True,
                                 blank=True)
    objects = FilteredManager()

    def code_number(self):
        """Retrieve number of last structure from code."""
        number = 0
        delimeter = '_PS'
        if (self.code is not None) and (self.code.find(delimeter) > 0):
            code_array = self.code.split(delimeter)
            number = int(code_array[len(code_array) - 1])
        return number

    def create_code(self, number):
        """Create structure code.

        The format is '2100_PS1' where:
        2100 - ident of area configuration
        PS - pumping stations
        01 - structure number
        """

        return "%s_PS%d" % (self.area.ident, number)

    def __unicode__(self):
        return "%s %s" % (self.code, self.name)

    class Meta:
        ordering = ['id']


class BucketsType(models.Model):
    code = models.IntegerField(unique=True, null=True, blank=True)
    bucket_type = models.CharField(max_length=128)
    description = models.CharField(max_length=256,
                                   null=True,
                                   blank=True)

    def __unicode__(self):
        return self.bucket_type


class Bucket(models.Model):
    """
    Bucket.
    """
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    bucket_type = models.ForeignKey(BucketsType, null=True, blank=True)
    area = models.ForeignKey(AreaConfiguration)
    y = models.DecimalField(max_digits=10, decimal_places=9,
                            null=True, blank=True)
    x = models.DecimalField(max_digits=10, decimal_places=9,
                            null=True, blank=True)
    replace_impact_by_nutricalc = models.BooleanField()
    is_computed = models.BooleanField()
    ingebr = models.BooleanField(default=True)
    flowoff_is_ts = models.BooleanField()
    flowoff = models.DecimalField(max_digits=10, decimal_places=2,
                                  null=True, blank=True)
    ts_flowoff = models.CharField(max_length=128, null=True, blank=True)
    drainageindraft_is_ts = models.BooleanField()
    drainageindraft = models.DecimalField(max_digits=10, decimal_places=2,
                                          null=True, blank=True)
    ts_drainageindraft = models.CharField(
        max_length=128, null=True, blank=True)
    referenceoverflow_is_ts = models.BooleanField()
    referenceoverflow = models.DecimalField(max_digits=10, decimal_places=2,
                                            null=True, blank=True)
    ts_referenceoverflow = models.CharField(
        max_length=128, null=True, blank=True)
    surface = models.DecimalField(max_digits=10, decimal_places=0,
                                  null=True, blank=True)
    kwelwegz_is_ts = models.BooleanField()
    kwelwegz = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    ts_kwelwegz = models.CharField(max_length=128, null=True, blank=True)
    porosity = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    crop_evaporation_factor = models.DecimalField(max_digits=10,
                                                  decimal_places=2,
                                                  null=True, blank=True)
    min_crop_evaporation_factor = models.DecimalField(max_digits=10,
                                                      decimal_places=2,
                                                      null=True, blank=True)
    drainage_fraction = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    indraft_fraction = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    man_water_level = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    min_water_level = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    equi_water_level = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    bottom_porosity = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    bottom_crop_evaporation_factor = models.DecimalField(max_digits=10,
                                                         decimal_places=2,
                                                         null=True, blank=True)
    bottom_min_crop_evaporation_factor = models.DecimalField(max_digits=10,
                                                         decimal_places=2,
                                                         null=True, blank=True)
    bottom_drainage_fraction = models.DecimalField(max_digits=10,
                                                   decimal_places=2,
                                                   null=True, blank=True)
    bottom_indraft_fraction = models.DecimalField(max_digits=10,
                                                  decimal_places=2,
                                                  null=True, blank=True)
    bottom_max_water_level = models.DecimalField(max_digits=10,
                                                 decimal_places=2,
                                                 null=True, blank=True)
    bottom_min_water_level = models.DecimalField(max_digits=10,
                                                 decimal_places=2,
                                                 null=True, blank=True)
    bottom_equi_water_level = models.DecimalField(max_digits=10,
                                                 decimal_places=2,
                                                 null=True, blank=True)
    init_water_level = models.DecimalField(max_digits=10, decimal_places=2,
                                           null=True, blank=True)
    bottom_init_water_level = models.DecimalField(max_digits=10,
                                                  decimal_places=2,
                                                  null=True, blank=True)
    concentr_chloride_flow_off = models.DecimalField(max_digits=10,
                                                     decimal_places=2,
                                                     null=True, blank=True)
    concentr_chloride_drainage_indraft = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    min_concentr_phosphate_flow_off = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    min_concentr_phosphate_drainage_indraft = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    incr_concentr_phosphate_flow_off = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    incr_concentr_phosphate_drainage_indraft = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    min_concentr_nitrogen_flow_off = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    min_concentr_nitrogen_drainage_indraft = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True)
    incr_concentr_nitrogen_flow_off = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    incr_concentr_nitrogen_drainage_indraft = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True)
    min_concentr_so4_flow_off = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    min_concentr_so4_drainage_indraft = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    incr_concentr_so4_flow_off = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    incr_concentr_so4_drainage_indraft = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True)
    label_flow_off = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         null=True, blank=True)
    label_drainaige_indraft = models.DecimalField(max_digits=10,
                                                  decimal_places=2,
                                                  null=True, blank=True)
    deleted = models.BooleanField(default=False)
    fews_meta_info = models.CharField(max_length=128, null=True, blank=True)
    supports_object_permissions = True
    data_set = models.ForeignKey(DataSet,
                                 null=True,
                                 blank=True)
    objects = FilteredManager()

    def code_number(self):
        """Retrieve number of last bucket from code per area."""
        number = 0
        delimeter = '_gw'
        if (self.code is not None) and (self.code.find(delimeter) > 0):
            code_array = self.code.split(delimeter)
            number = int(code_array[len(code_array) - 1])
        return number

    def create_code(self, number):
        """Create bucket code.

        The format is '2100_gw1' where:
        2100 - ident of area configuration
        gw - grond water
        1 - bucket number
        """

        return "%s_gw%d" % (self.area.ident, number)

    class Meta:
        ordering = ['id']
