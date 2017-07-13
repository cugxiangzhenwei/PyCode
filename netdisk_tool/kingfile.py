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
    
if __name__=='__main__':
    get_server_info()
    login(0,'xiangzhenwei','ACFGkp1017','kingfile')
    get_user_info(net_disk_global.token)

    list_arry = get_share_home_list()
    for i in list_arry['data']:
       recv_sub =  get_share_file_list(i['xid'],net_disk_global.token,1,1)
       sub_list = json.loads(recv_sub)
       print_file_list(sub_list)

    get_priave_home_list()
