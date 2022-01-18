import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url).text


soup = BeautifulSoup(r, 'html.parser')

filename = input('enter a file name: ')

for i in soup.find_all(class_='body__inner-container'):

    if i.p:
        with open(filename, 'w') as open_file:
            open_file.write(i.p.text.replace('<.+?>', ' '))

