from SeleniumTesting.pageObject.ConfirmPage import ConfirmPage
from selenium.webdriver.common.by import By


class CheckOutPage:

    cardTitle = (By.CSS_SELECTOR, '.card-title a')
    cardFooter = (By.CSS_SELECTOR, '.card-footer button')

    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)
    
    def CheckOutItems(self):
        #
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
