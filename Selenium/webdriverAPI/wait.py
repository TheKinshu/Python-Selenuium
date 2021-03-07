from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By
import selenium, time

# List to validate the items
cart = []
cart2 = []


driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

# This applies to the whole program
# It waits for a certain amount of time until - 
# object is displayed
driver.implicitly_wait(5)

# Implicit will wait 5 second after the the intial 1.5 sec wait 
# Explicit wait will wait until the a certain action is achieved 

# Search for all product with ber
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')

time.sleep(4)

# Find how many product was found
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))

# Assert error if count is not equal to 3
assert count == 3

# Find all the button and add them to the cart
buttons =  driver.find_elements_by_xpath("//div[@class='product-action']/button")

# //div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    cart.append(button.find_element_by_xpath('parent::div/parent::div/h4').text)
    button.click()


# Go to checkout
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# Wait for the website to finish loading to input coupon
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'promoCode')))


# Grab all checkout item and put them into cart3
checkout = driver.find_elements_by_css_selector('p.product-name')

for check in checkout:
    cart2.append(check.text)

assert cart == cart2

# Grab the total cost of everything
totalAmount = driver.find_element_by_css_selector('.totAmt').text


# Enter promo code
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
driver.find_element_by_css_selector('.promoBtn').click()

# Wait for promo code to proccess
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'span.promoInfo')))

discount = driver.find_element_by_css_selector('.discountAmt').text

# Assert error if promo code failed to applied
assert float(totalAmount) > float(discount)

# Validate the final sum total
sums = driver.find_elements_by_xpath('//tr/td[5]/p')
total = 0

for sum in sums:
    total = total + int(sum.text)


assert float(totalAmount) == total

print('$' + str(total))
print('Complete')

