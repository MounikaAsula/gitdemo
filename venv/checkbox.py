from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
varable="mounika"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
options = Select(driver.find_element_by_id("dropdown-class-example"))
options.select_by_index(2)
buttons = driver.find_elements_by_css_selector("input[type = 'checkbox']")
print(len(buttons))
for button in buttons:
    if button.get_attribute("value") == "option2":
        button.click()
        assert button.is_selected()
radio = driver.find_elements_by_name("radioButton")
radio[2].click()
driver.find_element_by_id("name").send_keys(varable)
driver.find_element_by_id("alertbtn").click()
alerts = driver.switch_to.alert
alerttext = alerts.text
assert varable in alerttext
alerts.accept()