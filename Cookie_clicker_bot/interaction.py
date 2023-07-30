from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(articles.text)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Łukasz")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Wojczuk")
email = driver.find_element(By.NAME, "email")
email.send_keys("wojczuklukasz@gmail.com")
sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()

driver.quit()
