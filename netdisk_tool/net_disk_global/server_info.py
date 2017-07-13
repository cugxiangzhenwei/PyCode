#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from global_data import net_disk_global
import sys
sys.path.append("..")
from http.json_request import json_request

def get_server_info():
    url = 'https://pan.ksyun.com:443/api/v2/server/info'
    srvInfo = json_request(url,'{}')
    jsonInfo = json.loads(srvInfo)
    blockInfo = jsonInfo['data']['block']
    upload_host = blockInfo['upload']['host']
    upload_port = blockInfo['upload']['port']
    print ('upload host = %s,port =%d'% (upload_host,upload_port))

    download_host = blockInfo['download']['host']
    download_port = blockInfo['download']['port']
    print ('download host = %s,port =%d'% (download_host,download_port))

    common_host = jsonInfo['data']['common']['host']
    common_port = jsonInfo['data']['common']['port']
    print 'common host =%s,port=%d'%(common_host,common_port)
    net_disk_global.upload_host = upload_host
    net_disk_global.upload_port = upload_port
    net_disk_global.download_host = download_host
    net_disk_global.download_port = download_port
    net_disk_global.common_host = common_host
    net_disk_global.common_port = common_port
    net_disk_global.upload_url = upload_host + ':' + str(upload_port)
    net_disk_global.download_url = download_host + ':' + str(download_port)
    net_disk_global.common_url = common_host + ':' + str(common_port)
    print 'upload_url= %s'%(net_disk_global.upload_url)
    print 'download_url= %s'%(net_disk_global.download_url)
    print 'common_url= %s'%(net_disk_global.common_url)

if __name__ == '__main__':
    get_server_info()
