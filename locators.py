
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("mounika")
driver.find_element_by_css_selector("input[name = 'email']").send_keys("mounika.asula@tcs.com")
driver.find_element_by_xpath("//input[@id = 'exampleInputPassword1']").send_keys("Mounika@3109")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@type = 'submit']").click()
messagr = driver.find_element_by_css_selector("[class*='alert-dismissible']").text
print(messagr)
assert "Success! The Form has been submitted successfully!." in messagr
