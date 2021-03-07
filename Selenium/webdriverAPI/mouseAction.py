from selenium import webdriver
from selenium.webdriver import ActionChains
import selenium


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')

# Action chain is a way to create automation mouse movement
action = ActionChains(driver)

action.double_click(driver.find_element_by_id('double-click')).perform()

# Context click performs right click
action.context_click().perform()


alert = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == alert.text

alert.accept()