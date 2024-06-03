import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service("C:/ML/My_Projects/Webscrapper/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Function to extract car details
def extract_car_details(card):
    car_name = card.find_element(By.CSS_SELECTOR, 'h3').text
    details = card.find_element(By.CSS_SELECTOR, 'div.d-flex.flex-column').text.split('\n')
    year, driven_kms, car_type, transmission = details[:4]
    price = card.find_element(By.CSS_SELECTOR, 'div.price').text
    location = card.find_element(By.CSS_SELECTOR, 'div.cityName').text
    return {
        'car_name': car_name,
        'year': year,
        'driven_kms': driven_kms,
        'type': car_type,
        'transmission': transmission,
        'price': price,
        'location': location
    }

# Initialize WebDriver

driver.get("https://www.carwale.com/used/cars-in-chennai/")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
time.sleep(5)
driver.find_elements(By.CSS_SELECTOR, '#cityPopUp > div > div:nth-child(2) > section > div > ul > li:nth-child(4) > a')
time.sleep(5)



'''
try:
    # Infinite scroll simulation
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait to load the page
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract car details
    car_cards = driver.find_elements(By.CSS_SELECTOR, 'div.cardetail')
    car_data = [extract_car_details(card) for card in car_cards]

    # Close the WebDriver
    driver.quit()

    # Convert data to DataFrame
    df = pd.DataFrame(car_data)

    # Save to CSV
    df.to_csv('used_cars_chennai.csv', index=False)

    print("Data has been successfully scraped and saved to 'used_cars_chennai.csv'")

except Exception as e:
    print("error in webscrapper code",e)
'''