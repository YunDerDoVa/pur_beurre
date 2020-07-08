from django.test import TestCase

from django.urls import reverse


class AutocompleteTestCase(TestCase):

    NAME = 'TestFood'
    RESPONSE = {'names': []}

    def setUp(self):
        pass

    def test_food_name(self):

        response = self.client.get(reverse('autocomplete_foodname') + '?name=' + self.NAME)

        self.assertEqual(response.status_code, 200)
