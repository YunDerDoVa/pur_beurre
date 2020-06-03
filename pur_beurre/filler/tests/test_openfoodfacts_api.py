from django.test import TestCase

from unittest.mock import MagicMock


from filler.openfoodfacts.database import OFFDatabase, OFFSearch
from foodfinder.models import Food


# Create your tests here.
class OpenFoodFactsTestCase(TestCase):

    SEARCHS = []

    def setUp(self):
        self.database = OFFDatabase()

        for i in range(3):
            self.SEARCHS.append(
                OFFSearch(1, 1).set_dict({'name': 'TestFood'})
            )

    def test_get_connexion(self):

        self.assertEqual(type(True), type(self.database.get_connexion()))

    def test_get_database(self):

        self.database._fetch_categories = MagicMock(return_value=self.SEARCHS)

        self.database.update_database()

        self.assertEqual(self.SEARCHS, self.database.searchs)

    def test_update_django(self):

        self.database.update_django()

        query = Food.objects.filter(name='TestFood')

        self.assertEqual(len(self.SEARCHS), len(query))
