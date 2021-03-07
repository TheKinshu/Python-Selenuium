from selenium import webdriver
from selenium.webdriver import ActionChains
import selenium


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/AutomationPractice')

# Action chain is a way to create automation mouse movement
action = ActionChains(driver)

location = driver.find_element_by_id('mousehover')

# You can do a chain of actions for mouse movement but -
# perform() is required for it act
action.move_to_element(location).perform()

childMenu = driver.find_element_by_link_text('Reload')
action.move_to_element(childMenu).click().perform()