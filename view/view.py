# coding=utf-8

import pycurl
import urllib
from StringIO import StringIO
import json
import re
import certifi  #①  没有这个则出现pycurl.error: (60, 'SSL certificate problem: unable to get local issuer certificate')


# class definition

class shua_view_class:


    def __init__(self,link):
        self.website = unicode(link)
        self.configure()

    def shouye(self):
        buffer = StringIO()
        self.c.setopt(pycurl.URL, self.website)
        self.c.setopt(pycurl.CAINFO, certifi.where())   #②
        #没有②这个则出现pycurl.error: (60, 'SSL certificate problem: unable to get local issuer certificate')
        self.c.setopt(pycurl.POST, 0)
        self.c.setopt(self.c.WRITEDATA, buffer)
        self.c.perform()
        body = buffer.getvalue().decode('utf-8')
        self.uuid = re.search(r"uuid\":\"(.+)\"}", body).group(1)
        view_count = re.search(r"views_count\":(\d+)", body).group(1)
        #print self.uuid
        print "view:" + str(view_count)

    def configure(self):
        self.c = pycurl.Curl()
        USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.c.setopt(pycurl.HTTPHEADER, ['Origin: http://www.jianshu.com', 'Referer: '+self.website])    # this line is very important to if we can succeed!
        self.c.setopt(self.c.FOLLOWLOCATION, 1)
        self.c.setopt(pycurl.VERBOSE, 0)
        self.c.setopt(pycurl.FAILONERROR, True)
        self.c.setopt(pycurl.USERAGENT, USER_AGENT)

    def shuaview(self):
        data_form = {
            'uuid': self.uuid,
        }

        # print data_form

        buffer = StringIO()
        data_post = urllib.urlencode(data_form)
        url = self.website.replace("/p/","/notes/") + '/mark_viewed.json'
        #print url
        self.c.setopt(pycurl.URL, url)
        self.c.setopt(pycurl.POST, 1)
        self.c.setopt(pycurl.POSTFIELDS, data_post)
        self.c.setopt(self.c.WRITEFUNCTION, buffer.write)
        self.c.perform()

        response = buffer.getvalue()
        response_json = json.loads(response)


    def exit(self):
        self.c.close()


# main function

Post_link="https://www.jianshu.com/p/fca53c2d23c8"
n = 0
app=shua_view_class(Post_link)
app.shouye()  # check the view number before we shua view
while True:
    app.shuaview()
    n += 1

    if n > 100:  # add 101 more views
        break

app.shouye() # check the view number after we shua view
app.exit()