from selenium import webdriver
import selenium, time


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://the-internet.herokuapp.com/iframe')

# Switch to iframe, frameset, frame but require frame id
driver.switch_to.frame('mce_0_ifr')

driver.find_element_by_css_selector('#tinymce').clear()
driver.find_element_by_css_selector('#tinymce').send_keys('I am able to automate')


# When switching focus of driver you must switch back -
# in order to interact with other content of the page
# Switch back to default
driver.switch_to.default_content()

print(driver.find_element_by_tag_name('h3').text)
