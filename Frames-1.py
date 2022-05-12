from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://w3schools.com/js/tryit.asp?filename=tryjs_prompt")

frame1 = driver.find_element_by_name('iframeResult')
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH, "//button[text()='Try it']").click()