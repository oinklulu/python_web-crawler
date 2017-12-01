# -*- coding: utf-8 -*-
import urllib2
from HTMLParser import HTMLParser

class MovieParser(HTMLParser):  #涉及到继承，所以用class
    def __init__(self):
        HTMLParser.__init__(self)
        #在Python中子类继承父类的过程中，如果子类不覆盖父类的__init__()方法，则子类默认将执行与父类一样的初始化方法。
        #但是假如子类自己重写了(也成为覆盖)父类的__init__()方法，
        # 那么就需要显式的调用父类的初始化方法了。有两种方法可以做到:
        #1:HTMLParser.__init__()，父类名加上init函数
        #2:super(MovieParser,self).__init__() （可以简写为super()）
        self.movies = []

    def handle_starttag(self, tag, attrs):  #重写此方法（处理html的开始标签）
        def _attr(attrlist,attrname):
            for attr in attrlist:                 #for (variable, value) in attrs:
                if attr[0] == attrname:
                    return attr[1]
            return None                 #作为一个函数或者类方法，没有返回值就返回None

        if tag == 'li' and _attr(attrs,'data-title') and _attr(attrs,'data-category') == 'nowplaying':
            movie = {}
            movie['title'] = _attr(attrs,'data-title')
            movie['score'] = _attr(attrs,'data-score')
            movie['director'] = _attr(attrs,'data-director')
            movie['actors'] = _attr(attrs,'data-actors')
            self.movies.append(movie)
            print('%(title)s|%(score)s|%(director)s|%(actors)s' % movie)



def nowplaying_movies(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400'}
    req = urllib2.Request(url,headers=headers)
    s = urllib2.urlopen(req)
    parser = MovieParser()      #实例化
    parser.feed(s.read())       #向解析器喂数据，分段提供
    s.close()
    return parser.movies

if __name__ == '__main__':
    url = 'http://movie.douban.com/nowplaying/hangzhou/'
    movies = nowplaying_movies(url)

    import json
    print('%s' % json.dumps(movies,sort_keys=True,indent=4,separators=(',',':')))
