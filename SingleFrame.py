from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()
singleFrame = driver.find_element_by_id('singleframe')
driver.switch_to.frame(singleFrame)
driver.find_element(By.XPATH, "//div[contains(@class,'offset-5')]//following::input[1]").send_keys('Arpana')
driver.close()