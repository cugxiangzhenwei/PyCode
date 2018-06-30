#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a module to get map tile image file'
import os
import requests
import threading
import Queue
from coordinate import Tile,geo2Tile

NUM_THREADS = 40
MIN_LON = 110.611961
MAX_LAT = 33.356915

MAX_LON = 111.036994
MIN_LAT = 33.118575

TOTAL = 0
FINISHED = 0

# 定义同时队列数
queue = Queue.Queue()

class Task():
    def __init__(self,mainurl,x,y,z):
        self._mainurl = mainurl
        self._x = x
        self._y = y
        self._z = z


def download_file_v2(url,outfile):
    #print 'download from url:%s' % url
    r = requests.get(url)
    f = open(outfile,'wb')
    f.write(r.content)
    f.close()


def download_map_tile(mainurl,x,y,z):
    full_url = mainurl + 'x=%d&y=%d&z=%d'%(x,y,z)
    save_file = './tile/%d_%d_%d.png'%(x,y,z)
    print 'Begin to download tile from:%s,save to %s' %(full_url,save_file)
    download_file_v2(full_url,save_file)
    print 'download blog finished'


def download_task(queue):
    while queue.empty() == False:
        task = queue.get()
        full_url = task._mainurl + 'x=%d&y=%d&z=%d'%(task._x,task._y,task._z)
        save_file = './tile/%d_%d_%d.png'%(task._x,task._y,task._z)
        global FINISHED
        FINISHED+=1
        queue.task_done()
        print 'download tile(%d,%d,%d,progress=%d%%)' %(task._x,task._y,task._z,FINISHED*100/TOTAL)
        download_file_v2(full_url,save_file)



def download_range(leftTopLong,leftTopLat,rightBottomLong,rightBottomLat,zoom):
    tileLeftTop = geo2Tile(leftTopLong,leftTopLat,zoom)
    tileRightBottom = geo2Tile(rightBottomLong,rightBottomLat,zoom)
    print tileLeftTop.x,' ', tileLeftTop.y
    print tileRightBottom.x,' ', tileRightBottom.y
    count = (tileRightBottom.x - tileLeftTop.x)*( tileRightBottom.y - tileLeftTop.y)
    global TOTAL
    global FINISHED
    TOTAL = count
    FINISHED = 0
    print 'download xmin=%d,ymin=%d,xmax=%d,ymax=%d,z=%d' % (tileLeftTop.x,tileLeftTop.y,tileRightBottom.x,tileRightBottom.y,zoom)
    print 'Tile Count %d'%count
    if not os.path.exists('./tile/'):
        os.makedirs('./tile/')
    threads = []
    for x in range(tileLeftTop.x,tileRightBottom.x):
        for y in range(tileLeftTop.y,tileRightBottom.y):
            mainurl = 'http://www.google.cn/maps/vt?lyrs=s@729&gl=cn&'
            task = Task(mainurl,x,y,zoom)
            queue.put(task)

    for i in range(0,NUM_THREADS):
        t  = threading.Thread(target=download_task,args=(queue,))
        threads.append(t)
        t.setDaemon(True)
        t.start()

    queue.join()

    for t in threads:
        t.join()
download_range(MIN_LON,MAX_LAT,MAX_LON,MIN_LAT,18)
print 'download map tile finished'

