#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
from block_info import *
def http_download(header,url,save_path):
    print 'bengin to dwonload from url:%s'%url
    req = urllib2.Request(url)
    for i in header:
        req.add_header(i,header[i])
    req.add_header('GET', url)
    u = urllib2.urlopen(req) #将request对象传入urlopen方法，返回一个response对象
    f = open(save_path,'wb')
    if not f:
        print 'failed to open path %s'%(save_path)
        return -1

    blk_size = 256
    finish_size = 0
    while True:
        buffer  = u.read(blk_size) # read blk_size file data for mutlti times
        if not buffer:
            break # read finish

        finish_size += len(buffer)
        f.write(buffer)
    f.close()
    return 0

