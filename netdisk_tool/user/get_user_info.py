#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.global_data import net_disk_global
import json

def get_user_info(token):
    url = net_disk_global.common_url + '/api/v1/account/info';
    json_data  = {'token':token}
    post_data = json.dumps(json_data)
    recv = json_request(url,post_data)
    js_rev = json.loads(recv)
    net_disk_global.domain_ident = js_rev['data']['domain_ident']
    net_disk_global.share_home = js_rev['data']['share_home']
    net_disk_global.cage_home = js_rev['data']['cage_home'] 
    net_disk_global.user_xid = js_rev['data']['xid']
    net_disk_global.user_email = js_rev['data']['email']
    net_disk_global.staff_name = js_rev['data']['staff_name']
    net_disk_global.domain_name = js_rev['data']['domain_name']
    net_disk_global.domain_id = js_rev['data']['domain_id']
    net_disk_global.super_type = js_rev['data']['super_type']

if __name__ == "__main__":
    net_disk_global.common_url = 'https://pan.ksyun.com:443'
    get_user_info('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MDA1MTk4ODAsImlzcyI6ImxvZ2luIiwidXNlcl9pZCI6MTQ4MywiaXNhIjoxNDk5OTE1MDgwLCJkZXZpY2UiOiJQQy1QeXRvb2wtezAwLTBDLTI5LUQzLTk3LTFCfSJ9.NJD5nbdygWMkSKmrvTmIlEYPAgcAG55qATm-5sq7rfI')
