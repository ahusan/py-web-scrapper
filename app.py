import requests
from bs4 import BeautifulSoup
import csv

# Making a GET request
url = 'https://mihaaru.com/news/'

# Parsing the HTML

# s = soup.find('div', class_='entry-content')

# lines = s.find_all('p')
filename = 'titles.csv'


with open(filename, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['Page', 'Title']
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for page in range(10001, 10200):
        req = requests.get(url + str(page) + '/')
        soup = BeautifulSoup(req.content, 'html.parser')

        title = soup.find('h1', class_='text-waheed')
        if(title):
            d = {}
            print(page, title.text)
            w.writerow({'Page':page, 'Title':title.text})
        else:
            print('Article does not exist')
        
        


        