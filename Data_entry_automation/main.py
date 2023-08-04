from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A34.40378463935821%2C%22east%22%3A-117.9008682421875%2C%22south%22%3A33.63662251280971%2C%22west%22%3A-118.9225967578125%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D",
                        headers=header)

data = response.text
response.raise_for_status()
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".ListItem-c11n-8-84-3__sc-10e22w8-0 a")
all_links = []

for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        if f"https://www.zillow.com{href}" not in all_links:
            all_links.append(f"https://www.zillow.com{href}")
    else:
        if href not in all_links:
            all_links.append(href)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0  a")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 span")
all_prices = [price.get_text().split(" ")[0].split("+")[0].split("/")[0] for price in all_price_elements]


driver = webdriver.Chrome()

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdrF4tr77nv-vMuAf7eOstNktIafNluviTj0M0s1j5fKXzxow/viewform?usp=sf_link")

    time.sleep(3)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(all_addresses[n])

    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(all_prices[n])

    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(all_links[n])

    button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()


