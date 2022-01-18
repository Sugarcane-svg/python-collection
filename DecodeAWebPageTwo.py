# using request and BeautifulSoup Python libraries, print to screen the full text of the article on this website.

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url).text


soup = BeautifulSoup(r, 'html.parser')

for i in soup.find_all(class_='body__inner-container'):

    if i.p:
        print(i.p.text.replace('<.+?>', ' '))
