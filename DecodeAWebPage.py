# use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the [New York Times](https://www.nytimes.com/)

import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)

r_html = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(r_html)
title = soup.find_all(class_="css-4m8aqz e1lsht870")
print([i.text for i in title])