from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'color'

num = 2
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=&gid=1-101-001'
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

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

num = 5
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=&gid=1-106-004'
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

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

num = 10
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=&gid=1-106-005'
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

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()
num = 3
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=1&gid=1-106-002'
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

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()  

num = 12
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=&gid=1-101-002'
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

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()  

num = 7
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=&gid=1-101-004'
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

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()

num = 7
web_url = 'https://www.sakura.in.th/th/'
web_url2 = 'https://www.sakura.in.th/'

stationery = 'https://www.sakura.in.th/th/products.php?bid=&gid=1-101-005'
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

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[images,name,price,link,sub])

    con.commit()
    
con.close()
