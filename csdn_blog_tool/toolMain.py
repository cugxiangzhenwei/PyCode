#!/usr/bin/env python
# -*- coding:utf-8 -*-
'main interface of blog tool'
import getblog_mutliThread
import build_local_index
import os
import sys, getopt

def usage():
    print "python toolMain.py -h help -d outdir -o outIndex.html"

if __name__=='__main__':
      opts, args = getopt.getopt(sys.argv[1:], "hu:o:d:")
      if len(sys.argv) < 3:
        print "参数不足"
        usage()
        sys.exit()

      url = 'http://blog.csdn.net/gaoxingnengjisuan/article/list/'
      outdir = './blog/'
      outfile = './gaoxingnengjisuan_index.html'
      for op, value in opts:
        if op == '-u':
            url = value
        elif op == '-o':
            outfile = value
        elif op == '-d':
            outdir = value
        elif op == '-h':
            usage()
            sys.exit()
      
      print 'url = %s,outdir = %s,outfile = %s' %(url,outdir,outfile)
      getblog_mutliThread.auto_search_download_all(url,outdir)
      build_local_index.build_index_file(outfile,outdir)
     # p  = os.path.join(os.path.abspath('.'),'gaoxingnengjisuan_blog')
     # print 'Download to %s' %(p,)
     # getblog_mutliThread.auto_search_download_all('http://blog.csdn.net/gaoxingnengjisuan/article/list/',p)
     # build_local_index.build_index_file('./gaoxingnengjisuan_index.html',p)
      print "Tool process finished,exit!"
