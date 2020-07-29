import os

from django.test import LiveServerTestCase
from django.conf import settings

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys


class FoodfinderSeleniumTestCase(LiveServerTestCase):

    USERNAME = 'TestUser'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(FoodfinderSeleniumTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(FoodfinderSeleniumTestCase, self).tearDown()

    def test_save_button(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')
        #find the form element
        email = selenium.find_element_by_id('food_input')

        submit = selenium.find_element_by_name('submit')

        #Fill the form with data
        email.send_keys('tomates')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        test_1 = 'sauvegarder' in selenium.page_source
        self.assertTrue(not test_1)
        self.assertTemplateUsed('foodfinder/results_page.html.django')
