# -*- coding:utf-8 -*-
import urllib
import urllib2
import re #正则
class BSBDJ():
	def rpk(self,a,b,c):
		per = 100 * a * b / c
		if per > 100:
			per = 100
		if per % 25 == 0:
			print "%0.2f%%" % per,

	def getVideo(self,page):
		req = urllib2.Request('http://www.budejie.com/video/%s' %page)  #请求页面
		req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
		html = urllib2.urlopen(req).read()
		reg = r'data-mp4="(.*?)"'  #正则表达式
		for i in re.findall(reg, html):  #找到视频地址,所有视频都是需要的，故好匹配
			filename = i.split("/")[-1]   #视频文件名
			print "正在下载%s" %filename
			urllib.urlretrieve(i, "D:/xz/%s" %filename,self.rpk)  #下载到与py文件同目录下的down_mp4文件夹
			print "\n下载完成\n"
	def start(self,x):
		for i in range(1,x):
			self.getVideo(i)

spider = BSBDJ()
spider.start(20)	#以下载前20页为例

