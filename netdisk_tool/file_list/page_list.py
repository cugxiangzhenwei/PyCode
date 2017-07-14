#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.global_data import net_disk_global
import json

def get_file_list(xid,token,sortBy,order,pageMax,pageIdx,bIsPublic):
    print 'begin to get file list from %d' %(xid)
    url  = net_disk_global.common_url + "/api/v1/xfile/dir/cage/page/list"
    if bIsPublic:
        url  = net_disk_global.common_url + "/api/v1/xfile/dir/share/page/list"

    js_data = {'token':token,'xid':xid,'sortBy':sortBy,'order':order,'pageMax':pageMax,'pageIdx':pageIdx}
    post_data = json.dumps(js_data)
    recv = json_request(url,post_data)
    return recv

def get_share_file_list(xid,token,sortBy,order,pageMax,pageIdx):
    return get_file_list(xid,token,sortBy,order,pageMax,pageIdx,True)


def get_private_file_list(xid,token,sortBy,order,pageMax,pageIdx):
    return get_file_list(xid,token,sortBy,order,pageMax,pageIdx,False)
    

def get_share_file_list(xid,token,sortBy,order):
    pageMax = 20
    pageIdx = 0
    list_result = {'code':0,'data':[]}
    while True:
        recv =  get_file_list(xid,token,sortBy,order,pageMax,pageIdx,True)
        js_data = json.loads(recv)
        if (js_data['code']!=0 or len(js_data['data']) < pageMax):
            break
        for i in js_data['data']:
            list_result['data'].append(i)
        pageIdx = pageIdx + 1
    str_rev = json.dumps(list_result)
    return str_rev
        

def get_private_file_list(xid,token,sortBy,order):
    pageMax = 20
    pageIdx = 0
    list_result = {'code':0,'data':[]}
    while True:
        recv =  get_file_list(xid,token,sortBy,order,pageMax,pageIdx,False)
        js_data = json.loads(recv)
        if (js_data['code']!=0 or len(js_data['data']) < pageMax):
            break
        for i in js_data['data']:
            list_result['data'].append(i)
        pageIdx = pageIdx + 1
    str_rev = json.dumps(list_result)
    return str_rev
