# coding=utf-8
import requests
import bs4
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/cinema/later/hangzhou/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
for item in soup.find_all(class_="intro"):
    print "《",item.select("h3")[0].text.strip(),"》",\
        item.select("li")[0].text.strip(),\
        item.select("li")[1].text.strip()




