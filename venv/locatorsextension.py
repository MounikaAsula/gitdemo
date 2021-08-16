from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element_by_css_selector('#username').send_keys("mounika")
driver.find_element_by_css_selector('.password').send_keys("mouni")
driver.find_element_by_css_selector('.password').clear()
driver.find_element_by_link_text('Forgot Your Password?').click()
driver.find_element_by_xpath("//input[@name = 'cancel']").click()
print(driver.find_element_by_xpath("//div[@id = 'usernamegroup']/label").text)

print(driver.find_element_by_xpath("//form[@name = 'login']/label").text)
