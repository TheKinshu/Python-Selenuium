from selenium import webdriver
import selenium


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/angularpractice/')

# driver.find_element_by_name('name').send_keys("Kev")
driver.find_element_by_css_selector("input[name = 'name']").send_keys('kev')
driver.find_element_by_name('email').send_keys('test@gmail.com')



driver.find_element_by_id('exampleCheck1').click()

driver.find_element_by_xpath("//input[@value='Submit']").click()

print(driver.find_element_by_class_name('alert-success').text)