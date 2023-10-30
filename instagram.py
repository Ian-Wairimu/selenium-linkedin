import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/reels/")
driver.maximize_window()

time.sleep(4)

username = driver.find_element(By.NAME, "username")
username.send_keys("ian_w.moon")

password = driver.find_element(By.NAME, "password")
password.send_keys("#moon254")
password.send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0, 200);")

time.sleep(1000)


driver.close()