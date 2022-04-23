from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sub = 'brush'

web_url ='https://shubaothai.com'
stationery = 'https://shubaothai.com/th/products/category/88460-%E0%B8%9E%E0%B8%B9%E0%B9%88%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%88%E0%B8%B5%E0%B8%99%20%E6%AF%9B%E7%AC%94'
response = requests.get(stationery)
response
page = BeautifulSoup(response.text, 'html.parser')

catalogue = page.find_all('div','caption')

catalogue2 = page.find_all('a','item-image')

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

con.close()
