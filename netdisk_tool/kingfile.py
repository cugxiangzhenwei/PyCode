#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import json
from net_disk_global.global_data import net_disk_global
from net_disk_global.server_info import *
from user.login import *
from user.get_user_info import *
from file_list.share_root_list import get_share_root_list
from file_list.page_list import *
from file_list.print_file_list import print_file_list
from ks_up_down.ks_download import *
from ks_up_down.encrypt_key import *

def get_priave_home_list():
       recv_sub =  get_private_file_list(net_disk_global.cage_home,net_disk_global.token,1,1)
       sub_list = json.loads(recv_sub)
       print_file_list(sub_list)
       return sub_list

def get_share_home_list():
    recv = get_share_root_list(net_disk_global.share_home,net_disk_global.token,1,1)
    list_arry = json.loads(recv)
    print_file_list(list_arry)
    return list_arry
    
def test_download(xid,filename):
    download = ks_download(xid,net_disk_global.token,-1)
    save_dir = os.environ['HOME'] + '/kingfile/download/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_file = save_dir + filename
    download.perform(save_file)

def test_filelist():
    list_arry = get_share_home_list()
    for i in list_arry['data']:
       recv_sub =  get_share_file_list(i['xid'],net_disk_global.token,1,1)
       sub_list = json.loads(recv_sub)
       print_file_list(sub_list)

    get_priave_home_list()

if __name__=='__main__':
    url = 'https://pan.ksyun.com/api/v2/server/info'
    #url = 'http://192.168.140.110/api/v2/server/info'
    get_server_info(url)
    login(0,'xiangzhenwei','ACFGkp1017','kingfile')
   #login(0,'zzy','123456','ceshi001')
    get_user_info(net_disk_global.token)
    get_encrypt_key_info()
   # test_filelist()
    test_download(605590409744,'DingDan.txt')
    #test_download(25770001893,'test.docx')


