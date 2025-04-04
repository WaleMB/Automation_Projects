from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
application_path = os.path.dirname(sys.executable)

# get date in format MMDDYYYY
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

web = 'https://news.sky.com/'
path = "C:/Users/walet/Downloads/chromedriver-win64/chromedriver.exe" # introduce path here

# Headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
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
file_name = f'news_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()

#Converting script to Executable
pyinstaller --onefile News Automation.py  #bash script
