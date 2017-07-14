#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.global_data import net_disk_global
from server_api import *
import json
import time

class Encrypt_Key_Info(object):
   def __init__(self):
        self.timestamp = 0
        self.client_key = ''
        self.domain_id = ''
        self.user_xid = 0
        self.xid = 0
        self.m_strHexKey = '' #fetch this value from transfer_shakehand_encrypt_key api

global_encrypt_key = Encrypt_Key_Info()

def get_encrypt_key_info():
    url  =  net_disk_global.common_url + transfer_shakehand_encrypt_key
    strRandomKey = '3242423'
    t = time.time()
    js_data = {'xid':net_disk_global.user_xid,'token':net_disk_global.token,'clientKey':strRandomKey,'clientTime':t}
    post_data = json.dumps(js_data)
    recv = json_request(url,post_data)
    js_rev = json.loads(recv)
    if not js_rev['code']==0:
        return js_rev['code']

    global_encrypt_key.user_xid = net_disk_global.user_xid
    global_encrypt_key.domain_id = net_disk_global.domain_id
    global_encrypt_key.timestamp = t 
    global_encrypt_key.xid = net_disk_global.user_xid
    global_encrypt_key.client_key = strRandomKey
    global_encrypt_key.m_strHexKey = js_rev['data']['key']
    print 'encrypt key:' + global_encrypt_key.m_strHexKey
    return 0
        

