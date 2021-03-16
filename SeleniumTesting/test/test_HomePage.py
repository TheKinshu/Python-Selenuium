from inspect import getdoc
import logging
import pytest

from SeleniumTesting.pageObject.HomePage import HomePage
from SeleniumTesting.utilities.BaseClass import BaseClass
from SeleniumTesting.TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        
        log = self.getLogger()

        homePage = HomePage(self.driver)
        
        log.info('Entering Information')
        log.info('--------------------')

        name = homePage.getName().send_keys(getData['name'])
        email = homePage.getEmail().send_keys(getData['email'])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData['gender'])
        log.info('Name: ' + str(name)  + ', Email: ' + str(email) + ' Gender: ' + str(getData['gender']))
        log.info('--------------------')
        log.info('End of information')
        homePage.submission().click()

        message = homePage.getMessage().text

        log.info('Web page message: ' + message)
        assert 'success' in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData('testcase2'))
    def getData(self, request):
        return request.param
