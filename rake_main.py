import pandas as pd
import requests
import numpy as np
from urlparse import urlparse
import urllib
import urllib3.request
import re
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt

# Open file

with open('history_export.txt') as f:
    content = f.readlines()

# Place data into a more legible format
# Separate the lines by the vertical bar '|'
raw_data = [line.split('|') for line in [x.strip() for x in content]]

data = pd.DataFrame(raw_data, columns=['datetime', 'url'])
data.head(1)

data.datetime = pd.to_datetime(data.datetime)

# urlparse divides the url into 6 or 7 components
# scheme: 'http'
# netlock: 'www.google.com'
# path: '/search'
# params: key value pairs for the query
# query: '?somequerystring'
# fragments: sometimes 'none'

#re.open()

#print(data.url[0])

lines = []
i = 0
string = 'Super Function'
dict = {}
for dat in data.url:
    counter = 0
    #i = 0
    r = requests.get(dat)
    beaut = soup(r.content)
   # if str(dat) == 'https://www.pythonforbeginners.com/super/working-python-super-function':
   #     print(beaut.get_text())
    strings = beaut.get_text()
    counter = strings.count(string) + strings.count(string.lower())
    dict[dat] = 'None'
    dict[dat] = [dict[dat], counter]

    if i == 50:
        break
    i = i + 1
for key,val in dict.items():
    print('{} {} \n'.format(key, val))

'''
    if urllib3.connection_from_url(dat).request:
        lines.append(urllib.urlopen(dat).readlines())
        print(lines)

        
        dict[dat] = 'None'
        for line in lines:
            beaut = soup(str(line), 'lxml')
            for b in beaut.find_all('p'):
              dict[dat] = [dict[dat], b.get_text()]
        i = i + 1
    if i == 5:
        break
for key in dict.keys():
    counter = 0
    #dict.pop(key, val)
    for val in dict[key]:
        if 's' in val:
            counter = counter + 1
    dict[key] = [dict[key], counter]


for key,val in dict.items():
    print("{} = {}".format(key, val))
    print('\n')

'''
'''
parser = lambda u: urlparse(u).netloc(

print(parser)
data.url = data.url.apply(parser)
print(data.url)

data.url = data.url.apply(parser)

site_freq = data.url.value_counts().to_frame()

site_freq.reset_index(level=0, inplace=True)

site_freq.columns = ['domain', 'count']

site_freq.head(2)

topN = 5

plt.figure(1, figsize=(10,10))

plt.title('Top sites')

pie_data = site_freq['count'].head(topN).tolist()

pie_labels = site_freq['domain'].head(topN).tolist()

plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)




plt.show()
'''