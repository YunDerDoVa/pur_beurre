from django.test import TestCase

from foodfinder.food_manager import FoodManager

# Create your tests here.
class FoodSearchManagerTestCase(TestCase):
    """ FoodSearchManagerTestCase test the Food Search Manager system """

    def setUp(self):
        self.food_manager = FoodManager()
        self.food_manager.update_db()

    def test_search(self):
        substitutes = self.food_manager.search_substitutes(Food.objects.first())

        self.assertTrue(len(substitutes) > 0 or substitutes is None)

    def test_search_by_salt(self):
        substitutes = self.food_manager.search_substitutes(Food.objects.first(), algorythm='BySalt')

        self.assertTrue(len(substitutes) > 0 or substitutes is None)

    def test_search_by_fat(self):
        substitutes = self.food_manager.search_substitutes(Food.objects.first(), algorythm='ByFat')

        self.assertTrue(len(substitutes) > 0 or substitutes is None)

    def test_status_cached_coverage(self):
        status = self.food_manager.status_cached_coveraage()

        self.assertTrue(type('') == type(status))
