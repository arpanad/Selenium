import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, value='Alert with OK').click()
driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Waiting for alert to appear')
    driver.switch_to.alert.accept()
except:
    print('No alerts observed')
finally:
    driver.close()

