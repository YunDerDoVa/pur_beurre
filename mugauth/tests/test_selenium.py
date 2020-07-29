import os

from django.test import LiveServerTestCase
from django.conf import settings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AuthSeleniumTestCase(LiveServerTestCase):

    USERNAME = 'TestUser'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    def setUp(self):
        try:
            self.selenium = webdriver.Firefox()
        except:
            pass

        super(FoodfinderSeleniumTestCase, self).setUp()

    def tearDown(self):
        try:
            self.selenium.quit()
        except:
            pass

        super(FoodfinderSeleniumTestCase, self).tearDown()

    def test_next_redirect(self):
        if os.environ.get('TRAVIS', 'False') != 'False':
            selenium = self.selenium
            #Opening the link we want to test
            selenium.get('http://127.0.0.1:8000/favor/')
            #find the form element
            email = selenium.find_element_by_id('id_email')
            password = selenium.find_element_by_id('id_password')

            submit = selenium.find_element_by_name('submit')

            #Fill the form with data
            email.send_keys(self.EMAIL)
            password.send_keys('self.PASSWORD')

            #submitting the form
            submit.send_keys(Keys.RETURN)

            #check the returned result
            self.assertTemplateUsed('foodfinder/favors_page.html.django')
