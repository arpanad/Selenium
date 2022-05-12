import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys('Arp123')
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys('Lastname')
driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys('House number, street, area , city')
driver.find_element(By.XPATH, "//input[@type='email']").send_keys('email.id@gmail.com')
driver.find_element(By.XPATH, "//input[@type='tel']").send_keys('7845768790')
driver.find_element(By.XPATH, "//input[@value='FeMale']").click()
driver.find_element(By.XPATH, "//input[@value='Movies']").click()
#driver.find_element(By.XPATH, "//div[@id='msdd']").click()
#driver.find_element(By.XPATH, "//a[text()='English']").click()
skills = driver.find_element_by_id("Skills")
skill = Select(skills)
skill.select_by_value('Matlab')

#driver.find_element(By.XPATH, "//span[@role='combobox']").click()
#driver.find_element(By.XPATH, "//li[text()='India']").click()

years = driver.find_element_by_id('yearbox')
year = Select(years)
year.select_by_visible_text('1970')

months = driver.find_element(By.XPATH, "//select[@placeholder='Month']")
month = Select(months)
month.select_by_value('May')
#import pdb; pdb.set_trace()

days = driver.find_element_by_id('daybox')
day = Select(days)
day.select_by_index('10')

driver.find_element(By.XPATH, "//input[@id='firstpassword']").send_keys('456Password')
driver.find_element(By.XPATH, "//input[@id='firstpassword']//following::input[1]").send_keys('456Password')
driver.find_element_by_name('signup')
import pdb; pdb.set_trace()
driver.close()

