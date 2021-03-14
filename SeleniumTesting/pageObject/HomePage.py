from SeleniumTesting.pageObject.CheckoutPage import CheckOutPage
from selenium.webdriver.common.by import By


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, 'email')
    checkBox = (By.ID, 'exampleCheck1')
    gender = (By.ID, 'exampleFormControlSelect1')
    submitBtn = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CLASS_NAME, 'alert-success')
    #
    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        #
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)

        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    
    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)
    
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    
    def submission(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getMessage(self):
        return self.driver.find_element(*HomePage.successMessage)