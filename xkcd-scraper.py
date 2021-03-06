import requests, os, time, sqlite3
from azure.storage.blob import BlockBlobService, PublicAccess
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve

conn = sqlite3.connect('comics.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS comics (number TEXT UNIQUE, url text)''')

c.execute("SELECT number FROM comics ORDER BY number DESC LIMIT 1")
lastLoggedComic = c.fetchall()


xkcdUrl = 'http://xkcd.com/'
xkcdPage = urlopen(xkcdUrl)
soup = BeautifulSoup(xkcdPage, 'html.parser')
previousComic = ((soup.find("a", {"rel":"prev"})).attrs['href']).strip('/')
currentCommic = int(previousComic) + 1

if (currentCommic >= (int(lastLoggedComic[0][0]))):
    count = currentCommic
    while (count > lastLoggedComic):
        xkcdUrl = 'http://xkcd.com/'+str(count)
        xkcdPage = urlopen(xkcdUrl)
        count -= 1
        soup = BeautifulSoup(xkcdPage, 'html.parser')
        comicElement = soup.find("div", {"id": "comic" })
        comicImage = 'http:' + comicElement.find('img').attrs['src']
        print(comicImage)
        urlretrieve(currentCommic, currentCommic)
        c.execute("INSERT OR IGNORE INTO comics VALUES (?, ?);", (count, comicImage))
        conn.commit()
        #if (count % 5 == 0):
            #time.sleep(10)

conn.close()

print()
