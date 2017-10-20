# coding=utf-8
import urllib
import urllib2
import re
import  thread
import time
"""
（思路：
①class QSBK:初始化变量——获取网站完整代码——获取有用信息——加载和提取（保存）信息——输出信息——开始运行）
pageStories 存储一页的代码

"""
#糗事百科虫类
class QSBK:
    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        #简称UA，用户代理
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1)'
         #初始化headers
        self.headers = {'User-Agent' :self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False

    #传入某一页的索引，获得本页完整代码
    def getPage(self,pageIndex):
        try:
            #str(pageIndex)为数字几即对应糗事百科网站第几页
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url,headers=self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "连接糗事百科失败,错误原因",e.reason
                return None

    #传入某一页的索引，获得本页段子内容
    def getPageItems(self,pageIndex):
        #获取完整代码
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page load error"
            return None
        #正则表达式
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
        #正则表达式匹配所有代码
        items = re.findall(pattern,pageCode)
        #用来存储每页的段子们
        pageStories = []
        #.strip()函数去除字符串前后的空格
        for item in items:
            #item[0]是发布人，item[1]是内容，item[2]是获赞数
            #注意列表的append方法只能加一个列表，故所有项装入一个列表再append
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
            #print len(pageStories)      #1到25
            #print pageStories           #两个[]
        return pageStories              #每个段子构成一个列表，整体再构成一个列表的元素[[],[],[],[],[],[]]——一个页面的所有段子构成的列表

    #判断：如果当前未看的篇数少于2篇，则加载新一页
    def loadPage(self):
        #如果当前未看的篇数少于2篇，则加载新一页
        if self.enable==True:
            if len(self.stories)<1:
                #获取当前页内容
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的所有段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)        #三个[]   [[[],[],[],[],[],[]]]
                    #获取后，页码自动加1
                    self.pageIndex +=1
    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            if input == "Q":
                self.enable = False
                return
            self.loadPage()
            print u"第%d页\t发布人：%s\t 赞：%s\n%s" %(page,story[0],story[2],story[1])

    def start(self):
        print u'正在读取糗事百科，回车查看新段子，Q退出'
        #打开开始标志
        self.enable = True
        #加载（第）一页
        self.loadPage()
        #局部变量，当前页数置0
        nowPage = 0
        #死循环，程序持续运行
        while self.enable:
            if len(self.stories)>0:
                #self.stories就是个中间变量，先取过pageStories的所有列表元素，然后又吐回来
                #print len(self.stories)    长度为1
                pageStories = self.stories[0]           #self.stories[0]又转化为两个[],即[[],[],[],[],[]],这样才能用for提取，这很重要！！！！
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()
