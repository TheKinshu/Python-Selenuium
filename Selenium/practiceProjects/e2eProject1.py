from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# //div[@class='card h-100']/div/h4/a

for product in products:
    productN = product.find_element_by_xpath('div/h4/a').text
    if productN == 'Blackberry':
        # Add item to cart
        # You dont need to specifiy which div if the
        # element only has 1 button otherwise it is needed
        # an element must be specified.
        # Ex: 'div[2]/button'
        product.find_element_by_xpath('div/button').click()


driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()

driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

driver.find_element_by_id('country').send_keys('ind')

wait = WebDriverWait(driver,7)

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))

driver.find_element_by_link_text('India').click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

driver.find_element_by_css_selector("[type='submit']").click()

success = driver.find_element_by_class_name('alert-success').text

assert 'Success! Thank you!' in success

driver.get_screenshot_as_file('success.png')