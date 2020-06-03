from django.test import TestCase


from filler.openfoodfacts.database import OFFDatabase, OFFSearch


# Create your tests here.
class OpenFoodFactsTestCase(TestCase):

    SEARCHS = [
        OFFSearch(1, 1),
        OFFSearch(1, 1),
        OFFSearch(1, 1),
    ]

    def setUp(self):
        self.database = OFFDatabase()

    def test_get_connexion(self):

        self.assertEqual(type(True), type(self.database.get_connexion()))

    def test_get_database(self):

        self.database.update_database()

        self.assertEqual(self.SEARCHS, self.database.searchs)

    def test_update_django(self):

        self.database.update_django()

        query = []

        self.assertEqual(len(self.SEARCHS), len(query))
