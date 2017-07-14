#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from global_data import net_disk_global
import sys
sys.path.append("..")
from http.json_request import json_request

def get_server_info(url):
    srvInfo = json_request(url,'{}')
    jsonInfo = json.loads(srvInfo)
    blockInfo = jsonInfo['data']['block']
    upload_host = blockInfo['upload']['host']
    upload_port = blockInfo['upload']['port']
    upload_api_path = blockInfo['upload']['path']
    print ('upload host = %s,port =%d,path=%s'% (upload_host,upload_port,upload_api_path))

    download_host = blockInfo['download']['host']
    download_port = blockInfo['download']['port']
    download_api_path = blockInfo['download']['path']
    print ('download host = %s,port =%d,path=%s'% (download_host,download_port,download_api_path))

    common_host = jsonInfo['data']['common']['host']
    common_port = jsonInfo['data']['common']['port']
    print 'common host =%s,port=%d'%(common_host,common_port)
    net_disk_global.upload_host = upload_host
    net_disk_global.upload_port = upload_port
    net_disk_global.download_host = download_host
    net_disk_global.download_port = download_port
    net_disk_global.common_host = common_host
    net_disk_global.common_port = common_port
    net_disk_global.crypto = jsonInfo['data']['crypto']
    net_disk_global.upload_url = upload_host + ':' + str(upload_port) + upload_api_path
    net_disk_global.download_url = download_host + ':' + str(download_port) + download_api_path
    net_disk_global.common_url = common_host + ':' + str(common_port)
    print 'upload_url= %s'%(net_disk_global.upload_url)
    print 'download_url= %s'%(net_disk_global.download_url)
    print 'common_url= %s'%(net_disk_global.common_url)
    print 'crypto state=%d'%(net_disk_global.crypto)

if __name__ == '__main__':
    get_server_info()
