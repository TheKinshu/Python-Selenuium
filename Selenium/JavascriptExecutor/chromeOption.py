# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

from selenium import webdriver


chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")

# Start chrome in headless mode
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)

driver.get('https://rahulshettyacademy.com/angularpractice/')

print(driver.title)