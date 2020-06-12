from django.test import TestCase

from unittest.mock import MagicMock, patch


from filler.openfoodfacts.database import OFFDatabase, OFFSearch


# Create your tests here.
class OpenFoodFactsTestCase(TestCase):

    SEARCHS = []

    def setUp(self):
        self.database = OFFDatabase()

    def test_connexion(self):
        self.assertEqual(self.database.get_connexion(), True)

    def test_update_database(self):
        self.database.update_database(test=True)

        self.assertTrue(len(self.database.searchs) > 0)
