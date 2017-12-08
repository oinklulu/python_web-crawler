# -*- encoding: utf-8 -*-
#爬取某网站模特图片
# Created on 2017-12-4 00:59:45
# Project: model_01
import requests
import urllib
import bs4
from bs4 import BeautifulSoup
import os
import sys
sys.setrecursionlimit(1000000) #递归深度设置成100万
class Handler(object):
	def __init__(self):
		self.base_url = 'http://www.nvshen.ee/thread-'	#10021-1-1.html
		self.page_num = 10021
		# self.deal = Deal()
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1)'
		#初始化headers
		self.headers = {'User-Agent' :self.user_agent}
		self.index = 1
		self.enable = True


	def get_page(self,url):
		try:
			#构建请求
			res = requests.get(url,headers=self.headers)
			print res			#<Response [200]>
			self.enable = True
			print self.page_num
			return res.text
		except:
			print "小姐姐们已经下载完毕hhh"
			self.enable = False


	def get_imgs(self,html):
		soup = BeautifulSoup(html,"html5lib")
		for img in soup.find_all('img',{'class':'zoom'}):
			print ("正在下载{}号小姐姐第{}张图片".format(self.page_num,self.index))
			path = 'http://www.nvshen.ee/'+img.get("data-echo")
			urllib.urlretrieve(path,r'D:\pic\{}\{}.jpg'.format(self.page_num,self.index))
			self.index += 1

	def download(self):
		urls = self.base_url + str(self.page_num)+'-1-1.html'
		h1 = self.get_page(urls)
		self.local_path = r'D:\pic\{}'.format(self.page_num)
		if not os.path.exists(self.local_path):
			os.makedirs(self.local_path)
		self.get_imgs(h1)
		self.page_num -= 1
		self.index = 1

	def run(self):
		while(self.enable):
			self.download()

hd = Handler()
hd.run()

