from django.test import TestCase

from foodfinder.algorythms import Algorythm

# Create your tests here.
class AlgorythmsrTestCase(TestCase):
    """ AlgorythmsrTestCase test the Food Algorythm Substitute Finder """

    def setUp(self):
        pass

    def test_get_algorythm_by_classname(self):
        algorythm = Algorythm.get_algorythm_by_classname('ByFat')

        self.assertEqual(algorythm.__name__, 'ByFat')
