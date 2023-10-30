import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

time.sleep(20)

driver.quit()