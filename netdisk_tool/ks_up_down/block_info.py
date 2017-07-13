#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class ks_block_info(object):
    def __init__(self):
        self.id = 0
        self.t = ''
        self.md5 = ''
        self.sha1 = ''
        self.m = json.loads('{}')

class ks_file_block_info(object):
    def __init__(self):
        self.file_version = 0
        self.xid = 0
        self.ks_block_list = []
