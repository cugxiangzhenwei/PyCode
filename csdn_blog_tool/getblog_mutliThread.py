#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a module to get blog html contents'
import urllib2
import re
import random
import os
import threading

#Get indicated url content html,return string type content
def gethtml(url):
    user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ]
    agent = random.choice(user_agents) #每次随机抽取一个伪装的客户端浏览器版本号
    req = urllib2.Request(url) #将要请求的地址映射成request对象，然后可以对其添加HTTP头
    req.add_header('User-Agent', agent)
    req.add_header('Host', 'blog.csdn.net')
    req.add_header('Accept', '*/*')
    req.add_header('Referer', url)
    req.add_header('GET', url)
    page = urllib2.urlopen(req) #将request对象传入urlopen方法，返回一个response对象
    html = page.read()
#    print html
    return html


#gethtml("http://blog.csdn.net/gaoxingnengjisuan?viewmode=contents")

def get_bloglist(url):
    reg = r'<span class="link_title"><a href="(.+?)"'
    urlreg = re.compile(reg)
    html = gethtml(url)
    bloglist = re.findall(urlreg,html)
    print "get blog count :%d" % len(bloglist)
    return bloglist


#get_bloglist("http://blog.csdn.net/gaoxingnengjisuan?viewmode=contents")

def download_blog(url,outdir):
    print 'download from url:%s' % url
    html = gethtml(url)
    p = url.rfind('/') +1
    name = outdir + '/' + url[p:] + '.html'
    print 'save to file %s' % name
    f = open(name,'w')
    f.write(html)
    f.close()

def download_all(mainurl,outdir):
    print 'Begin to download blog from:%s' % mainurl
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    bloglist = get_bloglist(mainurl)
    if len(bloglist) == 0:
        print 'get 0 blog,search break!'
        return 0

    threads = []
    for u in bloglist:
        full_url = "http://blog.csdn.net" + u
        t  = threading.Thread(target=download_blog,args=(full_url,outdir,))
        threads.append(t)
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()
    print 'download blog finished ,count is %d' % len(bloglist)
    return len(bloglist)

#入口函数，自动探测直到获取不到内容为止
def auto_search_download_all(url_main,outdir):
    sum = 0
    pageIndex = 1
    while 1:
        url = url_main + str(pageIndex)
        count  = download_all(url,outdir)
        pageIndex  = pageIndex + 1
        sum += count
        if count <20:
            break
    print "finished task, get blog count is %d" % sum

if __name__=='__main__':
    auto_search_download_all('http://blog.csdn.net/gaoxingnengjisuan/article/list/','./blog/')
