from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'eraser'

num = 18
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=&gid=1-103-004'
response = requests.get(stationery)
response
page = BeautifulSoup(response.text, 'html.parser')

parent =  page.find_all('div',{'class':'bc-content-center'})[5]
text = list(parent.descendants)[0]

for n in range(0,num):
    name = text.find_all('li')[n].find('span', 'product-name').text

    link = text.find_all('li')[n].find('a')['href']
    link = web_url + link

    image = text.find_all('li')[n].find('img')['src']
    images = web_url2 + image
    
    price = 'คลิกเพื่อดูราคาผ่านเวปไซต์'

    cur.execute('INSERT INTO shop_manage_erasers(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

web_url = 'https://www.ohwowshop.com/'
num = 3

for i in range(1,num+1):
  stationery = web_url + 'category/3/เครื่องเขียน-ขายส่งราคาสำเพ็ง/ยางลบ?tskp=' + str(i)
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

    cur.execute('INSERT INTO shop_manage_erasers(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

sub = 'correction'

num = 12
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = web_url + 'products.php?bid=&gid=1-103-002'
response = requests.get(stationery)
response
page = BeautifulSoup(response.text, 'html.parser')

parent =  page.find_all('div',{'class':'bc-content-center'})[5]
text = list(parent.descendants)[0]

for n in range(0,num):
    name = text.find_all('li')[n].find('span', 'product-name').text

    link = text.find_all('li')[n].find('a')['href']
    link = web_url + link

    image = text.find_all('li')[n].find('img')['src']
    images = web_url2 + image
    
    price = 'คลิกเพื่อดูราคาผ่านเวปไซต์'

    cur.execute('INSERT INTO shop_manage_erasers(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

web_url = 'https://www.ohwowshop.com/'
num = 1

for i in range(1,num+1):
  stationery = web_url + 'category/65/เครื่องเขียน-ขายส่งราคาสำเพ็ง/เทปลบคำผิด-ลิขวิด?tskp=' + str(i)
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

    cur.execute('INSERT INTO shop_manage_erasers(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()
    
con.close()