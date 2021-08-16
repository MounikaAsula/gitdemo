from  selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdowfnsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")
for country in countries:
    if country.text == "India" :
        country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"