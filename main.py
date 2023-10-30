import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

ACCOUNT_EMAIL = "ianwairimu4@gmail.com"
ACCOUNT_PASSWORD = "#xnova-hacker4"

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Chrome()

APP_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3632673256&distance=25&f_AL=true&f_E=2%2C3%2C4&f_WT=2&geoId=103644278&keywords=software%20engineer'

driver.get(APP_URL)
driver.maximize_window()

time.sleep(1)

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

time.sleep(1)

username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)

btn = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
btn.submit()



# image3
time.sleep(100)
easy_apply = driver.find_element(By.CSS_SELECTOR, "button.jobs-apply-button")
easy_apply.click()

next_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
next_btn.click()

cover_letter = driver.find_element(By.ID, 'multiline-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3632673256-2424461457389151447-text')

cover_letter.send_keys("Ian Wairimu is my name")
next_btn.click()

time.sleep(1000)

driver.quit()