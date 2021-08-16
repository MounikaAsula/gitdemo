from  selenium import webdriver

import time


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(2)
list = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for i in list:
    i.click()
driver.find_element_by_xpath('//img[@alt="Cart"]').click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(5)
driver.find_element_by_css_selector('.promoCode').send_keys("rahulshettyacademy")
driver.find_element_by_css_selector('.promoBtn').click()
time.sleep(5)
print(driver.find_element_by_css_selector('.promoInfo').text)