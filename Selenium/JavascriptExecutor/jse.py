# Javascript DOM can access any elements on web page like selenium
# Selenium using Javascript are uncommon but it is there when-
# Selenium isn't working on the page
from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name('name').send_keys('hello')

# These 2 lines does the same but one execute through javascript
print(driver.find_element_by_name('name').get_attribute('value'))
# print(driver.execute_script("return document.getElementsByName('name')[0].value"))

shopBtn = driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script("arguments[0].click();", shopBtn)

# Selenium default does not have a scroll option but you can -
# access Javacript to scroll down the page for you
driver.execute_script('window.scrollTo(0,dicynebt.body.scrollHeight);')
print('dfs')