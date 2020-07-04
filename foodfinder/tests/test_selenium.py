from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


from mugauth.models import Account


class MySeleniumTests(StaticLiveServerTestCase):

    USERNAME = 'Test'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    def setUp(self):

        account = Account.objects.create_user(username=self.USERNAME, email=self.EMAIL, password=self.PASSWORD)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('{0}{1}'.format(self.live_server_url, '/auth/login/'))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys(self.EMAIL)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.PASSWORD)
        #self.selenium.find_element_by_xpath('//input[@value="submit"]').click()
