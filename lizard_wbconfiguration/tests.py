# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.test import TestCase
from lizard_area.models import Area
from lizard_wbconfiguration.models import AreaConfiguration
from lizard_wbconfiguration.models import StructureInOut
from lizard_wbconfiguration.api.views import WaterBalanceAreaObjectConfiguration
from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point


class StructureTest(TestCase):

    def setUp(self):
        self.area = None
        self.area_configuration = None

    def create_area(self):
        user = User(username='admin', password='admin')
        user.save()
        geo_object_group = self.get_or_create_geoobjectgroup(
            user.username)
        self.area = Area(ident="test", name="test",
                         geo_object_group=geo_object_group,
                         geometry=GEOSGeometry(Point(0, 0), srid=4326),
                         data_administrator_id=1)
        self.area.save()

    def create_structure_in_out(self):
        """Add in/out objects into StructureInOut."""
        StructureInOut(code='in', index=1, decsription="In default").save()
        StructureInOut(code='uit', index=0, decsription="Uit default").save()

    def create_areaconfiguration(self, area):
        try:
            self.area_configuration = AreaConfiguration(
                ident=area.ident,
                name=area.name,
                area=area)
            self.area_configuration.save()
            return True
        except:
            return False

    def test_create_structures(self):
        self.create_area()
        self.create_areaconfiguration(self.area)
        area_object_config = WaterBalanceAreaObjectConfiguration()
        self.create_structure_in_out()
        inout_obj = StructureInOut.objects.get(code='uit')
        area_object_config.create_default_structure(
            self.area_configuration, inout_obj)
        is_created = area_object_config.exists_default_structure(
            self.area_configuration, inout_obj)
        self.assertEquals(is_created, True)

    def get_or_create_geoobjectgroup(self, user_name):
        from lizard_geo.models import GeoObjectGroup
        user_obj = User.objects.get(username=user_name)
        group_name = 'test'
        group_slug = 'test'
        geo_object_group, created = GeoObjectGroup.objects.get_or_create(
            name=group_name, slug=group_slug, created_by=user_obj)
        if created:
            geo_object_group.source_log = 'test'
            geo_object_group.save()
        return geo_object_group

    def tearDown(self):
        """Clear the Stuctures and AreaConfiguration."""
        if self.area is not None:
            Area.objects.all().delete
        if self.area_configuration is not None:
            AreaConfiguration.objects.all().delete()
