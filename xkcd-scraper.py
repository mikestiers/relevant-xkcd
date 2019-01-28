import requests, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

xkcdUrl = 'http://xkcd.com'
xkcdPage = urlopen(xkcdUrl)


soup = BeautifulSoup(xkcdPage)
