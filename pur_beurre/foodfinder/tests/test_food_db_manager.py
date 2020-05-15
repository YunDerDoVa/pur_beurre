from django.test import TestCase

from foodfinder.food_manager import FoodManager

# Create your tests here.
class FoodDBManagerTestCase(TestCase):
    """ FoodDBManagerTestCase test the Food DB Manager system """

    def setUp(self):
        self.food_manager = FoodManager()

    def test_fill_database(self):
        self.food_manager.fill_db()

        self.assertTrue(Food.objects.all().count() > 0)

    def test_update_database(self):
        self.food_manager.fill_db()

        for i in range(3):
            Food.objects.first().delete()

        count = Food.objects.all().count()

        self.food_manager.update_db()

        self.assertEqual(count+3, Food.objects.all().count())

    def test_status_database(self):
        status = self.food_manager.status_db()

        self.assert(type(''), type(status))
