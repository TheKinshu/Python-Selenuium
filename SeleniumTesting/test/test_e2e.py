from SeleniumTesting.pageObject.HomePage import HomePage
import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By
from SeleniumTesting.utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        cards = checkOutPage.getCardTitles()

        i = -1        
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == 'Blackberry':
                checkOutPage.getCardFooter()[i].click()


        self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()

        confirmPage = checkOutPage.CheckOutItems()
        confirmPage.countrySubmit()
        success = confirmPage.confirmPurchase()

        assert 'Success! Thank you!' in success

        self.driver.get_screenshot_as_file('success.png')