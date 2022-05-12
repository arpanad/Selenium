import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH, "//button[text()='OK']").click()
driver.find_element(By.XPATH, "//a[text()=' REGISTER ']").click()
time.sleep(10)
driver.find_element_by_id('userName').send_keys('UserName123')
driver.find_element(By.XPATH, "//input[@id='userName']/following::input").send_keys('Password987')
driver.find_element(By.XPATH, "//input[@id='usrPwd']/following::input").send_keys('Password987')
driver.find_element(By.XPATH, "//span[text()='Preferred Language']").click()
driver.find_element(By.XPATH, "//span[text()='English']").click()
driver.find_element(By.XPATH, "//span[text()='Security Question']").click()
driver.find_element(By.XPATH,"//li[@role='option']//following::li[2]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Security Answer']").send_keys("hero")
driver.find_element(By.XPATH, "//button[@label='Continue']").click()
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys('FirstNameArp')
driver.find_element(By.XPATH, "//input[@id='middleName']").send_keys('middleName')
driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys('lastName')
driver.find_element(By.XPATH, "//span[text()='Select Occupation']").click()
driver.find_element(By.XPATH, "//span[text()='SELF EMPLOYED']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Date Of Birth']").click()
#driver.find_element(By.XPATH, "//select[contains(@class,'month')]").click()
import pdb; pdb.set_trace()
months = driver.find_element(By.XPATH, "//select[contains(@class,'month')]")
month = Select(months)
month.select_by_value('9')
dates = driver.find_element(By.XPATH, "//select[contains(@class,'datepicker')]")
date = Select(dates)
date.select_by_visible_text()

