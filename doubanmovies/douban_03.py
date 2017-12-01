# coding=utf-8
#豆瓣即将上映电影列表下载
import requests
from lxml import etree
url = 'https://movie.douban.com/cinema/later/hangzhou/'
res = requests.get(url)

# from lxml import etree
# html = etree.parse('1.html')
# dom = etree.tostring(html,pretty_print=True) #解析html并建立dom
# print dom
#以上为etree读取文件的方法（使用etree.parse)

html = etree.HTML(res.text)
		#相当于soup = BeautifulSoup(res.text,'lxml'),不过html为ElementTree格式
		#.text是现成的字符串，.content还要编码(.content.decode('utf-8'))，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码。
		#result = etree.tostring(html,pretty_print=True)
Mname1 = []
Mtime1 = []
Mtype1 = []
Mcountry1 = []

for Mname in html.xpath("/html/body//div[@class='intro']/h3//a"):
		#html.xpath()格式为list
	# print(etree.tostring(i).decode('utf-8'))
	Mname1.append(Mname)

for Mtime in html.xpath("/html/body//div[@class='intro']/ul//li[1]"): #li[1]代表第一个li元素
	Mtime1.append(Mtime)

for Mtype in html.xpath("/html/body//div[@class='intro']/ul//li[2]"):
	Mtype1.append(Mtype)

for Mcountry in html.xpath("/html/body//div[@class='intro']/ul//li[3]"):
	Mcountry1.append(Mcountry)

for i in range(len(Mname1)):
	print '《',Mname1[i].text,'》',\
	Mtime1[i].text,\
	Mtype1[i].text,\
	Mcountry1[i].text


