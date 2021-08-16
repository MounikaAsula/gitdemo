from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
list1 = []
list2 = []
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(2)
products = driver.find_elements_by_xpath('//div[@class="product"]/h4')
for product in products:
    list1.append(product.text)
print(list1)
#search-button
driver.find_element_by_xpath("//input[@type='search']")
driver.find_element_by_css_selector('.search-button').click()
products = driver.find_elements_by_xpath('//div[@class="product"]/h4')
for product in products:
    list2.append(product.text)
print(list2)
assert list1 == list2
driver.close()