#!/usr/bin/python
#coding=utf-8
import urllib
import re
import threading
import copy

FinishCount = 0
    
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
   # html=html.decode("GB2312")
    print html
    return html

def downThread(url,index,total):
    urllib.urlretrieve(url,'%d.jpg' % index)
    global FinishCount
    FinishCount+=1
    print "download image %d finished,%d/%d" %(index,FinishCount,total)


def getimg(html):
    reg = r'"objURL":"(.+?\.jpg)",'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print "get image cout %d"%len(imglist)
    x = 1
    threads = []
    for imgurl in imglist:
        t = threading.Thread(target=downThread,args=(imgurl,x,len(imglist),))
        #downThread(imgurl,x,len(imglist))
        x += 1
        threads.append(t)

    for ti in threads:
        ti.setDaemon(True)
        ti.start()

    for ti in threads:
        ti.join()

html = getHtml("https://image.baidu.com/search/index?ct=&z=&tn=baiduimage&ipn=r&word=%E5%9B%BE%E7%89%87%E7%BE%8E%E5%A5%B3%E6%B8%85%E7%BA%AF%E5%A3%81%E7%BA%B8&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=&lm=-1&st=-1&fr=&fmq=1492890654482_R&ic=0&se=&sme=&width=1920&height=1080&face=0")
print getimg(html)
print 'Finished Downlaod all picture!'
