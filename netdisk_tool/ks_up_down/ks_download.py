#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("..")
from http.json_request import json_request
from net_disk_global.global_data import net_disk_global
import json
from block_info import *
from block_download import *

class ks_download(object):
    def  __init__(self,xid,token,fileVer):
        self.xid = xid
        self.token = token
        self.m_fileVer = fileVer
        self.m_blockCount = 0
        self.m_save_path = ''
        self.m_block_index_start = 0

    def perform(self,save_file_path):
        self.m_save_path = save_file_path
        code,result_blocks = self.__download_prepare()
        if code!=0:
            print 'download_prepare error!'
            return code
        code = self.__download_blocks(result_blocks)
        if not (code==0):
            return code

        while True: # loop diff blocks then download them
            sy = self.m_blockCount - self.m_block_index_start
            blk_count  = 16
            if sy < 16:
                blk_count = sy
            if blk_count ==0:
                break #all finish
            code,result_blocks = self.__download_diff(self.m_block_index_start,blk_count)
            if code ==0:
                code = self.__download_blocks(result_blocks)
            else:
                return code
        return code

    def __pro_bundle_info(self,recv):
        js_rev = json.loads(recv)
        if js_rev['code']!=0:
            return js_rev['code'],None

        result_blocks = ks_file_block_info()
        data = js_rev['data']
        block_max = data['block_max']
        self.m_blockCount = block_max + 1
        file_version = data['file_version']
        self.m_fileVer = file_version
        bundle  = data['bundle']
        for b in bundle:
           blf = ks_block_info()
           blf.id = b['i']
           blf.t = b['t']
           blf.md5 = b['w']
           blf.sha1 = b['s']
           blf.m = b['m']
           result_blocks.ks_block_list.append(blf)
        return js_rev['code'],result_blocks
        

    def __download_prepare(self):
        url = net_disk_global.common_url + "/api/v3/xfile/file/download/prepare"
        js_data  = {'xid':self.xid,'token':self.token,'fileVer':self.m_fileVer}
        post_data = json.dumps(js_data)
        recv = json_request(url,post_data)
        return self.__pro_bundle_info(recv)
        
    def __get_block_bundle_info(self,bids):
        url = net_disk_global.common_url + "/api/v2/xfile/file/download/diff"
        js_data  = {'xid':self.xid,'token':self.token,'fileVer':self.m_fileVer,'bids':bids}
        post_data = json.dumps(js_data)
        recv = json_request(url,post_data)
        return self.__pro_bundle_info(recv)

    def __download_diff(self,iStartIndex,blkCount):
        bids = range(iStartIndex,iStartIndex + blkCount)
        return self.__get_block_bundle_info(bids)

    def __download_blocks(self,result_blocks):
        print 'download_blocks called,input block count=%d'%len(result_blocks.ks_block_list)
        cache = os.environ['HOME'] + '/kingfile/cache/' 
        if not os.path.exists(cache):
            os.makedirs(cache)
        for blk in result_blocks.ks_block_list:
            blk_save_path =  cache + blk.sha1 + '.sha1'
            iRev = self.__download_block(blk,blk_save_path)
            if not (iRev==0): 
                return iRev
            iRev = self.__merge_block(blk_save_path)
            if not (iRev==0): 
                return iRev
            self.m_block_index_start +=1
        return 0

    def __download_block(self,blf,blk_save_path):
        down_url = net_disk_global.download_url + blf.t
        iRev = http_download(blf.m,down_url,blk_save_path)
        print 'download_block called ,block index=%d,save_path=%s,from url = %s,return value=%d'%(blf.id,blk_save_path,down_url,iRev)
        return iRev

    def __merge_block(self,blk_save_path):
        print 'begin to merge block file %s to out file %s' %(blk_save_path,self.m_save_path) 
        with open(blk_save_path,'rb') as blk:
            with open(self.m_save_path,'ab') as fo:
                buffer  = blk.read()
                if buffer:
                    fo.write(buffer)
                blk.close()
                fo.close()
                return 0
            blk.close()
            print 'failed to open out file %s'%self.m_save_path
            return -2
        print 'failed to opent block file %s'%blk_save_path
        return -1
