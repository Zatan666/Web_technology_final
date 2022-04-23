from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'eraser'

stationery = 'https://www.stationerymine.com/stationery/eraser-and-correction-product?new_stationary_type=1839'
response = requests.get(stationery)
page = BeautifulSoup(response.text, 'html.parser')
staionery = page.find_all('div','product-item-info')

for k in staionery:

    image = k.find('img')['data-src']

    link = k.find('a','product-item-link')['href']

    name = k.find('a','product-item-link').get_text(strip = True)
    name = name.replace(',','')
    name.replace(',','')
    
    price = k.find('span','price-wrapper').find('span','price').get_text(strip = True)
    price = price.replace(',','')
 
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('INSERT INTO shop_manage_erasers(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

    con.commit()

sub = 'correction'

stationery = 'https://www.stationerymine.com/stationery/eraser-and-correction-product?new_stationary_type=1818&product_list_limit=48'
response = requests.get(stationery)
page = BeautifulSoup(response.text, 'html.parser')
staionery = page.find_all('div','product-item-info')

for k in staionery:

    image = k.find('img')['data-src']

    link = k.find('a','product-item-link')['href']

    name = k.find('a','product-item-link').get_text(strip = True)
    name = name.replace(',','')
    name.replace(',','')
    
    price = k.find('span','price-wrapper').find('span','price').get_text(strip = True)
    price = price.replace(',','')

    cur.execute('INSERT INTO shop_manage_erasers(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

    con.commit()

con.close()