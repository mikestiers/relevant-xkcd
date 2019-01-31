import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

xkcdUrl = 'http://xkcd.com'
xkcdPage = urlopen(xkcdUrl)


soup = BeautifulSoup(xkcdPage, 'html.parser')
comicElement = soup.find("div", {"id": "comic" })
print(comicElement)
comicImage = 'http:' + comicElement.find('img').attrs['src']


#images = soup.findAll('img')
print()