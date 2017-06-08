#!/usr/bin/env python
import sys
import logging
import pdb

def test(a):
    pdb.set_trace()
    try:
        a = int(a)
    except ValueError, e:
        print 'ValueError',e
    else:
        if isinstance(a,int) == False:
            raise  ValueError('%s is not int param!' % a)
        try:
            print 'try...'
            r = 10 / a
            print 'result:', r
        except ZeroDivisionError, e:
            print 'except:', e
        finally:
            print 'finally...'
            print 'END'

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'less paramter,at least two param!'
    else:
        try:
            test(sys.argv[1])
        except StandardError, e:
            logging.exception(e)
        else:
            logging.info('End')
