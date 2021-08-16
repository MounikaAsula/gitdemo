from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")
driver.get("https://www.flipkart.com/")
driver.maximize_window()
#driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()
driver.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']").send_keys("7013215167")
driver.find_element_by_css_selector("input[type ='password']").send_keys("mounika@3109")
driver.find_element_by_xpath('//button[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")



#print(driver.title)
#print(driver.current_url)


#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.minimize_window()
#driver.back()
#driver.refresh()
#driver.close()