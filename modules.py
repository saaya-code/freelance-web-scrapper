import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
base_url = "https://www.rockauto.com/"

def get_years(carModel):
    url = "https://www.rockauto.com/en/catalog/"+carModel
    driver_path = 'C:/Users/boual/Downloads/chromedriver.exe'  # Update with your actual path to chromedriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # Open the webpage
    driver.get(url)

    # Allow some time for JavaScript to execute (adjust the sleep time as needed)
    import time
    time.sleep(5)

    # Get the page source and close the driver
    page_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_content, 'html.parser')

    res = soup.find_all('a', class_="navlabellink nvoffset nnormal")

    allDataInside = [x.text for x in res]

    years = filter(lambda x: x.isdigit(),allDataInside)
    return list(years)



def get_cars_models():
    response = requests.get(base_url)
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')
    tds = soup.find_all('a', class_="navlabellink")
    list_of_all_cars = [x.text for x in tds]
    return list_of_all_cars



def getPartNumbers(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    partnumbers = soup.find_all('span', class_="listing-final-partnumber")
    allDataInside = [x.text for x in partnumbers]
    return allDataInside

def getManufacturers(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    manufacturers = soup.find_all('span', class_="listing-final-manufacturer")
    allDataInside = [x.text for x in manufacturers]
    return allDataInside