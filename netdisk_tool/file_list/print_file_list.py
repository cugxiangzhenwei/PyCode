#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
def print_file_list(list_arry):
    for i in list_arry['data']:
        print '%-50s %-20d'%(i['name'],i['xid']),
        if 'role' in i:
            print '角色:%-8d'%(i['role']),
        ta = time.localtime(i['ctime'])
        print time.strftime('%Y-%m-%d %H:%M:%S',ta)
