from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

USER_EMAIL = "EMAIL"
USER_PASSWORD = "PASS"
ACCOUNT = "_rl9"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/login/")


    def login(self):
        time.sleep(5)

        cookies = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookies.click()

        time.sleep(3)

        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys(USER_EMAIL)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(USER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(5)

        notifications = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notifications.click()


    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}")

        time.sleep(5)

        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)

    def follow(self):
        for num in range(1, 100):
            time.sleep(3)
            follow_button = self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{num}]/div/div/div/div[3]/div/button')
            if follow_button.text == "Obserwuj":
                follow_button.click()
            else:
                pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
