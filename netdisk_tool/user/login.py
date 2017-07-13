#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.server_info import get_server_info
from net_disk_global.global_data import net_disk_global
import json
import time

def login(login_type,usr_name,usr_pwd,domain_indent):
    login_url = net_disk_global.common_url + '/api/v1/account/login'
    dict_js = {'loginType':login_type,'loginTag':usr_name,'userPwd':usr_pwd,'domainIdent':domain_indent}
    post_data = json.dumps(dict_js)
    print post_data
    login_result = json_request(login_url,post_data)
    js_rev = json.loads(login_result)
    code = js_rev['code']
    if code!=0:
        print 'login failed!'
        return
    net_disk_global.token = js_rev['data']['token']
    net_disk_global.token_start = time.time()
    net_disk_global.expires_in = js_rev['data']['expires_in']
    print 'net_disk_global.token=%s'%(net_disk_global.token)


if __name__=='__main__':
    get_server_info()
    login(0,'xiangzhenwei','123456','cugxiangzhenwei')
