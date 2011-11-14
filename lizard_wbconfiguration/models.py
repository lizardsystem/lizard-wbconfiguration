# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
import logging
from django.db import models

from lizard_area.models import Area
from lizard_fewsnorm.models import TimeSeriesCache
from lizard_fewsnorm.models import ParameterCache

logger = logging.getLogger(__name__)


class ParameterMapping(models.Model):
    """
    Map wbconfigurations parameters with cached parameters
    """
    parametercache = models.ForeignKey(ParameterCache)
    ident_wbconfiguration = models.CharField(unique=True,
                                             max_length=128)

    def __unicode__(self):
        return "%s %s" % (
            self.parametercache.ident,
            self.ident_wbconfiguration)


def parameter(ident):
    try:
        parameter = ParameterMapping.objects.get(
            ident_wbconfiguration=ident).parametercache
    except:
        logger.warning("Parameter ident '%s' is NOT properly mapped." % ident)
        parameter = None
    return parameter


class AreaConfiguration(Area):
    """
    Areaconfiguration for water balace.
    """

    start_dt = models.DateTimeField(null=True, blank=True)
    ts_precipitation = models.ForeignKey(TimeSeriesCache,
                                         null=True, blank=True,
                                         related_name='ts_precipitation',
                                         limit_choices_to={
            'parametercache': parameter('precipitation')},)
    ts_evaporation = models.ForeignKey(TimeSeriesCache,
                                       null=True, blank=True,
                                       related_name='ts_evaporation',
                                       limit_choices_to={
            'parametercache': parameter('evaporation')})
    max_intake = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    max_outtake = models.DecimalField(max_digits=5, decimal_places=3,
                                      null=True, blank=True)
    ts_concentr_chloride_1 = models.ForeignKey(
        TimeSeriesCache,
        null=True, blank=True,
        related_name='ts_concentr_chloride_1',
        limit_choices_to={'parametercache': parameter('concentr_chloride_1')})
    ts_concentr_chloride_2 = models.ForeignKey(
        TimeSeriesCache,
        null=True, blank=True,
        related_name='ts_concentr_chloride_2',
        limit_choices_to={
            'parametercache': parameter('concentr_chloride_2')})
    surface = models.DecimalField(max_digits=10, decimal_places=1,
                                  null=True, blank=True)
    bottom_height = models.DecimalField(max_digits=5, decimal_places=3,
                                        null=True, blank=True)
    ts_water_level = models.ForeignKey(TimeSeriesCache,
                                       null=True, blank=True,
                                       related_name='ts_water_level',
                                       limit_choices_to={
            'parametercache': parameter('water_level')})
    kwel_is_ts = models.BooleanField()
    kwel = models.DecimalField(max_digits=5, decimal_places=3,
                               null=True, blank=True)
    ts_kwel = models.ForeignKey(TimeSeriesCache,
                                null=True, blank=True,
                                related_name='ts_kwel',
                                limit_choices_to={
            'parametercache': parameter('kwel')})
    wegz_is_ts = models.BooleanField()
    wegz = models.DecimalField(max_digits=5, decimal_places=3,
                               null=True, blank=True)
    ts_wegz = models.ForeignKey(TimeSeriesCache,
                                null=True, blank=True,
                                related_name='ts_wegz',
                                limit_choices_to={
            'parametercache': parameter('wegz')})
    peilh_issp = models.BooleanField()
    sp_is_ts = models.BooleanField()
    ts_sp = models.ForeignKey(TimeSeriesCache,
                              null=True, blank=True,
                              related_name='sp',
                              limit_choices_to={
            'parametercache': parameter('sp')})
    winterp = models.DecimalField(max_digits=5, decimal_places=3,
                                  null=True, blank=True)
    lentep = models.DecimalField(max_digits=5, decimal_places=3,
                                 null=True, blank=True)
    zomerp = models.DecimalField(max_digits=5, decimal_places=3,
                                 null=True, blank=True)
    herfstp = models.DecimalField(max_digits=5, decimal_places=3,
                                  null=True, blank=True)
    start_wp = models.DateTimeField(null=True, blank=True)
    start_lp = models.DateTimeField(null=True, blank=True)
    start_zp = models.DateTimeField(null=True, blank=True)
    start_hp = models.DateTimeField(null=True, blank=True)
    marge_ond = models.DecimalField(max_digits=5, decimal_places=3,
                                    null=True, blank=True)
    marge_bov = models.DecimalField(max_digits=5, decimal_places=3,
                                    null=True, blank=True)
    nutc_min_1 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    nutc_inc_1 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    nutc_min_2 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    nutc_inc_2 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    nutc_min_3 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    nutc_inc_3 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    nutc_min_4 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    nutc_inc_4 = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    ini_con_cl = models.DecimalField(max_digits=5, decimal_places=3,
                                     null=True, blank=True)
    init_water_level = models.DecimalField(max_digits=5, decimal_places=3,
                                           null=True, blank=True)
    concentr_chloride_precipitation = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    concentr_chloride_seepage = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_phosphate_precipitation = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_phopshate_seepage = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    incr_concentr_phosphate_precipitation = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    incr_concentr_phosphate_seepage = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_nitrogyn_precipitation = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_nitrogyn_seepage = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    incr_concentr_nitrogyn_precipitation = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    incr_concentr_nitrogyn_seepage = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)


class Structure(models.Model):
    """
    Structure.
    """
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    is_computed = models.BooleanField()
    from_area = models.ForeignKey(
        AreaConfiguration,
        related_name='wbconfiguration_structure_set1',
        null=True, blank=True)
    to_area = models.ForeignKey(
        AreaConfiguration,
        related_name='wbconfiguration_structure_set2',
        null=True, blank=True)
    deb_is_ts = models.BooleanField()
    ts_debiet = models.ForeignKey(
        TimeSeriesCache,
        related_name='ts_debiet',
        null=True, blank=True,
        limit_choices_to={
            'parametercache': parameter('debiet')})
    deb_zomer = models.DecimalField(max_digits=5, decimal_places=3,
                                    null=True, blank=True)
    deb_wint = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    concentr_chloride = models.DecimalField(max_digits=5, decimal_places=3,
                                            null=True, blank=True)
    min_concentr_phosphate = models.DecimalField(max_digits=5,
                                                 decimal_places=3,
                                                 null=True, blank=True)
    incr_concentr_phosphate = models.DecimalField(max_digits=5,
                                                  decimal_places=3,
                                                  null=True, blank=True)
    min_concentr_nitrogen = models.DecimalField(max_digits=5, decimal_places=3,
                                                null=True, blank=True)
    incr_concentr_nitrogen = models.DecimalField(max_digits=5,
                                                 decimal_places=3,
                                                 null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.code, self.name)


class BucketsType(models.Model):
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
    replace_impact_by_nutricalc = models.BooleanField()
    is_computed = models.BooleanField()
    ts_flowoff = models.ForeignKey(TimeSeriesCache,
                              null=True, blank=True,
                              related_name='ts_flowoff_bucket',
                              limit_choices_to={
            'parametercache': parameter('flowoff')})
    ts_drainageindraft = models.ForeignKey(TimeSeriesCache,
                              null=True, blank=True,
                              related_name='ts_drainageindraf_bucket',
                              limit_choices_to={
            'parametercache': parameter('drainage_indraf')})
    ts_referenceoverflow = models.ForeignKey(TimeSeriesCache,
                              null=True, blank=True,
                              related_name='ts_referenceoverflow_bucket',
                              limit_choices_to={
            'parametercache': parameter('referenceoverflow')})
    surface = models.DecimalField(max_digits=10, decimal_places=1,
                                  null=True, blank=True)
    kwelwegz_is_ts = models.BooleanField()
    kwelwegz = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    ts_kwelwegz = models.ForeignKey(TimeSeriesCache,
                                    null=True, blank=True,
                                    related_name='ts_kwelwegz_bucket',
                                    limit_choices_to={
            'parametercache': parameter('kwelwegz')})
    porosity = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    crop_evaporation_factor = models.DecimalField(max_digits=5,
                                                  decimal_places=3,
                                                  null=True, blank=True)
    min_crop_evaporation_factor = models.DecimalField(max_digits=5,
                                                      decimal_places=3,
                                                      null=True, blank=True)
    drainage_fraction = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    indraft_fraction = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    man_water_level = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    min_water_level = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    bottom_porosity = models.DecimalField(max_digits=5, decimal_places=3,
                                   null=True, blank=True)
    bottom_crop_evaporation_factor = models.DecimalField(max_digits=5,
                                                         decimal_places=3,
                                                         null=True, blank=True)
    bottom_min_crop_evaporation_factor = models.DecimalField(max_digits=5,
                                                         decimal_places=3,
                                                         null=True, blank=True)
    bottom_drainage_fraction = models.DecimalField(max_digits=5,
                                                   decimal_places=3,
                                                   null=True, blank=True)
    bottom_indraft_fraction = models.DecimalField(max_digits=5,
                                                  decimal_places=3,
                                                  null=True, blank=True)
    bottom_max_water_level = models.DecimalField(max_digits=5,
                                                 decimal_places=3,
                                                 null=True, blank=True)
    bottom_min_water_level = models.DecimalField(max_digits=5,
                                                 decimal_places=3,
                                                 null=True, blank=True)
    init_water_level = models.DecimalField(max_digits=5, decimal_places=3,
                                           null=True, blank=True)
    bottom_init_water_level = models.DecimalField(max_digits=5,
                                                  decimal_places=3,
                                                  null=True, blank=True)
    concentr_chloride_flow_off = models.DecimalField(max_digits=5,
                                                     decimal_places=3,
                                                     null=True, blank=True)
    concentr_chloride_drainage_indraft = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_phosphate_flow_off = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_phosphate_drainage_indraft = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    incr_concentr_phosphate_flow_off = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    incr_concentr_phosphate_drainage_indraft = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_nitrogen_flow_off = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    min_concentr_nitrogen_drainage_indraft = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        null=True, blank=True)
    incr_concentr_nitrogen_flow_off = models.DecimalField(
        max_digits=5, decimal_places=3,
        null=True, blank=True)
    incr_concentr_nitrogen_drainage_indraft = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        null=True, blank=True)
    label_flow_off = models.DecimalField(max_digits=5,
                                         decimal_places=3,
                                         null=True, blank=True)
    label_drainaige_indraft = models.DecimalField(max_digits=5,
                                                  decimal_places=3,
                                                  null=True, blank=True)
