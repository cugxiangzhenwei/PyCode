#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json

def get_request(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'kingsoft-ecloud-pc;Pytool-{00-0C-29-D3-97-1B};1.0.0.1')
    req.add_header('Accept', '*/*')
    req.add_header('Referer', url)
    req.add_header('GET', url)
    page = urllib2.urlopen(req) #将request对象传入urlopen方法，返回一个response对象
    html = page.read()
    print 'get from url=%s,return data=%s'%(url,html)


def get_platform():
    url = 'http://pan.ksyun.com/platform/config'
    return get_request(url)


if __name__ == '__main__':
    get_platform()
