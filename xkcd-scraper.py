import requests, os, time, sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen

conn = sqlite3.connect('comics.db')
c = conn.cursor()
#c.execute('''CREATE TABLE comics (number text, url text)''')



xkcdUrl = 'http://xkcd.com/'
xkcdPage = urlopen(xkcdUrl)
soup = BeautifulSoup(xkcdPage, 'html.parser')
previousComic = ((soup.find("a", {"rel":"prev"})).attrs['href']).strip('/')
currentCommic = int(previousComic) + 1

count = currentCommic
while (count > 0):
    xkcdUrl = 'http://xkcd.com/'+str(count)
    xkcdPage = urlopen(xkcdUrl)
    count -= 1
    soup = BeautifulSoup(xkcdPage, 'html.parser')
    comicElement = soup.find("div", {"id": "comic" })
    comicImage = 'http:' + comicElement.find('img').attrs['src']
    print(comicImage)
    c.execute("INSERT INTO comics VALUES (?, ?);", (count, comicImage))
    conn.commit()
    if (count % 5 == 0):
        time.sleep(10)

conn.close()

print()
