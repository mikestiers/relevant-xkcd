import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

count = 1
while (count < 15):
    xkcdUrl = 'http://xkcd.com/'+str(count)
    xkcdPage = urlopen(xkcdUrl)
    count += 1
    soup = BeautifulSoup(xkcdPage, 'html.parser')
    comicElement = soup.find("div", {"id": "comic" })
    #print(comicElement)
    comicImage = 'http:' + comicElement.find('img').attrs['src']
    print(comicImage)


#images = soup.findAll('img')
print()