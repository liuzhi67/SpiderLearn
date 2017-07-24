#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import cookielib
import re

cookie=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
resp=opener.open('http://book.douban.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value


connection=r'keep-alive'
agent=r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

headers={'User-Agent':agent, 'Connection':connection}
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
opener.addheaders.append(headers)

#douban uid
uid=r'58508448'
#req=opener.open('https://book.douban.com/people/' + uid + '/collect/')

#get first page's data
resp=opener.open('https://book.douban.com/people/%s/collect?start=0&sort=time&rating=all&filter=all&mode=grid'%(uid))

content=resp.read()

urlpattern=re.compile(r'https://book\.douban\.com/people/%s/collect\?start=[\d]+.*mode=grid'%(uid))

urls=urlpattern.findall(content)

for item in urls:
    print item

urlDic=dict()
for url in urls:
    if urlDic.has_key(url):
        pass
    else:
        urlDic[url]=1
        print urlDic
        pageNo=re.findall(r'start=(?P<pageNo>[\d]+)&', url)
        if len(pageNo)>=1:
            pageFile='booklist_%s.html'%(pageNo[0])
            print pageFile
            resp=opener.open(url)
            with open(pageFile,'w') as outfile:
                outfile.writelines(resp.read())

'''
req=opener.open('https://book.douban.com/people/' + uid + '/collect?start=0&sort=time&rating=all&filter=all&mode=grid')
#print req.read()

outfile=open('book.html', 'w')
outfile.writelines(req.read())
'''

#res=urllib2.urlopen('https://book.douban.com/people/' + uid)
#print res.read()

