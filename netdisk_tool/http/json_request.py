#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json

def json_request(url,js):
    print 'request url=%s,post_data=%s'%(url,js)
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'kingsoft-ecloud-pc;Pytool-{00-0C-29-D3-97-1B};1.0.0.1')
    req.add_header('Content-Type','application/json')
    req.add_header('kp-p','1')
    req.add_header('kp-os','1')
    req.add_header('v','4')
    req.add_header('Accept', '*/*')
    req.add_header('Referer', url)
    req.add_header('POST', url)
    req.add_data(js)
    page = urllib2.urlopen(req) #将request对象传入urlopen方法，返回一个response对象
    recv = page.read()
    print 'request url=%s,return data=%s'%(url,recv)
    return recv
