from django.test import TestCase

from unittest.mock import MagicMock, patch


from filler.openfoodfacts.database import OFFDatabase, OFFSearch
from foodfinder.models import Food


# Create your tests here.
class OpenFoodFactsTestCase(TestCase):

    SEARCHS = []
    PRODUCT = {
        'product_name': 'Name',
        'code': '0000000',
        'nutriments': {'fat': 1.2},
        'categories_tags': ['Chocolat', 'Sugar'],
        'img_front_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'img_back_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'nutriscore_data': {'nutriscore_score': 1},
    }

    def setUp(self):
        for i in range(3):
            self.SEARCHS.append(
                OFFSearch(i, 'Test', 1, 1).set_product(self.PRODUCT)
            )

    @patch('filler.openfoodfacts.database.OFFDatabase')
    def test_get_database(self, mock_offdatabase):

        database = OFFDatabase()

        mock_offdatabase._fetch_categories.return_value = self.SEARCHS

        #self.database._fetch_categories = MagicMock(return_value=self.SEARCHS)

        self.database.update_database(test=True)

        self.assertEqual(self.SEARCHS, database.searchs)

    @patch('filler.openfoodfacts.database.OFFDatabase')
    def test_update_django(self, mock_offdatabase):

        database = OFFDatabase()

        mock_offdatabase._fetch_categories.return_value = self.SEARCHS

        database.update_database(test=True)
        database.update_django()

        query = Food.objects.filter(name='TestFood')

        self.assertEqual(len(self.SEARCHS), len(query))
