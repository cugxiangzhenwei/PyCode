#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a module to test sqlite operation by pyhon'
import sqlite3

cx = sqlite3.connect('./KingFileSyncDisk_kingfile_xiangzhenwei.db')
cu = cx.cursor()
cu.execute('select * from sync_path')
rev = cu.fetchall()
for i in range(len(rev)):
    for j in range(len(rev[i])):
        print rev[i][j],'\t',
    print '\n'

cu.execute("update sync_path set local_path='./test/' where xid = 8589934611")
cx.commit()
cu.execute('select * from sync_path')
rev = cu.fetchall()
for i in range(len(rev)):
    for j in range(len(rev[i])):
        print rev[i][j],'\t',
    print '\n'
