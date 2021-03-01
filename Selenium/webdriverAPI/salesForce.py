from selenium import webdriver
import selenium


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://login.salesforce.com/?locale=ca')
driver.find_element_by_css_selector('#username').send_keys('kev')
driver.find_element_by_css_selector('.password').send_keys('testing1')

# Finds the tag name with the following text and click on <a> tag
driver.find_element_by_link_text('Forgot Your Password?').click()

driver.find_element_by_xpath("//a[text()='Cancel']").click()
temp = driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text

print(temp)
print('done')

# Notes
# You can find the child tag from the parent tag with a '/' in xpath //div[id='usernamegroup']/label
# but for css you just need to input child tag after parent tag div[id='usernamegroup']label