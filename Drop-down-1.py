import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/newtours/register.php")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_name("firstName").send_keys("Arpana")
driver.find_element_by_name("lastName").send_keys("M Dandin")
driver.find_element_by_name("phone").send_keys("997278995")
driver.find_element_by_id("userName").send_keys("arpanadandin@gmail.com")
driver.find_element_by_name("address1").send_keys("Vishwapriyanagar")
driver.find_element_by_name("city").send_keys("Bangalore")
driver.find_element_by_name("state").send_keys("Karnataka")
driver.find_element_by_name("postalCode").send_keys("560068")
countries = driver.find_element(By.XPATH, "//select[@name='country']")
country = Select(countries)
country.select_by_visible_text("INDIA")
driver.find_element_by_id("email").send_keys("arpanad")
driver.find_element_by_name("password").send_keys("password123")
driver.find_element_by_name("confirmPassword").send_keys("password123")
driver.find_element_by_name("submit").click()
driver.close()