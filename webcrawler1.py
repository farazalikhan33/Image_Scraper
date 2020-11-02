from bs4 import BeautifulSoup
import urllib.request
import requests

source = requests.get('https://www.creativeshrimp.com/top-30-artworks-of-beeple.html').text
soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

for block in soup.find_all('div', class_='wp-caption alignnone'):
    image_link = block.a.get('href')
    title = block.p.text
    urllib.request.urlretrieve(image_link, title+'.jpg')
    print(title, image_link)
    print()
