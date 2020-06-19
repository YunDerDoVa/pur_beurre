from django.test import TestCase


from foodfinder.views import home


class ViewsTestCase(TestCase):

    VALID_DATA = {'search_term': 'chocolat'}
    NON_VALID_DATA = {'form': 'chocolat'}

    def setUp(self):
        pass

    def test_home_template_used(self):
        pass

    def test_search_perform_search_valid(self):

        # url : reverse()
        # data : dict
        response = self.client.post(url, data)

        pass

# assert code=200
# response.content : html
# response.context : context de render
# self.assertTemplateUsed : vérifie le bon template (!= ...NotUsed)
