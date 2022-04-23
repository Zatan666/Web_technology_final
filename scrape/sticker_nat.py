from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'sticker'

stationery = 'https://natpopshop.com/product/collection/3/'
response = requests.get(stationery)
response
page = BeautifulSoup(response.text, 'html.parser')

catalogue = page.find_all('h3','product-title')
#names = [] #links = []

catalogue2 = page.find_all('div','product-thumb')
#images = []

catalogue3 = page.find_all('div','product-price')
#prices = []
web_url = 'https://natpopshop.com'

for container ,container2, container3 in zip(catalogue,catalogue2, catalogue3):
    name = container.find('a').text

    link = container.find('a')['href']
    link = web_url + link

    image = container2.find('img')['src']

    price = container3.find('ins').text
    price = 'B ' + price[:-4]

    cur.execute('INSERT INTO shop_manage_diys(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

    con.commit()

con.close()