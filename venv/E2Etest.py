import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector('a[href*="shop"]').click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    options = product.find_element_by_xpath("div/h4").text
    print(options)
    if options == "Blackberry":
        product.find_element_by_xpath("div[2]/button").click()

driver.find_element_by_css_selector(".btn-primary").click()
assert "Blackberry" == driver.find_element_by_xpath('//div[@class="media-body"]/h4').text
driver.find_element_by_css_selector(".btn-success").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="suggestions"]/ul')))
#time.sleep(8)
driver.find_element_by_xpath('//div[@class="suggestions"]/ul[1]').click()
driver.find_element_by_xpath('//div[@class="checkbox checkbox-primary"]').click()
driver.find_element_by_css_selector('.btn-success').click()
print(driver.find_element_by_css_selector('.alert-success').text)
driver.get_screenshot_as_file('end2end.png')