from selenium import webdriver

validateText = 'Option3'

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Find the alert input field and click alert button
driver.find_element_by_css_selector('#name').send_keys(validateText)
driver.find_element_by_id('alertbtn').click()

# Switch driver to alert
alert = driver.switch_to.alert

alertTxt = alert.text

# Validate the alert text to ensure that the text is indeed there
assert validateText in alertTxt

# This clicks the ok button on alert
alert.accept()

# This clicks the cancel button on alert
# alert.dismiss()