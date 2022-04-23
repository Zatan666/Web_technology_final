from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'color'

web_url = 'https://shubaothai.com/'
stationery = 'https://shubaothai.com/th/products/category/88462-%E0%B8%AB%E0%B8%A1%E0%B8%B6%E0%B8%81%E0%B8%88%E0%B8%B5%E0%B8%99%20%E5%A2%A8%E6%B1%81'
response = requests.get(stationery)
response
page = BeautifulSoup(response.text, 'html.parser')

catalogue = page.find_all('div','caption')
#names = [] ;prices =[] ;links = []

catalogue2 = page.find_all('a','item-image')
#images = []

for container ,container2 in zip(catalogue,catalogue2):
    name = container.find('a').text
  
    price = container.find('div',{'class':'discount-price'}).text
    price = price.replace(" ","")
    price = 'B ' + price[1:-4]

    link = container.find('a')['href']
    link = web_url + link

    image = container2.find('img')['src']

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

    con.commit()
####

web_url = 'https://shubaothai.com/'
stationery = 'https://shubaothai.com/th/products/category/88924-%E0%B8%AB%E0%B8%A1%E0%B8%B6%E0%B8%81%E0%B8%97%E0%B8%AD%E0%B8%87%20%E9%87%91%E5%A2%A8'
response = requests.get(stationery)
page = BeautifulSoup(response.text, 'html.parser')

catalogue = page.find_all('div','caption')
#names = [] ;prices =[] ;links = []

catalogue2 = page.find_all('a','item-image')
#images = []

for container ,container2 in zip(catalogue,catalogue2):
    name = container.find('a').text
    
    price = container.find('div',{'class':'discount-price'}).text
    price = price.replace(" ","")
    price = 'B ' + price[1:-4]

    link = container.find('a')['href']
    link = web_url + link

    image = container2.find('img')['src']

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

    con.commit() 
######
web_url = 'https://shubaothai.com/'
stationery = 'https://shubaothai.com/th/products/category/88949-%E0%B8%AA%E0%B8%B5%E0%B8%A7%E0%B8%B2%E0%B8%94%E0%B8%A0%E0%B8%B2%E0%B8%9E%20%E9%A2%9C%E6%96%99'
response = requests.get(stationery)
page = BeautifulSoup(response.text, 'html.parser')

catalogue = page.find_all('div','caption')
#names = [] ;prices =[] ;links = []

catalogue2 = page.find_all('a','item-image')
#images = []

for container ,container2 in zip(catalogue,catalogue2):
    name = container.find('a').text

    price = container.find('div',{'class':'discount-price'}).text
    price = price.replace(" ","")
    price = 'B ' + price[1:-4]

    link = container.find('a')['href']
    link = web_url + link


    image = container2.find('img')['src']

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

    con.commit() 

####
web_url = 'https://shubaothai.com/'
stationery = 'https://shubaothai.com/th/products/category/88922-%E0%B8%AB%E0%B8%A1%E0%B8%B6%E0%B8%81%E0%B9%81%E0%B8%94%E0%B8%87%E0%B8%88%E0%B8%B9%E0%B8%8B%E0%B8%B2%20%E6%9C%B1%E7%A0%82'
response = requests.get(stationery)

page = BeautifulSoup(response.text, 'html.parser')

catalogue = page.find_all('div','caption')
#names = [] ;prices =[] ;links = []

catalogue2 = page.find_all('a','item-image')
#images = []

for container ,container2 in zip(catalogue,catalogue2):

    name = container.find('a').text

    price = container.find('div',{'class':'discount-price'}).text
    price = price.replace(" ","")
    price = 'B ' + price[1:-4]

    link = container.find('a')['href']
    link = web_url + link

    image = container2.find('img')['src']

    cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
    'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

    con.commit() 
web_url = 'https://natpopshop.com/'
stationery = 'https://natpopshop.com/product/collection/13/'
response = requests.get(stationery)
response
page = BeautifulSoup(response.text, 'html.parser')

catalogue = page.find_all('h3','product-title')
#names = [] ;links = []

catalogue2 = page.find_all('div','product-thumb')
#images = []

catalogue3 = page.find_all('div','product-price')
#prices = []

for container ,container2, container3 in zip(catalogue,catalogue2, catalogue3):
        name = container.find('a').text

        link = container.find('a')['href']
        link = web_url + link

        image = container2.find('img')['src']

        price = container3.find('ins').text
        price = 'B ' + price[:-4]

        cur.execute('INSERT INTO shop_manage_arts(image,name,price,link,sub)'
        'VALUES (?,?,?,?,?)',[image,name,price,link,sub])

        con.commit() 

con.close()