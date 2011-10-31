# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models

from lizard_area.models import Area
from lizard_fewsnorm import TimeSeriesKeys


class AreaConfiguration(models.Model)
    """
    Areaconfiguration. Currently copied from lizard-esf.models
    """
    area = models.ForeignKey(Area)
    configuration = models.ForeignKey(Configuration)
    manual = models.BooleanField()
    manual_value = models.DecimalField()
    timeseries_manual = models.ForeignKey(TimeSeriesKeys)
    timeseries_automatic = models.ForeignKey(TimeSeriesKeys)
    timeseries_final_value = models.ForeignKey(TimeSeriesKeys)


class Structure(models.Model):
    pass


class Bucket(models.Model):
    pass
