import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

base_url = "https://www.rockauto.com/en/catalog/acura,2015,mdx,3.5l+v6,3307727,electrical,alternator+/+generator,2412"
driver_path = 'C:/Users/boual/Downloads/chromedriver.exe'

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get(base_url)

# Allow some time for JavaScript to execute (adjust the sleep time as needed)
import time
time.sleep(5)

# Get the page source and close the driver
page_content = driver.page_source
driver.quit()



def get_prices(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    prices = soup.find_all('span', class_="listing-amount-bold")
    allDataInside = [x.text for x in prices]
    return allDataInside

print(get_prices(page_content))