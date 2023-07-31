from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "EMAIL"
ACCOUNT_PASSWORD = "PASS"
NUMBER = "333333333"

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3616254230&f_LF=f_AL&geoId=90009829&keywords=python%20developer&location=Katowice%20i%20okolice&refresh=true")

login_button = driver.find_element(By.LINK_TEXT, "Zaloguj się")
login_button.click()

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_jobs:
    print("Trying")
    job.click()
    time.sleep(5)

    try:

        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        easy_apply.click()

        time.sleep(5)

        number = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        if number.text == "":
            number.send_keys(NUMBER)

        submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("cos")
        continue

time.sleep(5)
driver.quit()
