from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'sticker'

web_url = 'https://www.ohwowshop.com/'
num = 3

for i in range(1,num+1):
  stationery = web_url + 'category/29/สติ๊กเกอร์ลายการ์ตูนสติ๊กเกอร์หัวใจดาวและอื่นๆ-2?tskp=' + str(i)
  response = requests.get(stationery)
  response
  page = BeautifulSoup(response.text, 'html.parser')

  catalogue = page.find_all('div',{'productArea'})
  catalogue = catalogue[:-22]
  #names = [] ;prices =[] ;links = [] ;images = []

  for container in catalogue :
    name = container.find('img')['alt']

    price = container.find('div',{'class':'product_price has_currency_unit'}).text[:-4]
    price = 'B ' + price
  
    link = container.find('a')['href']
  
    images = container.find('img')['data-src']

    cur.execute('INSERT INTO shop_manage_diys(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

web_url = 'https://thaigoodprice.fun/'
num = 10

for i in range(1,num+1):
  stationery = 'https://thaigoodprice.fun/cat/%E0%B8%AA%E0%B8%95%E0%B8%B4%E0%B9%8A%E0%B8%81%E0%B9%80%E0%B8%81%E0%B8%AD%E0%B8%A3%E0%B9%8C-cat.1315.1333.17540?page=' + str(i)
  response = requests.get(stationery)
  page = BeautifulSoup(response.text, 'html.parser')

  catalogue = page.find_all('div',{'class':'col-xl-3 col-lg-3 col-md-4 col-sm-6 col-12 '})
  catalogue = catalogue[1:]
  #names = [] ;prices =[] ;links = [] ;images = []

  for container in catalogue :
    name = container.find('img')['alt']

    price = container.find('p').find('del').text
    price = 'B ' + price[1:]
  
    link = container.find('a')['href']
    link = web_url + link
  
    images = container.find('img')['src']

    cur.execute('INSERT INTO shop_manage_diys(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

con.close()