from selenium import webdriver
import selenium, time


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://the-internet.herokuapp.com/windows')

driver.find_element_by_link_text('Click Here').click()

# Switching windows, windows handles is a list, element 0 is parent
childWindow = driver.window_handles[1]
driver.switch_to_window(childWindow)

print(driver.find_element_by_tag_name('h3').text)

# Driver close only closes the current focus tab
driver.close()

# Switch back to parent tab
driver.switch_to_window(driver.window_handles[0])

print(driver.find_element_by_tag_name('h3').text)


