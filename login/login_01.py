# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import re
class QSBKImitateLogin():

	def __init__(self):
		self.loginUrl =  'https://accounts.douban.com/login'
		self.data = {
		'redir' : 'https://www.douban.com/gallery/topic/1915/?from_reason=%E6%96%B0%E8%AF%9D%E9%A2%98&from=gallery_rec_topic',
		'form_email':'15755378450',
		'form_password':'aini8023520',
		'login':u'登录'
		}
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

	def getPage(self):

		r = requests.post(self.loginUrl, data = self.data, headers=self.headers)
		page = r.text
		return page

	def idCode(self,page1):
		#利用bs4获得验证码图片地址
		soup = BeautifulSoup(page1,"html.parser")
		captcha_url = soup.find('img',id='captcha_image')['src']
		#利用正则获得验证码ID
		pattern = re.compile('<input type="hidden" name="captcha-id" value="(.*?)"/')
		captcha_id = re.findall(pattern, page1)
		#将验证码图片保存到本地
		urllib.urlretrieve(captcha_url,"captcha.jpg")
		captcha = raw_input('please input the captcha:')
		self.data['captcha-solution'] = captcha
		self.data['captcha-id'] = captcha_id



	def Imatate(self):
		realPage = self.getPage()
		m = self.idCode(realPage)
		r = requests.post(self.loginUrl, self.data, headers=self.headers)
		page = r.text
		if u"妖铃铃" in page:
			print "登陆成功"
		else:
			print "登陆失败"
# r = requests.post(url, data=data, headers=headers)
#
# page = r.text
if __name__ == '__main__':
	spider = QSBKImitateLogin()
	spider.Imatate()


