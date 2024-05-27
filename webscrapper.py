from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time 

s = Service("C:/ML/My_Projects/Webscrapper/chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s,options=options)

driver.get("https://www.cardekho.com/used-cars+in+chennai")
time.sleep(5)

height = driver.execute_script("return document.body.scrollHeight")
print(height)

#driver.execute_script("windows.scrollTo(0,return document.body.scrollHeight)")