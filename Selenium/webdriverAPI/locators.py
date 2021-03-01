from selenium import webdriver
from selenium.webdriver.support.ui import Select
import selenium


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/angularpractice/')

# Driver.find_element_by_name('name').send_keys("Kev")
driver.find_element_by_css_selector("input[name = 'name']").send_keys('kev')
driver.find_element_by_name('email').send_keys('test@gmail.com')


# Click the button
driver.find_element_by_id('exampleCheck1').click()


# Drop down menu
# Select class provide the methods to handle the options in dropdown
dropDown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
dropDown.select_by_visible_text('Female')
dropDown.select_by_index(0)

driver.find_element_by_xpath("//input[@value='Submit']").click()

message = driver.find_element_by_class_name('alert-success').text

assert 'success' in message

driver.close()