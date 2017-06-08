#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a test wrapper module'

__author__ = 'Xiang Zhen Wei'
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'begin call %s()' % func.__name__
        data = func(*args,**kw)
        print 'end call %s()' % func.__name__
        return data
    return wrapper
@log
def f():
    print 'function f called!'

f()
print f.__name__
