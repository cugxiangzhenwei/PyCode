#!/usr/bin/env python
# -*- coding:utf-8 -*-
'a module to build index.html from local html blog files,auto search title'
import os
import re
import sys

def get_title(html):
    # ht = html.decode('UTF-8')
    ht = html
    prefix = '<span class="link_title"><a href="/'
    p = ht.find(prefix) + len(prefix)
    ht = ht[p+1:p+300]
    p = ht.find('">') + 2
    end = ht.find('</a></span>')
    t = ht[p:end]
    return t

def build_index_file(indexfile,input_dir):
   if os.path.exists(indexfile):
        os.remove(indexfile)

   reload(sys)
   sys.setdefaultencoding('utf8')
   out = open(indexfile,'w')
   out.write("<head>\n")
   out.write("<body>\n")
   htmlList = [x for x in os.listdir(input_dir) if os.path.splitext(x)[1]=='.html']    
   for i in htmlList:
        p = os.path.join(input_dir,i)
        with open(p) as f:
            html = f.read()
            f.close()
            t = get_title(html)
            s = '<a href="%s">%s</a></br>\n' %(p,t)
            out.write(s)
    
   out.write("</body>\n")
   out.write("</head>\n")
   out.close()
   print 'build index.html successfully,process html count %d,save index.html to %s' %(len(htmlList),indexfile)
            


if __name__=='__main__':
    p  = os.path.join(os.path.abspath('.'),'blog')
    build_index_file('./gaoxingneng_index.html',p)

