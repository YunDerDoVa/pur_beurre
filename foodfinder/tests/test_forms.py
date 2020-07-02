from django.test import TestCase


from foodfinder.forms import SearchForm


class FormsTestCase(TestCase):

    SEARCH_TERM = 'Chocolat'
    FORM_DATA = {'search_term': SEARCH_TERM}

    def setUp(self):
        self.form = SearchForm(data=self.FORM_DATA)
        self.form.search_term = self.SEARCH_TERM

    def test_search_form(self):

        search_term = self.form.get_search_term()

        self.assertEqual(search_term, self.SEARCH_TERM)
