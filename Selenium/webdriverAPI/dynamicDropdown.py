from selenium import webdriver
import time
import selenium


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element_by_id('autosuggest').send_keys('ind')

time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break

# Since the website isn't updated you are unable to -
# grab any information from the text box dispite inputing information beforehand
# driver.find_element_by_id('autosuggest').text

assert driver.find_element_by_id('autosuggest').get_attribute('value') == 'India'



