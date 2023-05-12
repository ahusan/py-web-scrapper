import requests
import os
from bs4 import BeautifulSoup
import csv
from dotenv import load_dotenv

load_dotenv()




# Settign variables from env file
rangefrom = int(os.getenv('RANGE_FROM'))
rangeto = int(os.getenv('RANGE_TO'))
url = os.getenv('SCRAPE_URL')
tag = os.getenv('SCRAPE_TAG')
date_tag = os.getenv('SCRAPE_DATE_TAG')
class_name = os.getenv('SCRAPE_CLASS')
date_class = os.getenv('SCRAPE_DATE_CLASS')
#File to save the headings
filename = 'titles.csv'

#Setting up a CSV file to save the article Headings
with open(filename, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['Page', 'Date', 'Title']
    w = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|', dialect='excel')
    w.writeheader()
    
    #Looping through the first 200 articles
    for page in range(rangefrom, rangeto):
        req = requests.get(url + str(page) + '/')
        soup = BeautifulSoup(req.content, 'html.parser')

        title = soup.find(tag, class_=class_name);
        date = soup.find(date_tag, class_=date_class);
        #Checking if an article exist
        if(title):
            print(page, date.text, title.text)
            w.writerow({'Page':page, 'Date': date.text, 'Title':title.text})
        else:
            print(page, 'Article does not exist')
        
        


        