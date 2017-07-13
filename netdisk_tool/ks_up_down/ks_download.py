#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.global_data import net_disk_global
import json
from block_info import *

class ks_download(object):
    def  __init__(self,xid,token,fileVer):
        self.xid = xid
        self.token = token
        self.m_fileVer = fileVer
        self.m_blockCount = 0

    def perform():
        code,result_blocks = download_prepare()
        if code!=0
            print 'download_prepare error!'
            return code
        code = download_blocks(result_blocks)
        return code

    def download_prepare():
        url = net_disk_global.common_url + "/v3/xfile/file/download/prepare"
        js_data  = {'xid':xid,'token':token,'fileVer':fileVer}
        post_data = json.dumps(js_data)
        recv = json_request(url,post_data)
        js_rev = json.loads(recv)
        if js_rev['code']!=0:
            print 'faile to call downlaod prepare v3'
            return code,None

        result_blocks = ks_file_block_info()
        data = js_rev['data']
        block_max = data['block_max']
        m_blockCount = block_max + 1
        file_version = data['file_version']
        m_fileVer = file_version
        bundle  = data['bundle']
        for b in bundle:
           blf = ks_block_info()
           blf.id = b['i']
           blf.t = b['t']
           blf.md5 = b['w']
           blf.sha1 = b['s']
           blf.m = b['m']
           result_blocks.append(blf)

        return code,result_blocks
        
    
    def download_blocks(result_blocks):
        print 'download_blocks called,input block count=%d'%len(result_blocks)
        return 0
