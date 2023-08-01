from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

USER_EMAIL = "YOUR_EMAIL"
USER_PASSWORD = "YOUR_PASSWORD"

driver = webdriver.Chrome()

driver.get("http://tinder.com/")

time.sleep(3)


cookies = driver.find_element(By.XPATH, '//*[@id="s-2082074848"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

time.sleep(3)

login = driver.find_element(By.XPATH, '//*[@id="s-2082074848"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(3)

facebook = driver.find_element(By.XPATH, '//*[@id="s484511372"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook.click()

time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

facebook_cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[1]')
facebook_cookies.click()

time.sleep(1)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(USER_EMAIL)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(USER_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(15)

localization = driver.find_element(By.XPATH, '//*[@id="s484511372"]/main/div/div/div/div[3]/button[1]')
localization.click()

time.sleep(3)

notifications = driver.find_element(By.XPATH, '//*[@id="s484511372"]/main/div/div/div/div[3]/button[2]')
notifications.click()

time.sleep(5)


for n in range(100):
    time.sleep(3)
    try:
        print("Trying")

        like_button = driver.find_element(By.XPATH, '//*[@id="s-2082074848"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            match.click()

        except NoSuchElementException:
            time.sleep(3)

time.sleep(3)
driver.quit()
