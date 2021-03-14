from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from SeleniumTesting.utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):
    
    countryTxt = (By.ID, 'country')
    linkTxt = (By.LINK_TEXT, 'India')

    agreeBtn = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")

    alertMsg = (By.CLASS_NAME, 'alert-success')

    def __init__(self, driver):
        
        self.driver = driver

    def countrySubmit(self):

        self.driver.find_element(*ConfirmPage.countryTxt).send_keys('ind')
        
        self.verifyLinkPresence('India')

        self.driver.find_element(*ConfirmPage.linkTxt).click()

    def confirmPurchase(self):

        self.driver.find_element(*ConfirmPage.agreeBtn).click()
        self.driver.find_element(*ConfirmPage.purchase).click()

        return self.driver.find_element(*ConfirmPage.alertMsg).text
        