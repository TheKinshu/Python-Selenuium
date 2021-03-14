from SeleniumTesting.pageObject.HomePage import HomePage
from Selenium.logging.baseClase import BaseClass
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from SeleniumTesting.utilities.BaseClass import BaseClass

class TextHomePage(BaseClass):

    def text_formSubmission(self):

        homePage = HomePage(self.driver)

        homePage.getName().send_keys('kev')
        homePage.getEmail().send_keys('test@gmail.com')
        homePage.getCheckBox().click()

        dropDown = Select(homePage.getGender())
        dropDown.select_by_visible_text('Male')

        homePage.submission().click()

        message = homePage.getMessage().text

        assert 'success' in message
