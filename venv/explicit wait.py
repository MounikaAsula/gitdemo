from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
list1 = []
list2 = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(2)
#veggies = driver.find_elements_by_xpath("//h4[@class='product-name']")
#for vegie in veggies:
#    print(vegie.text)
list = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for i in list:
    list1.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()
print(list1)
driver.find_element_by_xpath('//img[@alt="Cart"]').click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoCode')))
products = driver.find_elements_by_css_selector(".product-name")
for product in products:
    list2.append(product.text)
print(list2)
assert list1 == list2
driver.find_element_by_css_selector('.promoCode').send_keys("rahulshettyacademy")
driver.find_element_by_css_selector('.promoBtn').click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
orgamt = driver.find_element_by_css_selector(".totAmt").text
print(orgamt)
discamt = driver.find_element_by_css_selector(".discountAmt").text
print(discamt)
assert int(orgamt) > float(discamt)
print(driver.find_element_by_css_selector("span.promoInfo").text)

totamt = driver.find_elements_by_xpath('//tr/td[5]/p')
sum = 0
for amt in totamt:
    sum+=int(amt.text)
print(sum)
amtor = int(driver.find_element_by_css_selector('.totAmt').text)
print(amtor)
assert amtor == sum

driver.close()