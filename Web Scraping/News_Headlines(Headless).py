from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

web = 'https://news.sky.com/'
path = "C:/Users/walet/Downloads/chromedriver-win64/chromedriver.exe" # introduce path here

# add headless mode
options = Options()
options.headless = True
driver_service = webdriver.ChromeService(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

containers = driver.find_elements(by='xpath', value='//div[@class="ui-story-content"]')

headlines = []
links = []
for container in containers:
    headline = container.find_element(by='xpath', value='./a').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    headlines.append(headline)
    links.append(link)

# Exporting data to the same folder where the executable will be located
my_dict = {'headline': headlines, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('Headlines-headless.csv')

driver.quit()
