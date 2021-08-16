from  selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#action = ActionChains(driver)
#child = driver.find_element_by_id('mousehover')
#action.move_to_element(child).perform()
#child2 = driver.find_element_by_link_text('Reload')
#action.move_to_element(child2).click().perform()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#action = ActionChains(driver)
print(driver.find_element_by_id('displayed-text').is_displayed())

driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_id('displayed-text').is_displayed())