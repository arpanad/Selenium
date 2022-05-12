from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

#frame1 = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']") #try
driver.switch_to.frame(1)

#frame2 = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']") try
driver.switch_to.frame(0)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys('Arpana')
driver.close()