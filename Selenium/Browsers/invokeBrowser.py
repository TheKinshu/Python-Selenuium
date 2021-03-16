from selenium import webdriver
import selenium


# browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then -
# invoke the actual browser
driver = webdriver.Chrome(executable_path='geckodriver.exe')
# driver = webdriver.Firefox(executable_path='geckodriver.exe')

# Maximize the browser window
driver.maximize_window()

# Runs the method and call the browser with this url attached to it
driver.get('https://www.youtube.com')

# Minimize the window
driver.minimize_window()

print(driver.title)
print(driver.current_url)

driver.get('https://www.google.ca')

# Go back to previous page
driver.back()

# Refresh current page
driver.refresh()

# Closes the webdriver
# Another way to close webdriver is by using drivers.quit
# The differences is that quit closes all the webdriver - 
# while close only close the current webdriver
driver.close() 