# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models

from lizard_area.models import Area
from lizard_fewsnorm.models import Series
from lizard_esf.models import Configuration


class AreaConfiguration(models.Model):
    """
    Areaconfiguration.
    """
    area = models.ForeignKey(
        Area,
        related_name='wbconfiguration_areaconfiguration_set',
    )
    configuration = models.ForeignKey(
        Configuration,
        related_name='wbconfiguration_areaconfiguration_set',
    )
    manual = models.BooleanField()
    manual_value = models.DecimalField(max_digits=15, decimal_places=6)
    timeseries_manual = models.ForeignKey(
        Series,
        related_name='wbconfiguration_areaconfiguration_set1',
    )
    timeseries_automatic = models.ForeignKey(
        Series,
        related_name='wbconfiguration_areaconfiguration_set2',
    )
    timeseries_final_value = models.ForeignKey(
        Series,
        related_name='wbconfiguration_areaconfiguration_set3',
    )


class Structure(models.Model):
    pass


class Bucket(models.Model):
    pass
