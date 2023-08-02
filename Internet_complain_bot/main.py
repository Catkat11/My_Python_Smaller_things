from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 80
PROMISED_UP = 35
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASS"
TWITTER_USERNAME = "USERNAME"


class InternetSpeedTestTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

        self.driver.get("https://www.speedtest.net/")
        self.down = 0
        self.up = 0

    def get_internet_speed(self):

        time.sleep(5)
        accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()

        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            return True
        else:
            return False

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(5)

        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(3)

        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)

        time.sleep(3)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(10)

        tweet = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        tweeting = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet.send_keys(tweeting)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(30)


bot = InternetSpeedTestTwitterBot()
if bot.get_internet_speed():
    bot.tweet_at_provider()
