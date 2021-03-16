import pytest

from SeleniumTesting.pageObject.HomePage import HomePage
from SeleniumTesting.utilities.BaseClass import BaseClass

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By

class TestOne(BaseClass):

    def test_e2e(self):
        
        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        log.info('getting all the cards titles')
        cards = checkOutPage.getCardTitles()

        i = -1        
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == 'Blackberry':
                checkOutPage.getCardFooter()[i].click()


        self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()

        confirmPage = checkOutPage.CheckOutItems()

        log.info('Entering country name as ind')
        confirmPage.countrySubmit()
        success = confirmPage.confirmPurchase()

        log.info('Text received from application is :' + success)
        assert 'Success! Thank you!' in success
        log.info('Success')
        self.driver.get_screenshot_as_file('success.png')