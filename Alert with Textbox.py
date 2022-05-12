import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:/Users/Arpana/PycharmProjects/LearnSelenium/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, value='Alert with Textbox').click()
driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Waiting for alert to appear')
    alert = driver.switch_to.alert
    alert.send_keys('Arpana')
    time.sleep(2)
    alert.accept()
    time.sleep(2)
    text1 = driver.find_element(By.ID, 'demo1').text
    print('The Text is:')
    print(text1)
except:
    print('No Alerts observed')
finally:
    driver.close()

