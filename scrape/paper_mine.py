from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'paper'

for i in range(1,3):
  pen ='https://www.stationerymine.com/art-supplies/sketch-book-and-paper?p=' +str(i) + '&product_list_limit=48'
  response = requests.get(pen)
  page = BeautifulSoup(response.text, 'html.parser')
  pen = page.find_all('div','product-item-info')

  for k in pen:
    images = k.find('img')['data-src']

    link = k.find('a','product-item-link')['href']

    name = k.find('a','product-item-link').get_text(strip = True)

    price = k.find('span','price-wrapper').find('span','price').get_text(strip = True)
    price = price.replace(',','')
  

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()
    
con.close()