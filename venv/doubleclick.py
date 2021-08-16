from  selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
click = driver.find_element_by_id("double-click")
action.context_click(click).perform()
action.double_click(click).perform()
mouni = driver.switch_to.alert
print(mouni.text)
assert "You double clicked me!!!, You got to be kidding me" == mouni.text
mouni.accept()



