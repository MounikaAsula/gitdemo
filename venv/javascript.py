from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

name = driver.find_element_by_xpath('//ul[@class="navbar-nav"]/li[2]/a')

driver.execute_script("arguments[0].click()",name)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")