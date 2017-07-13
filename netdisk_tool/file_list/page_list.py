#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.global_data import net_disk_global
import json

def get_file_list(xid,token,sortBy,order,bIsPublic):
    print 'begin to get file list from %d' %(xid)
    url  = net_disk_global.common_url + "/api/v1/xfile/dir/cage/page/list"
    if bIsPublic:
        url  = net_disk_global.common_url + "/api/v1/xfile/dir/share/page/list"

    js_data = {'token':token,'xid':xid,'sortBy':sortBy,'order':order}
    post_data = json.dumps(js_data)
    recv = json_request(url,post_data)
    return recv

def get_share_file_list(xid,token,sortBy,order):
    return get_file_list(xid,token,sortBy,order,True)


def get_private_file_list(xid,token,sortBy,order):
    return get_file_list(xid,token,sortBy,order,False)
