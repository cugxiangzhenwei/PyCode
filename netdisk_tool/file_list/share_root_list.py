#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.global_data import net_disk_global
import json

def get_share_root_list(share_root_xid,token,sortBy,order):
    print 'begin to get share root list from %d' %(share_root_xid)
    url  = net_disk_global.common_url + "/api/v1/xfile/dir/share/root/list"
    js_data = {'token':token,'xid':share_root_xid,'sortBy':sortBy,'order':order}
    post_data = json.dumps(js_data)
    recv = json_request(url,post_data)
    return recv

