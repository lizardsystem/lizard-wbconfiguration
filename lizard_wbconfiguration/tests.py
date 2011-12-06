# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.test import TestCase

from lizard_area.models import Area

from lizard_fewsnorm import Location

from lizard_wbconfiguration.models import Structure
from lizard_wbconfiguration.models import AreaConfiguration


class ExampleTest(TestCase):

    def setUp(self):
        self.db_name = 'fewsnorm'
        self.structures = []
        self.area_configuration = None

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

    def fewsnorm_locations(self, area):
        locations = Location.objects.using('db_name').all()
        if locations.exists():
            locations = locations[:2]
        return locations

    def create_structures(self, locations):
        is_created = False
        for location in locations:
            try:
                structure = Structure(
                    code=location.id,
                    name=location.name,
                    area=self.area_configuration)
                structure.save()
                self.structures.append(structure)
                is_created = True
            except:
                is_created = False
        return is_created

    def test_save_structure(self):
        areas = Area.objects.all()
        is_created = False
        if areas.exists():
            self.create_areaconfiguration(areas[0])
            locations = self.fewsnorm_locations()
            is_created = self.create_structures(locations)
        self.asserEquals(is_created, True)

    def tearDown(self):
        """Clear the Stuctures and AreaConfiguration."""
        if self.area_configuration.id is not None:
            AreaConfiguration.objects.get(
                pk=self.area_configuration.id).delete()

        for structure in self.structures:
            if structure.id is not None:
                Structure.objects.get(pk=structure.id).delete()
